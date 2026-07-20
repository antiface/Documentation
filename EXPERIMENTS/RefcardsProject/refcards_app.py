# The Refcards-System is a desktop knowledge management application built in Python with Tkinter,
# designed for researchers and creators to author, index, and organize atomic notes ("Refcards").
# It features a custom boolean search engine with field scoping, dynamic keyword-frequency faceted
# filtering, saved "Cardbox" collection views, and automatic plain-text backups.

import os
import re
import csv
import json
import uuid
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from collections import Counter, defaultdict


class RefcardsSystemEngine(tk.Tk):
    """
    Main Application Class for The Refcards-System - Desktop Knowledge Desk.

    Provides an interface for managing atomic research notes ("Refcards").
    Handles UI layout, database I/O, search logic, and persistent storage.
    """

    def __init__(self):
        """Initializes the application state, styles, database connections, and UI."""
        super().__init__()
        self.title("The Refcards-System - Desktop Knowledge Desk")
        self.geometry("1240x850")
        self.minsize(1000, 650)

        # Color Palette Settings
        self.COLOR_BG = "#FAF9F5"
        self.COLOR_INK = "#1A1E21"
        self.COLOR_TEAL = "#2A6B70"
        self.COLOR_CARD_BG = "#FFFFFF"
        self.COLOR_CRIMSON = "#A63A3A"

        self.configure(bg=self.COLOR_BG)
        self.setup_styles()

        # Hardcoded CSV File Targeting Schema
        self.DB_FILE = "refcards_database.csv"
        self.csv_headers = ["ID", "DATETIME", "EXPERIMENT", "PURPOSE", "PROCEDURE", "NOTES"]

        self.initialize_blank_csv_if_missing()

        # In-Memory Application States
        self.all_data = []      # All Refcards loaded from CSV
        self.active_data = []   # Currently displayed/filtered Refcards

        # Facet selections map structured by (field, keyword) tuples
        self.facet_selections = {}
        self.expanded_facets = {h: False for h in self.csv_headers if h not in ["ID", "DATETIME"]}

        # Saved Cardbox collections
        self.cardboxes = self.load_cardboxes_from_disk()

        # Internal lock flag to prevent cyclic infinite query generation loops during rendering
        self._updating_facets_lock = False

        self.build_ui_layout()
        self.reload_data_from_csv()
        self.show_all_records_action()

    def setup_styles(self):
        """Configures the ttk Style engine for consistent visual theming."""
        self.option_add("*Font", "TkDefaultFont 10")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(".", background=self.COLOR_BG, foreground=self.COLOR_INK)
        style.configure("TLabel", background=self.COLOR_BG, foreground=self.COLOR_INK)
        style.configure("TFrame", background=self.COLOR_BG)
        style.configure("Card.TFrame", background=self.COLOR_CARD_BG, relief="solid", borderwidth=1)

    def initialize_blank_csv_if_missing(self):
        """Ensures the existence of the CSV database file; creates a new one with headers if absent."""
        if not os.path.exists(self.DB_FILE):
            with open(self.DB_FILE, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.csv_headers)

    def load_cardboxes_from_disk(self):
        """Loads persistent JSON configuration for saved Cardbox views."""
        try:
            if os.path.exists("saved_cardboxes.json"):
                with open("saved_cardboxes.json", "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return {}

    def save_cardboxes_to_disk(self):
        """Persists the current Cardbox configurations to a JSON file."""
        try:
            with open("saved_cardboxes.json", "w", encoding="utf-8") as f:
                json.dump(self.cardboxes, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def reload_data_from_csv(self):
        """Synchronizes in-memory data with the CSV database file."""
        parsed_rows = []
        try:
            with open(self.DB_FILE, mode="r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    clean_row = {k.strip(): v for k, v in row.items() if k}
                    parsed_rows.append(clean_row)
            self.all_data = parsed_rows
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not read database file: {e}")

    def export_to_text_file(self, record_dict):
        """
        Creates a plain-text backup of a Refcard record.

        :param record_dict: Dictionary containing Refcard data.
        """
        dt_str = record_dict.get("DATETIME", "").strip()
        numeric_stamp = "".join(re.findall(r'\d+', dt_str))[:12]
        if not numeric_stamp or len(numeric_stamp) < 12:
            numeric_stamp = datetime.now().strftime("%Y%m%d%H%M")
        filename = f"{numeric_stamp}.txt"

        try:
            parsed_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            formatted_time = parsed_dt.strftime("%a %b %e %H:%M:%S %Y")
        except Exception:
            formatted_time = dt_str

        content = (
            f"Time: {formatted_time}\n\n"
            f"Experiment: {record_dict.get('EXPERIMENT', '')}\n\n"
            f"Statement of Purpose: {record_dict.get('PURPOSE', '')}\n\n"
            f"Procedure: {record_dict.get('PROCEDURE', '')}\n\n"
            f"Notes: {record_dict.get('NOTES', '')}\n"
        )
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Warning: Failed to export system backup file {filename}: {e}")

    def save_record_to_csv(self, record_dict, is_new=True):
        """
        Updates the in-memory data collection, triggers a text backup, and flushes to disk.

        :param record_dict: The Refcard data dictionary.
        :param is_new: Boolean flag indicating if this is a new entry.
        """
        if is_new:
            self.all_data.append(record_dict)
        else:
            for i, row in enumerate(self.all_data):
                if row["ID"] == record_dict["ID"]:
                    self.all_data[i] = record_dict
                    break
        self.export_to_text_file(record_dict)
        self.flush_all_data_to_disk()

    def remove_record_from_csv(self, record_id):
        """
        Deletes a specific record by ID and synchronizes the disk.

        :param record_id: Unique string ID of the record.
        """
        self.all_data = [row for row in self.all_data if row["ID"] != record_id]
        self.flush_all_data_to_disk()

    def flush_all_data_to_disk(self):
        """Writes current in-memory Refcards to the CSV database and triggers a refresh."""
        try:
            with open(self.DB_FILE, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.csv_headers)
                writer.writeheader()
                writer.writerows(self.all_data)
            self.reload_data_from_csv()
            self.execute_search_pipeline(update_facets_ui=True)
        except Exception as e:
            messagebox.showerror("Write Error", f"Could not write database changes to disk: {e}")

    def build_ui_layout(self):
        """Constructs the application GUI layout including headers, search bar, and panes."""
        # TOP UTILITIES BAR
        top_bar = ttk.Frame(self, padding=10)
        top_bar.pack(fill=tk.X, side=tk.TOP)
        title_lbl = tk.Label(top_bar, text="The Refcards-System", font=("TkDefaultFont", 16, "bold"), fg=self.COLOR_TEAL, bg=self.COLOR_BG)
        title_lbl.pack(side=tk.LEFT, padx=5)
        btn_new_card = tk.Button(top_bar, text="+ New Refcard", command=lambda: self.open_refcard_editor(), bg=self.COLOR_CARD_BG, relief="groove", font=("TkDefaultFont", 10, "bold"), cursor="hand2")
        btn_new_card.pack(side=tk.RIGHT, padx=5)
        btn_help = tk.Button(top_bar, text="? Syntax Help", command=self.display_syntax_popover, bg=self.COLOR_CARD_BG, relief="groove", cursor="hand2")
        btn_help.pack(side=tk.RIGHT, padx=5)

        # SEARCH COMMAND CENTER
        search_container = ttk.Frame(self, padding=10)
        search_container.pack(fill=tk.X, side=tk.TOP)
        search_input_row = ttk.Frame(search_container)
        search_input_row.pack(fill=tk.X, expand=True)
        self.search_val = tk.StringVar()
        self.search_entry = tk.Entry(search_input_row, textvariable=self.search_val, font=("TkDefaultFont", 11), bg="#FFFFFF", fg=self.COLOR_INK, insertbackground=self.COLOR_INK)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        self.search_entry.bind("<Return>", lambda e: self.execute_search_pipeline(update_facets_ui=True))
        btn_search = tk.Button(search_input_row, text="Search", command=lambda: self.execute_search_pipeline(update_facets_ui=True), bg=self.COLOR_TEAL, fg="#FFFFFF", relief="flat", font=("TkDefaultFont", 10, "bold"), padx=25, cursor="hand2")
        btn_search.pack(side=tk.LEFT, padx=2)

        # INTERACTIVE CARDBOXES ROW
        actions_row = ttk.Frame(search_container, padding=(0, 8, 0, 0))
        actions_row.pack(fill=tk.X)
        lbl_cardbox = ttk.Label(actions_row, text="Cardbox Collections:", font=("TkDefaultFont", 9, "bold"))
        lbl_cardbox.pack(side=tk.LEFT, padx=(5, 2))
        self.dropdown_var = tk.StringVar()
        self.cardbox_dropdown = ttk.Combobox(actions_row, textvariable=self.dropdown_var, state="readonly", width=25)
        self.cardbox_dropdown['values'] = list(self.cardboxes.keys())
        self.cardbox_dropdown.pack(side=tk.LEFT, padx=5)
        self.cardbox_dropdown.bind("<<ComboboxSelected>>", self.on_cardbox_dropdown_select)
        btn_delete_box = tk.Button(actions_row, text="Delete Box", command=self.delete_selected_cardbox, bg=self.COLOR_CARD_BG, fg=self.COLOR_CRIMSON, relief="groove", font=("TkDefaultFont", 9), cursor="hand2")
        btn_delete_box.pack(side=tk.LEFT, padx=2)
        btn_save_box = tk.Button(actions_row, text="Store View as Cardbox...", command=self.save_cardbox_dialog, bg=self.COLOR_CARD_BG, relief="groove", font=("TkDefaultFont", 9), cursor="hand2")
        btn_save_box.pack(side=tk.LEFT, padx=5)
        btn_show_all = tk.Button(actions_row, text="Show All Refcards", command=self.show_all_records_action, bg=self.COLOR_CARD_BG, fg=self.COLOR_TEAL, relief="groove", font=("TkDefaultFont", 9), cursor="hand2")
        btn_show_all.pack(side=tk.RIGHT, padx=5)
        btn_clear_search = tk.Button(actions_row, text="Clear Search Desk", command=self.clear_entire_search_action, bg=self.COLOR_CARD_BG, fg=self.COLOR_INK, activeforeground="#FFFFFF", activebackground=self.COLOR_TEAL, relief="groove", font=("TkDefaultFont", 9), cursor="hand2")
        btn_clear_search.pack(side=tk.RIGHT, padx=5)

        # SPLIT BODY CONTAINER
        body_paned = tk.PanedWindow(self, orient=tk.HORIZONTAL, bg="#E0DBD3", sashwidth=4)
        body_paned.pack(fill=tk.BOTH, expand=True, side=tk.TOP, padx=10, pady=10)

        # LEFT PANE: FACET SIDEBAR WITH SCROLLING
        sidebar_outer = ttk.Frame(body_paned)
        self.sidebar_canvas = tk.Canvas(sidebar_outer, width=280, bg=self.COLOR_BG, highlightthickness=0)
        sidebar_scroll = ttk.Scrollbar(sidebar_outer, orient=tk.VERTICAL, command=self.sidebar_canvas.yview)
        self.sidebar_frame = ttk.Frame(self.sidebar_canvas, padding=10)
        self.sidebar_canvas.create_window((0, 0), window=self.sidebar_frame, anchor="nw")
        self.sidebar_canvas.configure(yscrollcommand=sidebar_scroll.set)
        sidebar_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.sidebar_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.sidebar_frame.bind("<Configure>", lambda e: self.sidebar_canvas.configure(scrollregion=self.sidebar_canvas.bbox("all")))

        # RIGHT PANE: RESULTS WORKSPACE
        self.main_view_container = ttk.Frame(body_paned, padding=5)
        body_paned.add(sidebar_outer, minsize=260)
        body_paned.add(self.main_view_container, minsize=500)

        self.counter_lbl = ttk.Label(self.main_view_container, text="", font=("TkDefaultFont", 11, "bold"))
        self.counter_lbl.pack(anchor=tk.W, pady=(0, 5))

        self.feed_canvas = tk.Canvas(self.main_view_container, bg=self.COLOR_BG, highlightthickness=0)
        feed_scroll = ttk.Scrollbar(self.main_view_container, orient=tk.VERTICAL, command=self.feed_canvas.yview)
        self.feed_scroll_frame = ttk.Frame(self.feed_canvas)
        self.feed_canvas_window = self.feed_canvas.create_window((0, 0), window=self.feed_scroll_frame, anchor="nw")
        self.feed_canvas.configure(yscrollcommand=feed_scroll.set)
        feed_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.feed_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.feed_scroll_frame.bind("<Configure>", lambda e: self.feed_canvas.configure(scrollregion=self.feed_canvas.bbox("all")))
        self.feed_canvas.bind("<Configure>", lambda e: self.feed_canvas.itemconfig(self.feed_canvas_window, width=e.width))

    def save_cardbox_dialog(self):
        """Displays a dialog to name and save the current search state."""
        query = self.search_val.get().strip()
        active_facets = [[field, kw] for (field, kw), var in self.facet_selections.items() if var.get()]

        if not query and not active_facets:
            messagebox.showwarning("Empty View", "Cannot store an empty Cardbox. Please enter a search query or select some facet filters.")
            return

        dialog = tk.Toplevel(self)
        dialog.title("Define Cardbox Label")
        dialog.geometry("400x150")
        dialog.configure(bg=self.COLOR_BG)
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        lbl = tk.Label(dialog, text="Enter Name for this Cardbox Collection View:", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_BG)
        lbl.pack(pady=(15, 5))
        entry_name = tk.Entry(dialog, font=("TkDefaultFont", 11), width=35, bg="#FFFFFF")
        entry_name.pack(pady=5)
        entry_name.focus_set()

        def confirm():
            box_name = entry_name.get().strip()
            if not box_name:
                messagebox.showwarning("Missing Label", "Please declare a valid text label name.")
                return
            if active_facets:
                self.cardboxes[box_name] = {"query": query, "facets": active_facets}
            else:
                self.cardboxes[box_name] = query
            self.save_cardboxes_to_disk()
            self.cardbox_dropdown['values'] = list(self.cardboxes.keys())
            self.dropdown_var.set(box_name)
            dialog.destroy()
            messagebox.showinfo("Cardbox Stored", f"Collection '{box_name}' captured safely.")

        btn_confirm = tk.Button(dialog, text="Store Collection", bg=self.COLOR_TEAL, fg="#FFFFFF", font=("TkDefaultFont", 10, "bold"), relief="flat", padx=15, pady=4, command=confirm)
        btn_confirm.pack(pady=10)

    def on_cardbox_dropdown_select(self, event):
        """Loads a stored search configuration from the selected Cardbox."""
        selected_box = self.dropdown_var.get()
        saved = self.cardboxes.get(selected_box)
        if not saved:
            return

        if isinstance(saved, dict):
            self.search_val.set(saved.get("query", ""))
            desired = {(f, k) for f, k in saved.get("facets", [])}
            for key, var in self.facet_selections.items():
                var.set(key in desired)
        else:
            self.search_val.set(saved)
            for var in self.facet_selections.values():
                var.set(False)

        self.execute_search_pipeline(update_facets_ui=True)

    def delete_selected_cardbox(self):
        """Removes the currently selected Cardbox view from the registry."""
        selected_box = self.dropdown_var.get()
        if not selected_box:
            messagebox.showwarning("No Selection", "Please choose a Cardbox view from the dropdown menu first.")
            return
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to permanently erase the '{selected_box}' Cardbox layout link?")
        if confirm:
            del self.cardboxes[selected_box]
            self.save_cardboxes_to_disk()
            self.cardbox_dropdown['values'] = list(self.cardboxes.keys())
            self.dropdown_var.set("")
            self.search_val.set("")
            self.execute_search_pipeline(update_facets_ui=True)
            messagebox.showinfo("Cardbox Erased", f"'{selected_box}' has been cleared from your desk list.")

    def render_empty_welcome_splash(self, message="Search queries will show here."):
        """Displays a welcome screen when the result feed is empty."""
        for w in self.feed_scroll_frame.winfo_children():
            w.destroy()
        splash_box = ttk.Frame(self.feed_scroll_frame, padding=40)
        splash_box.pack(expand=True, fill=tk.BOTH, pady=60)
        lbl_h1 = tk.Label(splash_box, text="The Refcards-System", font=("TkDefaultFont", 20, "bold"), fg=self.COLOR_TEAL, bg=self.COLOR_BG)
        lbl_h1.pack(pady=(10, 2))
        lbl_msg = tk.Label(splash_box, text=message, font=("TkDefaultFont", 12, "italic"), fg=self.COLOR_INK, bg=self.COLOR_BG)
        lbl_msg.pack(pady=8)
        lbl_h3 = tk.Label(splash_box, text="Atomic Knowledge Engine Active.", font=("TkDefaultFont", 9, "italic"), fg="#7A7A7A", bg=self.COLOR_BG)
        lbl_h3.pack(pady=(5, 10))

    def generate_kwic_snippet(self, text, terms, window=60):
        """
        Generates a Keyword-In-Context (KWIC) snippet for search highlighting.

        :param text: The source text.
        :param terms: List of terms to highlight.
        :param window: Window size around match.
        :return: String snippet.
        """
        if not text or not terms:
            return text if len(text) <= 180 else text[:180] + "..."
        lower_text = text.lower()
        earliest_idx = -1
        matched_term_len = 0
        for t in terms:
            if not t: continue
            idx = lower_text.find(t)
            if idx != -1 and (earliest_idx == -1 or idx < earliest_idx):
                earliest_idx = idx
                matched_term_len = len(t)
        if earliest_idx == -1:
            return text if len(text) <= 180 else text[:180] + "..."
        start = max(0, earliest_idx - window)
        end = min(len(text), earliest_idx + matched_term_len + window)
        snippet = text[start:end]
        prefix = "... " if start > 0 else ""
        postfix = "..." if end < len(text) else ""
        return prefix + snippet + postfix

    def evaluate_boolean_expression(self, expression, record):
        """
        Parses and evaluates a boolean search query against a record.

        :param expression: Boolean query string.
        :param record: Dictionary record to test.
        :return: Boolean match result.
        """
        expression = expression.replace("(", " (").replace(")", ")")
        tokens = re.findall(r'"[^"]*"|[^\s"]+', expression)
        eval_string = ""
        for token in tokens:
            token_upper = token.upper()
            if token_upper in ("AND", "OR", "NOT", "(", ")"):
                eval_string += f" {token_upper.lower()} "
            else:
                clean_term = token.strip('"')
                if ":" in clean_term:
                    f_key, f_val = clean_term.split(":", 1)
                    f_val = f_val.strip('"').lower()
                    target_col = None
                    for h in self.csv_headers:
                        if f_key.lower() in h.lower():
                            target_col = h
                            break
                    match_found = target_col and f_val in str(record.get(target_col, "")).lower()
                else:
                    combined_dump = " ".join(str(val).lower() for val in record.values())
                    match_found = clean_term.lower() in combined_dump
                eval_string += f" {str(bool(match_found))} "
        if not eval_string.strip():
            return True
        try:
            return eval(eval_string, {"and": lambda a,b: a and b, "or": lambda a,b: a or b, "not": lambda a: not a, "true": True, "false": False})
        except Exception:
            return False

    def extract_highlight_terms(self, raw_query):
        """Parses a query string to return a set of unique search terms for highlighting."""
        cleaned = re.sub(r'\b(AND|OR|NOT)\b', ' ', raw_query, flags=re.IGNORECASE)
        cleaned = cleaned.replace("(", "").replace(")", "")
        terms = re.findall(r'"([^"]+)"|([^\s:]+)', cleaned)
        results = set()
        for t in terms:
            val = t[0] if t[0] else t[1]
            if val and ":" not in val:
                results.add(val.lower())
            elif val and ":" in val:
                v = val.split(":", 1)
                results.add(v[1].strip('"').lower())
        return results

    def execute_search_pipeline(self, update_facets_ui=False):
        """Runs the search-and-filter logic and refreshes the UI results."""
        raw_query = self.search_val.get().strip()
        terms_to_highlight = self.extract_highlight_terms(raw_query)

        active_facets_by_field = {}
        for (field, kw), var in self.facet_selections.items():
            if var.get():
                active_facets_by_field.setdefault(field, []).append(kw)

        matched_rows = []
        for row in self.all_data:
            text_match = True
            if raw_query:
                text_match = self.evaluate_boolean_expression(raw_query, row)
            facet_match = True
            for field, keywords in active_facets_by_field.items():
                field_content = str(row.get(field, "")).lower()
                if not any(kw in field_content for kw in keywords):
                    facet_match = False
                    break
            if text_match and facet_match:
                matched_rows.append(row)

        if update_facets_ui:
            self.rebuild_sidebar_facets_ui(matched_rows)

        self.active_data = matched_rows

        if raw_query or active_facets_by_field:
            self.counter_lbl.config(text=f"{len(self.active_data)} matching Refcards displayed")
        else:
            self.counter_lbl.config(text=f"{len(self.active_data)} Refcards displayed")

        self.render_result_cards(terms_to_highlight)

    def on_facet_checkbox_changed(self):
        """Handler for toggling sidebar facets."""
        if self._updating_facets_lock:
            return
        self.execute_search_pipeline(update_facets_ui=False)

    def rebuild_sidebar_facets_ui(self, baseline_rows):
        """Dynamically recreates the sidebar filter checkboxes based on result data."""
        if self._updating_facets_lock:
            return
        self._updating_facets_lock = True
        for w in self.sidebar_frame.winfo_children():
            w.destroy()

        lbl_title = tk.Label(self.sidebar_frame, text="FACETED FILTERS",
                            font=("TkDefaultFont", 10, "bold"), fg=self.COLOR_INK, bg=self.COLOR_BG)
        lbl_title.pack(anchor=tk.W, pady=(0, 2))
        btn_clear = tk.Button(self.sidebar_frame, text="Clear All Canvas Filters",
                              command=self.clear_all_facets_action, bg=self.COLOR_CARD_BG, font=("TkDefaultFont", 8), relief="groove")
        btn_clear.pack(fill=tk.X, pady=(0, 4))
        lbl_info = tk.Label(self.sidebar_frame, text="By Key Terms (Recent First):",
                           font=("TkDefaultFont", 9, "italic", "bold"), fg="#555555", bg=self.COLOR_BG)
        lbl_info.pack(anchor=tk.W, pady=(6, 10))

        stop_words = {
            'and', 'the', 'for', 'with', 'from', 'this', 'that', 'your', 'about', 'each', 'before',
            'after', 'over', 'under', 'into', 'upon', 'through', 'which', 'their', 'there', 'then',
            'took', 'them', 'they', 'have', 'has', 'had', 'been', 'being', 'were', 'was', 'are',
            'some', 'many', 'more', 'most', 'very', 'just', 'only', 'also', 'like', 'make', 'made',
            'take', 'took', 'give', 'given', 'find', 'found', 'know', 'known', 'see', 'seen', 'use',
            'used', 'using', 'new', 'old', 'good', 'great', 'small', 'large', 'first', 'last', 'next'
        }

        def parse_date(r):
            try:
                return datetime.strptime(r.get("DATETIME", ""), "%Y-%m-%d %H:%M:%S")
            except Exception:
                return datetime.min

        sorted_rows = sorted(baseline_rows, key=parse_date, reverse=True)
        target_fields = [h for h in self.csv_headers if h not in ["ID", "DATETIME"]]

        for field in target_fields:
            keyword_info = defaultdict(lambda: {'count': 0, 'latest_date': datetime.min})

            for row in sorted_rows:
                text_content = str(row.get(field, "")).strip()
                if not text_content:
                    continue
                clean_text = re.sub(r'[^\w\s-]', ' ', text_content.lower())
                clean_text = re.sub(r'\s+', ' ', clean_text).strip()
                tokens = clean_text.split()
                unique_tokens = {
                    w for w in tokens
                    if w not in stop_words and len(w) >= 4 and not w.isdigit()
                }
                row_date = parse_date(row)
                for w in unique_tokens:
                    keyword_info[w]['count'] += 1
                    if row_date > keyword_info[w]['latest_date']:
                        keyword_info[w]['latest_date'] = row_date

            if not keyword_info:
                continue

            sorted_keywords = sorted(
                keyword_info.items(),
                key=lambda x: (x[1]['latest_date'], x[1]['count']),
                reverse=True
            )
            sorted_keywords = [kw for kw, info in sorted_keywords][:20]

            lbl_field_header = tk.Label(self.sidebar_frame, text=f"{field}:",
                                        font=("TkDefaultFont", 9, "bold"), fg=self.COLOR_TEAL, bg=self.COLOR_BG)
            lbl_field_header.pack(anchor=tk.W, pady=(6, 2))

            is_expanded = self.expanded_facets.get(field, False)
            visible_limit = len(sorted_keywords) if is_expanded else 6

            for idx, kw in enumerate(sorted_keywords):
                facet_key = (field, kw)
                if facet_key not in self.facet_selections:
                    self.facet_selections[facet_key] = tk.BooleanVar(value=False)
                var = self.facet_selections[facet_key]
                if idx < visible_limit:
                    count = keyword_info[kw]['count']
                    cb = tk.Checkbutton(
                        self.sidebar_frame,
                        text=f"{kw.capitalize()} ({count})",
                        variable=var,
                        bg=self.COLOR_BG,
                        fg=self.COLOR_INK,
                        activebackground=self.COLOR_BG,
                        command=self.on_facet_checkbox_changed
                    )
                    cb.pack(anchor=tk.W, padx=5)

            if len(sorted_keywords) > 6:
                link_text = "Show Less" if is_expanded else f"+ Show More ({len(sorted_keywords) - 6})"
                btn_toggle = tk.Button(
                    self.sidebar_frame,
                    text=link_text,
                    font=("TkDefaultFont", 8, "underline"),
                    fg=self.COLOR_TEAL,
                    bg=self.COLOR_BG,
                    activeforeground=self.COLOR_TEAL,
                    activebackground=self.COLOR_BG,
                    relief="flat",
                    bd=0,
                    cursor="hand2",
                    command=lambda f=field: self.toggle_facet_expansion(f)
                )
                btn_toggle.pack(anchor=tk.W, padx=5, pady=(1, 4))

            sep = ttk.Separator(self.sidebar_frame, orient='horizontal')
            sep.pack(fill=tk.X, pady=4)

        self._updating_facets_lock = False

    def toggle_facet_expansion(self, column_key):
        """Toggles the visibility of expanded facet lists in the sidebar."""
        self.expanded_facets[column_key] = not self.expanded_facets.get(column_key, False)
        raw_query = self.search_val.get().strip()
        matched_rows = [row for row in self.all_data if not raw_query or self.evaluate_boolean_expression(raw_query, row)]
        self.rebuild_sidebar_facets_ui(matched_rows)

    def clear_all_facets_action(self):
        """Resets all facet selection filters."""
        for var in self.facet_selections.values():
            var.set(False)
        self.execute_search_pipeline(update_facets_ui=True)

    def clear_entire_search_action(self):
        """Resets the search UI to an empty state."""
        self.search_val.set("")
        self.dropdown_var.set("")
        for var in self.facet_selections.values():
            var.set(False)
        self.counter_lbl.config(text="")
        self.render_empty_welcome_splash(message="Cleared Search Desk. Search queries will show here.")

    def show_all_records_action(self):
        """Resets filters and reloads all records."""
        self.search_val.set("")
        self.dropdown_var.set("")
        for var in self.facet_selections.values():
            var.set(False)
        self.reload_data_from_csv()
        self.execute_search_pipeline(update_facets_ui=True)

    def render_result_cards(self, highlight_terms):
        """Renders the main list of Refcards as interactive result cards."""
        for w in self.feed_scroll_frame.winfo_children():
            w.destroy()
        if not self.active_data:
            lbl = ttk.Label(self.feed_scroll_frame, text="\nNo Refcards matched your current parameters.", font=("TkDefaultFont", 11, "italic"))
            lbl.pack(pady=20, anchor=tk.CENTER)
            return
        for row in self.active_data:
            card = ttk.Frame(self.feed_scroll_frame, style="Card.TFrame", padding=12, cursor="hand2")
            card.pack(fill=tk.X, expand=True, pady=6, padx=5)
            header_text = f"[{row.get('ID', '')}] {row.get('EXPERIMENT', 'Untitled Experiment')}"
            lbl_h = tk.Label(card, text=header_text, font=("TkDefaultFont", 12, "bold"), fg=self.COLOR_TEAL, bg=self.COLOR_CARD_BG, cursor="hand2")
            lbl_h.pack(anchor=tk.W, pady=(0, 2))
            meta_text = f"Logged: {row.get('DATETIME', '')}"
            lbl_m = tk.Label(card, text=meta_text, font=("TkDefaultFont", 8, "italic"), fg="#666666", bg=self.COLOR_CARD_BG, cursor="hand2")
            lbl_m.pack(anchor=tk.W, pady=(0, 6))
            snippet_elements = []
            for field in ["PURPOSE", "PROCEDURE", "NOTES"]:
                val = str(row.get(field, "")).strip()
                if val:
                    kwic_snippet = self.generate_kwic_snippet(val, highlight_terms)
                    snippet_elements.append(f"{field}: {kwic_snippet}")
            combined_display = "\n".join(snippet_elements)
            t_box = tk.Text(card, wrap=tk.WORD, font=("TkDefaultFont", 10), bg=self.COLOR_BG, relief="flat", height=4, highlightthickness=0, cursor="hand2")
            t_box.pack(fill=tk.X, expand=True, pady=4, padx=5)
            t_box.insert(tk.END, combined_display)
            if highlight_terms:
                self.insert_highlighted_text(t_box, combined_display, highlight_terms)
            t_box.config(state=tk.DISABLED)
            for target_widget in (card, lbl_h, lbl_m, t_box):
                target_widget.bind("<Button-1>", lambda event, r=row: self.open_refcard_editor(r))

    def insert_highlighted_text(self, text_widget, text, terms):
        """Highlights matching terms within the Text result widget."""
        text_widget.tag_config("match", background="#D1E7DD", foreground=self.COLOR_INK, font=("TkDefaultFont", 10, "bold"))
        lower_text = text.lower()
        for t in terms:
            if not t: continue
            start_pos = 0
            while True:
                idx = lower_text.find(t, start_pos)
                if idx == -1: break
                start_idx = f"1.0+ {idx} chars"
                end_idx = f"1.0+ {idx + len(t)} chars"
                text_widget.tag_add("match", start_idx, end_idx)
                start_pos = idx + len(t)

    def open_refcard_editor(self, record=None):
        """
        Opens a modal window for creating or editing a Refcard entry.

        :param record: Dictionary of existing record data, or None for new record.
        """
        editor = tk.Toplevel(self)
        editor.geometry("650x680")
        editor.configure(bg=self.COLOR_BG)
        is_new = record is None
        editor.title("New Refcard Creation Form" if is_new else "Modify Refcard Entry Form")
        editor.transient(self)
        editor.grab_set()

        # DATETIME Row
        lbl_dt = tk.Label(editor, text="DATETIME:", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_BG)
        lbl_dt.pack(anchor=tk.W, padx=15, pady=(10, 2))
        ent_dt = tk.Entry(editor, font=("TkDefaultFont", 10), width=60)
        ent_dt.pack(fill=tk.X, padx=15, pady=(0, 5))
        if is_new:
            ent_dt.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            ent_dt.insert(0, record.get("DATETIME", ""))

        # EXPERIMENT Row
        lbl_exp = tk.Label(editor, text="EXPERIMENT (Number and Title):", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_BG)
        lbl_exp.pack(anchor=tk.W, padx=15, pady=(10, 2))
        ent_exp = tk.Entry(editor, font=("TkDefaultFont", 10), width=60)
        ent_exp.pack(fill=tk.X, padx=15, pady=(0, 5))
        if not is_new:
            ent_exp.insert(0, record.get("EXPERIMENT", ""))

        # PURPOSE Frame
        lbl_purp = tk.Label(editor, text="PURPOSE:", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_BG)
        lbl_purp.pack(anchor=tk.W, padx=15, pady=(10, 2))
        txt_purp = tk.Text(editor, font=("TkDefaultFont", 10), wrap=tk.WORD, height=3)
        txt_purp.pack(fill=tk.X, padx=15, pady=(0, 5))
        if not is_new:
            txt_purp.insert(tk.END, record.get("PURPOSE", ""))

        # PROCEDURE Frame
        lbl_proc = tk.Label(editor, text="PROCEDURE (Succinct Description):", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_BG)
        lbl_proc.pack(anchor=tk.W, padx=15, pady=(10, 2))
        txt_proc = tk.Text(editor, font=("TkDefaultFont", 10), wrap=tk.WORD, height=4)
        txt_proc.pack(fill=tk.X, padx=15, pady=(0, 5))
        if not is_new:
            txt_proc.insert(tk.END, record.get("PROCEDURE", ""))

        # NOTES Frame
        lbl_notes = tk.Label(editor, text="NOTES & REFLEXIVE THOUGHTS:", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_BG)
        lbl_notes.pack(anchor=tk.W, padx=15, pady=(10, 2))
        txt_notes = tk.Text(editor, font=("TkDefaultFont", 10), wrap=tk.WORD, height=6)
        txt_notes.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        if not is_new:
            txt_notes.insert(tk.END, record.get("NOTES", ""))

        # BUTTON CONTROLS ACTION HOLDER
        btn_container = ttk.Frame(editor, padding=(15, 0, 15, 15))
        btn_container.pack(fill=tk.X, side=tk.BOTTOM)

        def save_action():
            exp_val = ent_exp.get().strip()
            if not exp_val:
                messagebox.showwarning("Missing Parameter", "Each card entry must track an EXPERIMENT identity.")
                return
            out_record = {
                "ID": record["ID"] if not is_new else str(uuid.uuid4())[:8],
                "DATETIME": ent_dt.get().strip(),
                "EXPERIMENT": exp_val,
                "PURPOSE": txt_purp.get("1.0", tk.END).strip(),
                "PROCEDURE": txt_proc.get("1.0", tk.END).strip(),
                "NOTES": txt_notes.get("1.0", tk.END).strip()
            }
            self.save_record_to_csv(out_record, is_new=is_new)
            editor.destroy()

        def delete_action():
            if is_new:
                editor.destroy()
                return
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to permanently delete Refcard [{record['ID']}] from the system index?")
            if confirm:
                self.remove_record_from_csv(record["ID"])
                editor.destroy()
                messagebox.showinfo("Card Purged", f"Refcard [{record['ID']}] successfully dropped from database.")

        btn_save = tk.Button(btn_container, text="Commit and Save Record", font=("TkDefaultFont", 10, "bold"), bg=self.COLOR_TEAL, fg="#FFFFFF", relief="flat", command=save_action, pady=6, cursor="hand2")
        btn_save.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        if not is_new:
            btn_delete = tk.Button(btn_container, text="Delete This Card", font=("TkDefaultFont", 10), bg=self.COLOR_CARD_BG, fg=self.COLOR_CRIMSON, activebackground=self.COLOR_CRIMSON, activeforeground="#FFFFFF", relief="groove", command=delete_action, pady=5, cursor="hand2")
            btn_delete.pack(side=tk.RIGHT, padx=(5, 0))
        btn_cancel = tk.Button(btn_container, text="Cancel", command=editor.destroy, bg=self.COLOR_CARD_BG, relief="groove")
        btn_cancel.pack(side=tk.RIGHT, padx=(5, 0))

    def display_syntax_popover(self):
        """Displays help dialog regarding search syntax operators."""
        help_msg = (
            "Knowledge Field Search Operator Rules: \n\n"
            "Logical Operators: Link keys with AND, OR, NOT gates.\n"
            " -> (noise OR randomness) NOT structural\n\n"
            "Scoped Modifiers: Target parameters precisely using column descriptors.\n"
            " -> EXPERIMENT: 001 AND NOTES: randomness\n"
            " -> PURPOSE: Aesthetics NOT NOTES: digital"
        )
        messagebox.showinfo("Search View System Help", help_msg)


if __name__ == "__main__":
    app = RefcardsSystemEngine()
    app.mainloop()
