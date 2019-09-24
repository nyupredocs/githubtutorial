# Git and GitHub tutorial

This is the repository for the Git and GitHub scalable collaborative workflow and methods tutorial prepared and presented by [Richard Evans](https://sites.google.com/site/rickecon/) (University of Chicago) for the NYU predoctoral economics training program hosted at New York University Stern School of Business, September 20-22, 2019 and cosponsored by [Schmidt Futures](https://schmidtfutures.com). This tutorial focuses on how to use Git and GitHub an a scalable collaborative workflow and as a medium for open source, transparent, and replicable research.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nyupredocs/githubtutorial/master)

This `README.md` serves as a syllabus, outline, and reference for the training. This document has ? sections.

1. [Schedule](#1-schedule)
2. [Git and GitHub Setup](#2-git-and-github-setup)
3. [Instructions for installing the Anaconda distribution of Python](#3-instructions-for-installing-the-anaconda-distribution-of-python)
4. [Jupyter Notebooks](#4-jupyter-notebooks)
5. [Text editor suggestions](#5-text-editor-suggestions)
6. [PEP 8, docstring commenting, and module structure](#6-pep-8-docstring-commenting-and-module-structure)
7. [References and Resources](#7-references-and-resources)


## 1. Schedule


### Friday, September 20

| Time | Topic | Materials |
|:----:|:----- |:--------- |
9:00a-12:00p | Git, GitHub, Python setup | [Day 1 Slides](https://github.com/nyupredocs/githubtutorial/blob/master/Slides/GitGitHub_d1.pdf) |
|            | Openness and collaboration in Econ |  |
|            | Git and GitHub basics              |  |
12:00-1:00p  | Lunch |  |
1:00-5:00p   | Evaluating GitHub repositories | [Project 1](https://github.com/nyupredocs/githubtutorial/blob/master/Projects/Project1.md) |


### Saturday, September 21

| Time | Topic | Materials |
|:----:|:----- |:--------- |
9:00a-12:00p | git merge and merge conflicts | [Day 2 Slides](https://github.com/nyupredocs/githubtutorial/blob/master/Slides/GitGitHub_d2.pdf) |
|            | Data best practices |  |
12:00-1:00p  | Lunch |  |
1:00-5:00p   | Collaborative economic modeling project | [Project 2](https://github.com/nyupredocs/githubtutorial/blob/master/Projects/Project2/OG2per.pdf) |
|            |  | Exercises 1, 2, 3, 4 |


### Sunday, September 22

| Time | Topic | Materials |
|:----:|:----- |:--------- |
9:00a-12:00p | Code cleanliness, documentation | [Day 3 Slides](https://github.com/nyupredocs/githubtutorial/blob/master/Slides/GitGitHub_d3.pdf) |
|            | Tools for extending open models |  |
|            | [ParamTools](https://github.com/PSLmodels/ParamTools) and [compute.studio](https://compute.studio) |  |
12:00-1:00p  | Lunch |  |
1:00-3:00p   | PEP8, Docstrings, and [Sphinx](http://www.sphinx-doc.org/en/master/) | [Project 3](https://github.com/nyupredocs/githubtutorial/blob/master/Projects/Project3.md) |


## 2. Git and GitHub Setup

### 2.1. Install Git

`Git` is powerful version control software that must be installed on your local computer. You can check if `Git` is already installed on your machine by typing the following command in your terminal window
```
git --version
```
You can install or `Git` by following the appropriate operating system instructions on the [`Git` download page](https://git-scm.com/downloads).


### 2.2. Sign up for a GitHub account

You should sign up for a GitHub account by going to [https://github.com/join](https://github.com/join). Choose a `username` that is not too long but that represents you. Be careful on what username you choose. That will be your GitHub handle and will be the main name by which you will be recognized in your interactions on GitHub. And the goal is for you to have many productive interactions on GitHub. My advice is to choose a username that is not "too" silly and not "too" cute.


### 2.3. Git and GitHub readings and tutorial resources

Some nice Git and GitHub tutorial matierial is available from the following resources.

* Evans (2019) [Git and GitHub tutorial chapter](https://github.com/nyupredocs/githubtutorial/blob/master/Tutorials/git_tutorial.pdf)
* Chacon and Straub (2014), [*Pro Git*](https://git-scm.com/book/en/v2) [Fittingly, this book is available open access online at the this link.]
* Sood, Arnav (2019) “[Git, GitHub, and Version Control](https://lectures.quantecon.org/jl/version_control.html)" QuantEcon lecture
* [Atlassian Git tutorial](https://www.atlassian.com/git/tutorials). This is a good Git tutorial for interaction with Atlassian's Bitbucket platform, a GitHub competitor.
[Atlassiang git merge conflict tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)


## 3. Instructions for installing the Anaconda distribution of Python

We will be using the [Python](https://www.python.org/) programming language and many of its powerful libraries for writing the code that will run most of the computational methods we will use during the Boot Camp. Using an open source language, such as Python, has the advantage of being free and accessible for anyone who wishes to learn these materials or contribute to these projects. Being open source also allows Python users to go into the source code of any function to modify it to suit one's needs.

We recommend that each participant download the Anaconda distribution of Python provided by [Anaconda, Inc.](https://www.anaconda.com/distribution/). We recommend the most recent stable version of Python, which is currently Python 3.7. This can be done from the [Anaconda download page](https://www.anaconda.com/distribution/) for Windows, Mac OSX, and Linux machines.


### Python tutorial materials

For this training, we have included in this repository six basic Python tutorials in the [`Tutorials`](Tutorials) directory.

1. [PythonReadIn.ipynb](Tutorials/PythonReadIn.ipynb). This Jupyter notebook provides instruction on basic Python I/O, reading data into Python, and saving data to disk.
2. [PythonNumpyPandas.ipynb](Tutorials/PythonNumpyPandas.ipynb). This Jupyter notebook provides instruction on working with data using `NumPy` as well as Python's powerful data library `pandas`.
3. [PythonDescribe.ipynb](Tutorials/PythonDescribe.ipynb). This Jupyter notebook provides instruction on describing, slicing, and manipulating data in Python.
4. [PythonFuncs.ipynb](Tutorials/PythonFuncs.ipynb). This Jupyter notebook provides instruction on working with and writing Python functions.
5. [PythonVisualize.ipynb](Tutorials/PythonVisualize.ipynb). This Jupyter notebook provides instruction on creating visualizations in Python.
6. [PythonRootMin.ipynb](Tutorials/PythonRootMin.ipynb). This Jupyter notebook provides instruction on implementing univariate and multivariate root finders and unconstrained and constrained minimizers using functions in the [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) sub-library.

To further one's Python programming skills, a number of other great resources exist.

* The [official Python 3 tutorial site](https://docs.python.org/3/tutorial/)
* [QuantEcon.net](https://lectures.quantecon.org/py/) is a site run by [Thomas Sargent](http://www.tomsargent.com/) (NYU Stern) and [John Stachurski](http://johnstachurski.net/) (Australia National University). QuantEcon has a very large number of high-quality economics focused computational tutorials in Python. The first three sections provide a good introduction to Python programming.
* [Python computational labs](https://acme.byu.edu/2019-2020-materials/) of the Applied and Computational Mathematics Emphasis at Brigham Young University.
* [Code Academy's Python learning module](https://www.codecademy.com/learn/learn-python)


## 4. Jupyter Notebooks

Because we are using Python in this training, students might want to use a Jupyter notebook as their development environment. Furthermore, many of the Python tutorials in the [Tutorials](Tutorials) folder are Jupyter notebooks. [Jupyter notebooks](http://jupyter.org/) are files that end with the `*.ipynb` suffix. These notebooks are opened in a browser environment and are an open source web application that combines instructional text with live executable and modifyable code for many different programming platforms (e.g., Python, R, Julia). Jupyter notebooks are an ideal tool for teaching programming as they provide the code for a user to execute and they also provide the context and explanation for the code.

These notebooks used to be Python-specific, and were therefore called iPython notebooks (hence the `*.ipynb` suffix). But Jupyter notebooks now support many programming languages, although the name still pays homage to Python with the vestigal "py" in "Jupyter". The notebooks execute code from the kernel of the specific programming language on your local machine.

Jupyter notebooks capability will be automatically installed with your download of the [Anaconda distribution](https://www.anaconda.com/download/) of Python. If you did not download the Anaconda distribution of Python, you can download Jupyter notebooks separately by following the instructions on the Jupyter [install page](http://jupyter.org/install).


### 4.1. Opening a Jupyter notebook

Once Jupyter is installed--whether through Anaconda or through the Jupyter website--you can open a Jupyter notebook by the following steps.

1. Navigate in your terminal to the folder in which the Jupyter notebook files reside. In the case of the Jupyter notebook tutorials in this repository, you would navigate to the `~/BootCamp2019/Tutorials/` directory.
2. Type `jupyter notebook` at the terminal prompt.
3. A Jupyter notebook session will open in your browser, showing the available `*.ipynb` files in that directory.
  *  In some cases, you might receive a prompt in the terminal telling you to paste a url into your browser.
4. Double click on the Jupyter notebook you would like to open.

It is worth noting that you can also simply navigate to the URL of the Jupyter notebook file in the GitHub repository on the web (e.g., [https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/PythonReadIn.ipynb](https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/PythonReadIn.ipynb)). You can read the Jupyter notebook on GitHub.com, but you cannot execute any of the cells. You can only execute the cells in the Jupyter notebook when you follow the steps above and open the file from a Jupyter notebook session in your browser.


### 4.2. Using an open Jupyter notebook

Once you have opened a Jupyter notebook, you will find the notebook has two main types of cells: Markdown cells and Code cells. Markdown cells have formatted Jupyter notebook markdown text, and serve primarily to present context for the coding cells. A reference for the markdown options in Jupyter notebooks is found in the [Jupyter markdown documentation page](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html).

You can edit a Markdown cell in a Jupyter notebook by double clicking on the cell and then making your changes. Make sure the cell-type box in the middle of the top menu bar is set to `Markdown`. To implement your changes in the Markdown cell, type `Shift-Enter`.

A Code cell will have a `In [ ]:` immediately to the left of the cell for input. The code in that cell can be executed by typing `Shift-Enter`. For a Code cell, the  cell-type box in the middle of the top menu bar says `Code`.


### 4.3. Closing a Jupyter notebook

When you are done with a Jupyter notebook, you first save any changes that you want to remain with the notebook. Then you close the browser windows associated with that Jupyter notebook session. You should then close the local server instance that was opened to run the Jupyter notebook in your terminal window. On a Mac or Windows, this is done by going to your terminal window and typing `Cmd-C` or `Ctrl-C` and then selecting `y` for yes and hitting `Enter`.


## 5. Text editor suggestions

In our recommended Python development workflow, you will write Python scripts and modules (`*.py` files) in a text editor. Then you will run those scripts from your terminal. You will want a capable text editor for developing your code. Many capable text editors exist, but we recommend three.

1. [Atom](https://atom.io)
2. [Sublime Text 3](https://www.sublimetext.com/)
3. [Vim](http://www.vim.org)

Atom and Vim are completely free. A trial version of Sublime Text 3 is available for free, but a licensed version is $80 (US dollars). In the following subsections, we give some of the details of each of the above three text editors.


### 5.1. Atom

[Atom](https://atom.io) is an open source text editor developed by people at GitHub.com. This editor has all the features of Sublime Text 3, but it also allows users full customizability. Further, it has been a while now that the users of Atom have surpassed the critical mass necessary to keep the editor progressing with the most cutting edge additions.

There are several packages you'll want to install with Atom.  Once Atom is installed, you can add packages by navigating Atom->Preferences->Install and then typing in the name of the package you would like to install.

For work with Python, we recommend the following packages be installed:

* MagicPython
* python-indent
* tabs-to-spaces
* minimap
* open-recent
* linter-python-pep8

For development with GitHub we recommend:

* merge-conflict

If using LaTex in this editor, the following packages are helpful:

* atom-latex
* latextools
* autocomplete-bibtex
* dictionary
* latexer
* pdf-view

In addition, if you are using a Mac, you will also want to download the [Skim](http://skim-app.sourceforge.net) PDF viewer to aid in displaying PDF files compiled from TeX with Atom.


### 5.2. Sublime Text 3

[Sublime Text 3](https://www.sublimetext.com) is the most widely used and versatile private software text editor. It has tremendous flexibility, as well as the polish of a piece of professional software. Sublime Text 3 will cost $80 for a license, although you can use a trial version indefinitely without charge while only having to suffer through frequent reminders to buy the full version.


### 5.3. Vim

[Vim](http://www.vim.org) is free and very powerful. Vim is the hard-core developer's text editor of choice. The learning curve for using vim is a little steeper than that of Atom and Sublime Text 3, but it also has some advantages for efficient programming. Vim has navigation that does not use a mouse or trackpad. Eventually, your fingers never leave your keyboard. Further, most terminals have Vim built in so you can more easily use Vim to edit scripts and modules on the fly with your terminal session.


## 6. PEP 8, docstring commenting, and module structure

Computer code executes some set of commands in an organized way. In every case, there are often many ways to execute a set of instructions--some ways more efficient than others. However, code has at least three functions.

1. Efficiently execute the task at hand.
2. Be accessible and usable to other programmers.
3. Be scalable and integrable with other projects and procedures.

Bill Gates is credited with the following plea for efficiency and parsimony in code writing.

> "Measuring programming progress by lines of code is like measuring aircraft building progress by weight."

Strong support for points (2) and (3) is Eagleson's Law.

> "Any code of your own that you haven't looked at for six or more months might as well have been written by someone else."

Because of the latter two characteristics, Python code has developed some conventions and best practices, some of which have been institutionalized in the [PEP 8--Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) ("PEP" stands for Python Enhancement Proposals). Key examples PEP 8 Python coding conventions are the following.

* Indents should be 4 spaces (not tab)
* Limit all lines to a maximum of 79 characters long blocks of text being limited to 72 characters (Evans limits all his lines to 72 characters)
* Use a space after a comma
* Use a space before and after arithmetic operators

In the text editors Atom, Sublime Text 3, and Vim, you can install Linter packages that highlight areas of your code that break PEP 8 rules and tell you what the violation is.

There are fewer conventions in docstring structure, but we have developed some of our own that are outlined in the [PythonFuncs.ipynb](https://github.com/OpenSourceMacro/BootCamp2019/blob/master/Tutorials/PythonFuncs.ipynb) Jupyter notebook. See especially Sections 3 and 4 of the Jupyter notebook.


## 7. References and Resources


### References
* Chacon, Scott and Ben Straub, [*Pro Git: Everything You Need to Know About Git*](https://git-scm.com/book/en/v2.), 2nd Edition, Apress (2014).
* Evans, Richard W., "[Using Git and GitHub](https://github.com/nyupredocs/githubtutorial/blob/master/Tutorials/git_tutorial.pdf)," unpublished manuscript (September 2019).
* Sood, Arnav, “[Git, GitHub, and Version Control](https://lectures.quantecon.org/jl/version_control.html),” QuantEcon Open Access Lecture (downloaded August 28, 2019).


### Resources
* [Atlassian Git tutorial](https://www.atlassian.com/git/tutorials)
* [Atlassiang git merge conflict tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
