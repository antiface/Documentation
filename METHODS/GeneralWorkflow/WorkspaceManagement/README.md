## WORKSPACE MANAGEMENT
* Temporary information:
  * The goal is to always be able to re-orient oneself after a *Work-Session*;
  * You leave *Breadcrumbs* so you can re-orient yourself each new *Workday*;
  * You need to master the art of *configuring a workspace*;
  * The *Workspace* is virtual and 4-dimensional, i.e. it is a 3-dimensional surface changing over time;
  * One needs to know the previous configuration and be able to reinstate that configuration;
  * You could call it the *Restoration of Previous Workstate*;

*06:00 2024-01-09*

* The most important thing in the kind of work of interdisciplinary art-research that I do is *not losing operational continuity*;
* This means that I always need to know *where I left off*, during my previous *work-session*;
* That's how one retains and maintains operational continuity, by knowing the previous *work-state* and *continuing in that vein*;
* This is the fundamental aspect of *Workspace Management*, i.e. the management of the virtual workspace so that you never lose continuity;
* When you go to bed at night, you leave the workspace behind and in the morning when you go back to work, you need to know *where you left off*;
* So you have to have some discipline in your work practices, you need to leave *a trail of breadcrumbs* that you can follow to come back to the fundamental *Workspace* you were in during your previous *work-session*;
* This means backing up all your data, all your current files, your logs and so forth;
* It also means documenting all your practices and making them accessible online;
* Everything needs to be accessible online so you can *work remotely*, never knowing if you are going to be at home or not when you need to keep working;
* All projects are saved and can be restored at any time;
* *In the workspace, in general, I always use timestamps and when I "leave off", I write what the last thing was that I was doing*;
* *In this way, I never lose track of what I'm doing, and I can reconstruct temporal orders of things based on my multiple log-files*;
* I basically only need to remember what the __*LAST THING*__ was that I was working on; the rest can be reconstructed from the timestamped materials;

- - - - - - - - -

*00:32:17 2026-05-07*

