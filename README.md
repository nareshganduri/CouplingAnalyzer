# CouplingAnalyzer

The coupling analyzer is a web interface for reading in a .zip file containing a bunch of Java files, computing the code coupling of all the classes, and displaying the code metrics to you in your browser.

Coupling is computed using [efferent and afferent coupling](http://www.informit.com/articles/article.aspx?p=1561879&seqNum=3), so a value near 0 is good, and a value near 1 is bad.

High coupling indicates strong interdependencies between classes in the package, which means changes to one class will probably require changes to all of it's dependent classes as well. This complicates refactoring, which is why loose coupling is preferred.

## Documentation
* [requirements.txt](requirements.txt) is used by [pip](https://pypi.org/project/pip/) to install the project's dependencies into a virtual environment.

* [run.py](run.py) kicks off a local server to test the application in. It should be run from a virtual environment (see below)

* [setup-win.bat](setup-win.bat) is a little script that will setup the local environment on Windows for running the app on a local server (see below).

See the READMEs in the other folders for more information regarding implementation.

## Installing on Windows
Running the software on Windows is pretty easy. You'll need [Python](https://www.python.org/) and [virtualenv](https://virtualenv.pypa.io/en/stable/) to get started.

* First, clone the repository:
```
git clone https://github.com/nareshganduri/CouplingAnalyzer
```

* `cd` into the directory:
```
cd CouplingAnalyzer
```

* Now just run the included batch file:
```
setup-win.bat
```
This will setup a virtualenv for you (So as to not conflict with your current python environment) and setup an instance configuration folder for [Flask](http://flask.pocoo.org/).

* Now just run:
```
venv\Scripts\python run.py
```
This will kick off a local server for you. You can see the program in action by visiting http://localhost:3000/ in your browser of choice.

* You'll need a .zip file to upload. There's an example .zip file in the [test](test/) folder.
