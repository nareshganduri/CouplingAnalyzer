### templates
Flask templates are stored here.

* [home.html](home.html) is the home page of the app. There's almost nothing on it except for a button to upload a .zip file. Errors also get redirected here.

* [analysis.html](analysis.html) holds the analysis results. It displays a table of the coupling metrics for each class in the uploaded .zip file and it displays an interactive graph (using [vis.js](http://visjs.org/)) of the class dependencies.
