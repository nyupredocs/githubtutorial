# Git and GitHub tutorial

This is the repository for the Git and GitHub scalable collaborative workflow and methods tutorial prepared and presented by [Richard Evans](https://sites.google.com/site/rickecon/) (University of Chicago) for the NYU predoctoral economics training program hosted at New York University Stern School of Business, September 20-22, 2019 and cosponsored by [Schmidt Futures](https://schmidtfutures.com). This tutorial focuses on how to use Git and GitHub an a scalable collaborative workflow and as a medium for open source, transparent, and replicable research.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nyupredocs/githubtutorial/master)

This `README.md` serves as a syllabus, outline, and reference for the training. This document has ? sections.

1. [Schedule](#1-ose-lab-leadership)
<!-- 2. [Boot Camp schedule](#2-boot-camp-schedule)
3. [Instructions for installing the Anaconda distribution of Python](#3-instructions-for-installing-the-anaconda-distribution-of-python)
4. [Text editor suggestions](#4-text-editor-suggestions)
5. [PEP 8, docstring commenting, and module structure](#5-pep-8-docstring-commenting-and-module-structure)
6. [Using LaTeX](#6-using-latex)
7. [Git and GitHub.com tutorial](#7-git-and-gitHub-tutorial)
8. [Jupyter notebooks](#8-jupyter-notebooks)
9. [Python tutorials](#9-python-tutorials)
10. [Other Books](#10-other-books)
11. [C++ tutorials](#11-c-tutorials)
12. [References](#12-references) -->


## 1. Schedule


### 1.1. Friday, September 20

| Time | Topic | Materials |
|:----:|:----- |:--------- |
9:00a-12:00p | Git, GitHub, Python setup | [Day 1 Slides](https://github.com/nyupredocs/githubtutorial/blob/master/Slides/GitGitHub_d1.pdf) |
             | Openness and collaboration in Econ |  |
             | Git and GitHub basics              |  |
12:00-1:00p  | Lunch |  |
1:00-5:00p   | Evaluating GitHub repositories | [Project 1](https://github.com/nyupredocs/githubtutorial/blob/master/Projects/Project1.md) |


### 1.2. Saturday, September 21

| Time | Topic | Materials |
|:----:|:----- |:--------- |
9:00a-12:00p | git merge and merge conflicts | [Day 2 Slides](https://github.com/nyupredocs/githubtutorial/blob/master/Slides/GitGitHub_d2.pdf) |
             | Data best practices |  |
12:00-1:00p  | Lunch |  |
1:00-5:00p   | Collaborative economic modeling project | [Project 2](https://github.com/nyupredocs/githubtutorial/blob/master/Projects/Project2/OG2per.pdf) |
             |  | Exercises 1, 2, 3, 4 |


### 1.3. Sunday, September 22

| Time | Topic | Materials |
|:----:|:----- |:--------- |
9:00a-12:00p | Git, GitHub, Python setup | [Day 1 Slides](https://github.com/nyupredocs/githubtutorial/blob/master/Slides/GitGitHub_d1.pdf) |
             | Openness and collaboration in Econ |  |
             | Git and GitHub basics              |  |
12:00-1:00p  | Lunch |  |
1:00-5:00p   | Evaluating GitHub repositories | [Project 1](https://github.com/nyupredocs/githubtutorial/blob/master/Projects/Project1.md) |


## 2. Git and GitHub Setup

### 2.1. Install Git

`Git` is powerful version control software that must be installed on your local computer. You can check if `Git` is already installed on your machine by typing the following command in your terminal window
```
git --version
```
You can install or `Git` by following the appropriate operating system instructions on the [`Git` download page](https://git-scm.com/downloads).


### 2.2. Sign up for a GitHub account

You should sign up for a GitHub account by going to [https://github.com/join](https://github.com/join). Choose a `username` that is not too long but that represents you. Be careful on what username you choose. That will be your GitHub handle and will be the main name by which you will be recognized in your interactions on GitHub. And the goal is for you to have many productive interactions on GitHub. My advice is to choose a username that is not "too" silly and not "too" cute.


## 3. Instructions for installing the Anaconda distribution of Python

We will be using the [Python](https://www.python.org/) programming language and many of its powerful libraries for writing the code that will run most of the computational methods we will use during the Boot Camp. Using an open source language, such as Python, has the advantage of being free and accessible for anyone who wishes to learn these materials or contribute to these projects. Being open source also allows Python users to go into the source code of any function to modify it to suit one's needs.

We recommend that each participant download the Anaconda distribution of Python provided by [Anaconda, Inc.](https://www.anaconda.com/distribution/). We recommend the most recent stable version of Python, which is currently Python 3.7. This can be done from the [Anaconda download page](https://www.anaconda.com/distribution/) for Windows, Mac OSX, and Linux machines.


## 4. Text editor suggestions

In our recommended Python development workflow, you will write Python scripts and modules (`*.py` files) in a text editor. Then you will run those scripts from your terminal. You will want a capable text editor for developing your code. Many capable text editors exist, but we recommend three.

1. [Atom](https://atom.io)
2. [Sublime Text 3](https://www.sublimetext.com/)
3. [Vim](http://www.vim.org)

Atom and Vim are completely free. A trial version of Sublime Text 3 is available for free, but a licensed version is $80 (US dollars). In the following subsections, we give some of the details of each of the above three text editors.


### 4.1. Atom

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


### 4.2. Sublime Text 3

[Sublime Text 3](https://www.sublimetext.com) is the most widely used and versatile private software text editor. It has tremendous flexibility, as well as the polish of a piece of professional software. Sublime Text 3 will cost $80 for a license, although you can use a trial version indefinitely without charge while only having to suffer through frequent reminders to buy the full version.


### 4.3. Vim

[Vim](http://www.vim.org) is free and very powerful. Vim is the hard-core developer's text editor of choice. The learning curve for using vim is a little steeper than that of Atom and Sublime Text 3, but it also has some advantages for efficient programming. Vim has navigation that does not use a mouse or trackpad. Eventually, your fingers never leave your keyboard. Further, most terminals have Vim built in so you can more easily use Vim to edit scripts and modules on the fly with your terminal session.


## 5. PEP 8, docstring commenting, and module structure

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

Project 1 has students evaluate GitHub repositories.

HEAD
Project 2 has students working on General Equilibriums problem.

Project 3 will be fun!

=======
Project 2: General Equilibrium collaboration.

## References
Put references here... or not.
