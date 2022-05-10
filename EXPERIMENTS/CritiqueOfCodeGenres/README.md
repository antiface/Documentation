### CRITIQUE OF CODE GENRES
* I began writing about this recently, the idea of studying computer programs, code, applications, etc., in terms of "genres";
* The idea is to treat code as what it actually is: text;
* Since code = text, then it is possible to treat source code, applications, etc., in terms of "code genres", if you will (a.k.a. "application genres");
* We will begin this experiment by looking at a bundle of Github repositories of apps written in Python - mostly in the Django framework - that are of the "accounting app genre";
* We will also be developing a method for going over repositories like these, going over all of the files and folders, essentially going over all of the contents of the repos to try to make sense of the given app, the app structure and so forth;
* For now, we will begin with a list of the Python/Django accounting apps that have been selected for this exercise, and then we will begin by looking at the various "models.py" programs within each pertinent section of the code base;
* Choosing to look at all the "models.py" scripts is meant to be in line with a practice of "introspection", if you will, more in a philosophical sense than in a programming sense;
* That is, what we are essentially doing is a form of "code review", but it is a "literate" and "critical" code review;
* First of all, by looking at code genres, we are presuming that computer applications have "genres" as works of literature or painting or music do;
* Secondly, we want to "inspect" the various code bases to see how they are structured;
* In the end, we are treating "computer code" as a form of "literature" (text) and so it will also have its own "discursive structures";
* That is, the application itself is part of a "discourse", with its own universe of discourse/domain of discourse, discursive structures, and so forth;
* Without further ado... the list of repositories we have chosen:

