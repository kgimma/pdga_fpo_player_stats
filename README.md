# Scrapers

Module for multiple scrapers.

## List of scrapers

### PDGA

The PDGA scraper gathers data from the PDGA website for the purposes of making visualizations and generally exploring data.

This scraper returns a CSV for use with data viz tools.

## Modular Program Architecture

### Modules

A module is simply a file. Each module will be responsible for a single scraper. This follows the 'single responsibility principal' which states that each module should only be responsible for a single thing. A module can represent a car, or a person, or an animal, or in this case, a scraper. A module is always a noun.

Each module has multiple functions. As with modules, each function should only do a single thing, again following the single responsibility principle.

Each module has a __main__() function. This function is where the above functions are used, and the program itself actually runs.

### Docstrings

Each module and function have docstrings, which describe what they do.

### Util

There is a util file, which will house functions that can be used by multiple scrapers. An example is the fetch_url() function, currenly in the utils file.

## Requirements

To import a library like BeautifulSoup, add the library name and version number to the requirements file. Then run the following command (without the quotes):

`sudo pip3 install -r scrapers/requirements.txt`

You can find projects and their version number by searching [pypi.org](https://pypi.org/project/beautifulsoup4/).

## Git ignore

The .gitignore file in this directory tells git to ignore certain files, to save space and time when uploading your code to and from git. So far we added __pycache__, which is a folder that holds python-generated bytecode which is read by the computer to run your code more efficiently. I have never had to know what's in this directory, other than the fact that it's machine readable binary. So don't worry too much about what's happening here.

## __init__.py

Each module has an __init__.py file. It's meant to set initial variables and other setup, none of which is necessary here. However, it is necessary to have that blank file so we can import this project elsewhere.

## File layout

Each scraper will have at least four sections

* Constants - to declare variables that won't change, like the url
* Extract - functions which fetch the data from it's source
* Transform - functions that take the fetched data and transform it into something more manageable
* Load - functions that take the transformed data and load it into something more useful, like a csv

ETL = Extract Transform Load

NOTE: These definitions are sometimes fuzzy, so load might mean something different in different contexts. Also maybe this isn't the correct definition, but it's a definition I've found useful. This is worth further investigation since you'll be doing interviews and these terms may come up.

## Use template

Create any file with the .py extension. For example for an mlb scraper, you'd call it mlb.py.

Inside of that file, type scraper_py and hit enter. The template will appear in the file.
## Run in a terminal

type cd Documents/python

In a terminal run these commands (without the parentheses).

* `python3`
* `import scrapers.pdga`
* `scrapers.pdga.__main__()`
* `exit()`
* `nano pdga.csv`