* I have been working on the actual __WORKSPACE__ and the __delta-workspace theory__ that goes with it;
* The __delta-workspace theory__ has mainly to do with the __variable geometry of the workspace__ and the workspace itself as *"the 3D surface of the workspace as it changes over time"*;
* I will get into this more soon. I just wanted to come back to this after a 2-year hiatus;
* I have been hard at work logging and documenting everything, something which I hadn't done very much of since last September, 2025;
* I published what I call an __"antilog"__ online on a blogging platform, __*"documenting the documentation*__" if you will, as part of what i now call the __*nonlinear practices and methodologies of hyperreflexive design*__, which I sometimes simplify as just *Reflexive Design* or *Non-Linear Practice* (see: [ANTILOG_06May26a](https://antilog.blogspot.com/2026/05/antilog06may26a.html);
* As I said, I will come back to this sortly and explain how it pertains to __WORKSPACE MANAGEMENT__ and my __*ambient experimental design workflow management methodology*__ or just *ALX* or else the *"delta-workspace model"* as I mentioned above (sorry, also as the concept in *Historiomics* of __historiotope/historiotopia__).
* Here is a copy of the instance of what I call __LABNOTES__, using a Python script I wrote 10 years ago called __*documentary_method.py*__, which basically produces the .txt file with the timestamp as filename;
* This type of script, in any case, will prove useful I think for this *WORKSPACE MANAGEMENT* GitHub repository;

![documentary_method](https://historiotheque.wordpress.com/wp-content/uploads/2026/05/202605062228.png)

* For future reference and for documentation purposes, here is the Python script I mentioned above, to generate *LabNotes* for my design experiments;
* It's pretty rudimentary and crude, but it does the job; I will likely be rewriting it completely, improving it, and turning it into an actual app; I've made a few attempts at this in the past, but need to update it, I think, with my current knowledge of and expertise in Python;

```python
# DATETIME: (date at top)

# EXPERIMENT: (number and title clearly stated)

# STATEMENT OF PURPOSE: (Clear statement of purpose)

# PROCEDURE:  (succinct description of procedure

# NOTES: (notes on all of the above and thoughts on the documentation process itself, reflexively)

import os
import time
 
os.chdir(FILEPATH) # Repository location for Labnotes.
 
def writeNote(x):
	with open(x, 'w') as outfile:
		outfile.write('Time: '+time.asctime())
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Experiment: '+input('Experiment: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Statement of Purpose: '+input('Statement of Purpose: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Procedure: '+input('Procedure: '))
		outfile.write('\n')
		outfile.write('\n')
		outfile.write('Notes: '+input('Notes: '))
		
def note():
	t = time.strftime('%Y%m%d%H%M')
	writeNote(t+'.txt')
```

- - - - - - -

06:28 2026-05-07


2026-05-06 21:55:19

- ALL THE PROJECTS ARE THE SAME ANYWAY;
- I JUST WAS OSCILLATING FOR ONE OF MY "15-MINUTE WORKDAYS" or "WORK SESSIONS" FROM TWO SEPARATE GEMINI TABS, ONE TAB FOR SENDING AN EMAIL TO MYSELF, BUT I WORKED ON THE TWO GEMINI TABS IN CONJUNCTION WITH A DOCUMENT I WAS CREATING OF THE CHAT I HAD JUST HAD WITH THE AI;
- THEN I WAS ALSO TRYING TO FIND A REFERENCE IN MY ARCHIVES OF THE CONCEPT OF "DELTA-WORKSPACE" AND "HISTORIOTOPIA" ORIGINALLY FROM A GITHUB REPOSITORY README.MD FILE, BUT WHICH I WAS SEARCHING TRYING TO FIND IN ANOTHER INSTANCE WHERE I HAD POSTED THE SAME CONTENT BUT IN A MEDIUM ARTICLE;
- I KEEP SWITCHING FROM THING TO THING, "TAB-TO-TAB", "TAB-TO-EDITOR", IT'S THE TRANSLATIONS AND TRANSITIONS FROM ONE TO THE OTHER;
- I WAS ALSO IN THE PROCESS OF PLANNING TO SEND AN EMAIL TO MYSELF WITH COPIES OF DOCUMENTS I HAD BEEN WORKING ON ONE OF MY COMPUTERS, THE UBUNTU MACHINE;
- THEN I'M ALREADY PLANNING RETRIEVING THE DOCUMENTS IN MY EMAIL ON MY WINDOWS LAPTOP, AFTER WHICH I WAS GOING TO PRINT OUT A DOZEN PAGES ON THAT COMPUTER;
- THEN I WAS PLANNING ON GOING TO READ THE DOCUMENTS AT THE KITCHEN TABLE;
- EXCEPT I'M FOLLOWING A RANDOM, NONLINEAR TRAJECTORY/PATH THROUGH THE WORKSPACE;
- I GO FROM WORKSPACE TO WORKSPACE, FROM DEVICE TO DEVICE, MEDIA TO MEDIA, ALWAYS IN "TRANSITION / INTERVAL / CONTACT";
- THERE WAS MORE TO IT BUT THAT'S IT FOR NOW, THIS HAS BEEN A DATA LOG, A SNAPSHOT OF THE WORKSPACE AS IT WAS IN THE PREVIOUS HOUR OR SO;
- TRANSITION / INTERVAL / CONTACT;
- "CONSCIENCE / VALUE / MOTIVE";

May 07, 2026 / 05h30

- Then early this morning, at one point I was reading and writing in bed, unable to fall asleep. I ended up going out for a smoke and had a coffee. I had a friendly encounter with a skunk.
- I spent time planning the first part of my day. Before that, I looked and leafed through my personal library and took out a half-dozen nooks I need to resd or reread and put them on the kitchen table. I plan to go through them today and read and reread them over coming days.
- References to specific works I have studied previously pop up in my mind at random times over the course of the day. I am more and more in the default mode, wandering like a vagabond,
- Before all of this, I was working at one of my two computer stations doing deep research and taking notes. I also wrote logs in one of my GitHub repositories on WORKSPACEMANAGEMENT. I wrote about it above, going from "tab-to-tab", "app-to-app" transitions, continually, etc.
- I reckon people will think I'm too systematic in my appriach. Systematicity seems to scare people, even those who make a living researching and/or teaching complexity and writing books on the subject. No one wants to LIVE in complexity.
- Complexity of experience can be very taxing, is a burden, it has many costs. People who specialize in doing hours of DEEP WORK every day work hard at building up complex structures in their minds, but behaviorally they are quite simple: they stand at a standing desk for 3-4 hours at a time or less. They do not LIVE complexity (they actually try to avoid it, I would say.
- Peculiarities of my mental condition make sustaining any level of concentration and attention nearly impossible. That's partly why I mosy my way around the workspace, wandering semi-aimlessly.
- The thing with trying to maximize compkexity in thought - inching towards that proverbial "ceiling of abstraction" (and systematic analysis) - is that in any given hour more or less, or every 15 minutes or less, the complex, multifaceted and multi-layered model you are building will suddenly collapse right in front of your eyes like a house of cards or a castle made of sand (and there is no remedy... except accepting one's date and quickly going back to work.
- Whiie I was having a coffee and cigarette on the balcony earlier (which is one of the 5 work states or "substations", if you will), I took notes and made a field recording of the ambient sound with the early birds.
- Yesterday was very oroductive, as I achieved a significant boost in efficiency across the "global workspace". As I said, I operate with 5 unique locations in The Historiotheque where I can do my work.
- Like I do with many domains and disciplines, I work across media, "intermedially", moving from "medium-to-medium", "device-to-device", etc. This "complexities work across the workspace, where a kind of 3D or 4D surface is oscillating, is changing shape and configuration over time.
- This is partly how I build up complexity in the workspace, via the implementation of randomized, dynamic task assignment algorithms (see: Ref. THE NOISE IN ]THE WORKSPACE PROJECT PROGRESS REPORT](https://medium.com/design-science/the-noise-in-the-workspace-project-progress-report-6773257fff9a). The complexity build up, then comes tumbling down. I call it "BABEL UP/BABEL DOWN", like in the Biblical story (see:  Ref. [THE TOWER OF INCOMPLETENESS AND INCOMPREHESION](https://medium.com/the-painters-almanach/the-tower-of-incompleteness-and-incomprehension-bc804a449845).
- It is contest against time and space and is largely an effect of combinations of movememts or "switches", if you will, from station-to-sration, different orderings between tasks, sequences/sequencing. Call it combinatorial complexity of rapidly cycling, discrete work sessions.
- Constraints are numerous, are aplenty. But complete and total collapse of the previously growing models and schemas is just around the corner. Call them "interruptions in the workflow"  or "discontinuities". There's no escaping it. Life means death. Every process that is spawned will eventually be "killed", as death or the ultimate end-state is already implied in its very definition.
- Do not become despondent and worry! This is the natural order of things. To be continued...

- - - - - - - - -

### [BACK TO DOCUMENTATION / METHODS](https://github.com/antiface/Documentation/tree/master/METHODS)
## [BACK TO INDEX OF REPOSITORIES](https://github.com/antiface/Index)

[A.G. (c) 2026. ![A.G. (c) 2026. All Rights Reserved](https://historiotheque.files.wordpress.com/2016/11/ag_signature_official_2015_50px_cropped.jpg) All Rights Reserved.](http://alexgagnon.com)
