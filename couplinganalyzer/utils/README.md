### utils
The utils folder is the main functionality of the application. It handles extracting the information from the .zip file, parsing the resultant Java code, and generating a dependency graph out of all the classes in the .zip file, which it uses to compute coupling metrics.

* [code_extract.py](code_extract.py) parses a list of strings containing Java code and returns the ASTs of all the classes to the user. The parsing is done via the [javalang](https://github.com/c2nes/javalang) Python package.

* [depgraph.py](depgraph.py) implements a simple Python class that generates the dependency graph from the ASTs. See the source file for more information.

* [file_uploader.py](file_uploader.py) holds some utility functions for uploading .zip files to the server and validating the file type (only .zip files are supported).

* [zip_extract.py](zip_extract.py) extracts source code strings out of the supplied zip file, and sends it through to the code extractor and DepGraph to compute the coupling.
