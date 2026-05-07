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

# (Clear statement of purpose)

# PROCEDURE:  (succinct description of procedure

# SIGNATURE:

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

- - - - - - - - -

### [BACK TO DOCUMENTATION / METHODS](https://github.com/antiface/Documentation/tree/master/METHODS)
## [BACK TO INDEX OF REPOSITORIES](https://github.com/antiface/Index)

[A.G. (c) 2026. ![A.G. (c) 2026. All Rights Reserved](https://historiotheque.files.wordpress.com/2016/11/ag_signature_official_2015_50px_cropped.jpg) All Rights Reserved.](http://alexgagnon.com)