### ACCOUNTING APP GENRE: MOSTLY PYTHON/DJANGO
* [masnun/django-accounts-app: A sample app that manages a few accounts and their transactions](https://github.com/masnun/django-accounts-app)
* [keeran6/check-logist: Django-admin-based system for logistics company accounting.](https://github.com/keeran6/check-logist)
* [hereischen/django-luoji-accounts: A general account app for projects.](https://github.com/hereischen/django-luoji-accounts)
* [kaedroho/Django-Accounts: Accounts app for Django](https://github.com/kaedroho/Django-Accounts)
* [KristianOellegaard/snapsekassen: An advanced Schnapps account keeper, written in Django.](https://github.com/KristianOellegaard/snapsekassen)
* [arvis/tripaccounting: Basic trip accounting web application, created with Django to compare developent speed with node.js frameworks on CRUD apps](https://github.com/arvis/tripaccounting)
* [Baltrunas/django-accounts2: Accounts with bucket for any types of models](https://github.com/Baltrunas/django-accounts2)
* [bitmazk/django-account-keeping: A reusable Django app for keeping track of transactions in your bank accounts.](https://github.com/bitmazk/django-account-keeping)
* [phillipberndt/coffeelist: Django application for account management for a coffee machine and automated processing of scanned tally lists](https://github.com/phillipberndt/coffeelist)
* [pbhopalka/AccountingSoftware: A online software built using Python Django](https://github.com/pbhopalka/AccountingSoftware)
* [Sinba/AccountingSite: Acoounting site on Django. Course work at the university](https://github.com/Sinba/AccountingSite)
* [altaurog/django-caspy: Django/Angular double-entry personal accounting](https://github.com/altaurog/django-caspy)
* [conicio/reckon-accounting: Generic double-entry accounting for Django](https://github.com/conicio/reckon-accounting)
* [kunkku/django-financial-accounting: Double-entry bookkeeping powered by Django admin](https://github.com/kunkku/django-financial-accounting)
* [ivarne/django_regnskap: A simple attemt to make an accounting application for django. Ugly mix of Norwegian and English in variable names and comments. You can freely use this code for whatever purpuse you'd like, but I take no responsibility.](https://github.com/ivarne/django_regnskap)
* [nimnull/expensor: Small django accounting webapp for own needs](https://github.com/nimnull/expensor)
* [enikesha/pacioli: Advanced accounting software for Bitcoin](https://github.com/enikesha/pacioli)
* [pipermerriam/ethereum-accounting: Basic accounting tools for ethereum contracts](https://github.com/pipermerriam/ethereum-accounting)
* [seldon/django-simple-accounting: A simple accounting applications for Django](https://github.com/seldon/django-simple-accounting)
* [prikhi/AcornAccounting: A Django-based Accounting System for Egalitarian Communities](https://github.com/prikhi/AcornAccounting)
* [cypreess/django-plans: Django application for managing account plans and quotas](https://github.com/cypreess/django-plans)
* [xtranophilist/awecounting: Awesome Accounting](https://github.com/xtranophilist/awecounting)
* [frasertweedale/ledgertools: Utilities for the Ledger accounting system.](https://github.com/frasertweedale/ledgertools)
* [mafm/ledger.py: Command-line, double-entry accounting in python. Excel and text output.](https://github.com/mafm/ledger.py)
* [pcapriotti/pledger: Command line accounting tool and python library](https://github.com/pcapriotti/pledger)
* [hasgeek/pennywise: Web-based double-entry accounting](https://github.com/hasgeek/pennywise)
* [cperler/accounting: Take control of your finances.](https://github.com/cperler/accounting)
* [ajpocus/djac: A double entry accounting app for Django.](https://github.com/ajpocus/djac)

### Critical, Discursive Code Inspection/Review
* Now we will take the same repositories listed above and "dig" into them a little deeper;
* We will begin by inspecting the various "models.py" pieces of code:

### A DEEPER LOOK INSIDE (REFLECTION, INTROSPECTION, CRITIQUE OF CODE GENRE)
* [django-accounts-app/models.py at master · masnun/django-accounts-app](https://github.com/masnun/django-accounts-app/blob/master/accounts/models.py)
* [check-logist/models.py at master · keeran6/check-logist](https://github.com/keeran6/check-logist/blob/master/persons/models.py)
* [django-luoji-accounts/models.py at master · hereischen/django-luoji-accounts](https://github.com/hereischen/django-luoji-accounts/blob/master/accounts/models.py)
* [Django-Accounts/models.py at master · kaedroho/Django-Accounts](https://github.com/kaedroho/Django-Accounts/blob/master/models.py)
* [snapsekassen/models.py at master · KristianOellegaard/snapsekassen](https://github.com/KristianOellegaard/snapsekassen/blob/master/schnappsaccount/models.py)
* [tripaccounting/models.py at master · arvis/tripaccounting](https://github.com/arvis/tripaccounting/blob/master/route/models.py)
* [django-accounts2/models.py at master · Baltrunas/django-accounts2](https://github.com/Baltrunas/django-accounts2/blob/master/models.py)
* [django-account-keeping/models.py at master · bitmazk/django-account-keeping](https://github.com/bitmazk/django-account-keeping/blob/master/account_keeping/models.py)
* [coffeelist/models.py at master · phillipberndt/coffeelist](https://github.com/phillipberndt/coffeelist/blob/master/coffeelist/coffeelist/coffee/models.py)
* [AccountingSoftware/models.py at master · pbhopalka/AccountingSoftware](https://github.com/pbhopalka/AccountingSoftware/blob/master/accounting/models.py)
* [AccountingSite/models.py at master · Sinba/AccountingSite](https://github.com/Sinba/AccountingSite/blob/master/accounts/models.py)
* [django-caspy/models.py at master · altaurog/django-caspy](https://github.com/altaurog/django-caspy/blob/master/caspy/models.py)
* [reckon-accounting/models.py at master · conicio/reckon-accounting](https://github.com/conicio/reckon-accounting/blob/master/accounting/models.py)
* [django-financial-accounting/models.py at master · kunkku/django-financial-accounting](https://github.com/kunkku/django-financial-accounting/blob/master/accounting/models.py)
* [django_regnskap/models.py at master · ivarne/django_regnskap](https://github.com/ivarne/django_regnskap/blob/master/regnskap/models.py)
* [expensor/models.py at master · nimnull/expensor](https://github.com/nimnull/expensor/blob/master/core/models.py)
* [pacioli/models.py at master · enikesha/pacioli](https://github.com/enikesha/pacioli/blob/master/pacioli/models.py)
* [ethereum-accounting/test_deposit.py at master · pipermerriam/ethereum-accounting](https://github.com/pipermerriam/ethereum-accounting/blob/master/tests/accounting/test_deposit.py)
* [django-simple-accounting/models.py at master · seldon/django-simple-accounting](https://github.com/seldon/django-simple-accounting/blob/master/simple_accounting/models.py)
* [AcornAccounting/models.py at develop · prikhi/AcornAccounting](https://github.com/prikhi/AcornAccounting/blob/develop/acornaccounting/accounts/models.py)
* [django-plans/models.py at master · cypreess/django-plans](https://github.com/cypreess/django-plans/blob/master/plans/models.py)
* [awecounting/models.py at master · xtranophilist/awecounting](https://github.com/xtranophilist/awecounting/blob/master/ledger/models.py)
* [ledgertools/rule.py at master · frasertweedale/ledgertools](https://github.com/frasertweedale/ledgertools/blob/master/ltlib/rule.py)
* [ledger.py/ledger.py at master · mafm/ledger.py](https://github.com/mafm/ledger.py/blob/master/ledger.py)
* [pledger/account.py at master · pcapriotti/pledger](https://github.com/pcapriotti/pledger/blob/master/pledger/account.py)
* [pennywise/ledgers.py at master · hasgeek/pennywise](https://github.com/hasgeek/pennywise/blob/master/pennywise/ledgers.py)
* [accounting/models.py at master · cperler/accounting](https://github.com/cperler/accounting/blob/master/accounting/models.py)
* [djac/models.py at master · ajpocus/djac](https://github.com/ajpocus/djac/blob/master/accounts/models.py)

### PYTHONIC REFLECTIONS
* Let us take a look at the first Python accounting app in our list: [masnun/django-accounts-app: A sample app that manages a few accounts and their transactions](https://github.com/masnun/django-accounts-app);
* As stated above, we will first look at a file called "models.py": [django-accounts-app/models.py at master · masnun/django-accounts-app](https://github.com/masnun/django-accounts-app/blob/master/accounts/models.py);
* Within "models.py", we want to look at these two lines, L7 and L16, where Classes are defined:
  * [accounts/models.py#L7](https://github.com/masnun/django-accounts-app/blob/master/accounts/models.py#L7) (i.e. "class Account(models.Model)");
  * [accounts/models.py#L16](https://github.com/masnun/django-accounts-app/blob/master/accounts/models.py#L16) (i.e. "class Transaction(models.Model)");
* Namely, we have two classes, one called "Account" and one called "Transaction";
* This allows us to get a feel for what the "objects", if you will, are for this particular software project;
