### couplinganalyzer
This folder is the root of the Flask application. It acts as a web interface for the main functionality.

* [app.py](app.py) holds the main application instance and sets up some basic configuration.

* [config.py](config.py) holds the configuration variables used by Flask to handle session cookie management and where .zip files should get uploaded on the server

* [views.py](views.py) is the main URL routing logic. It handles displaying the main page and the analysis page in the browser. To get a sense for what these pages look like, take a look in the [templates](templates/) folder.

* [uploads/](uploads/) is where uploaded .zip files go. It currently contains nothing and is only checked into version control to simplify setting up the app on your computer. (The Flask app has hardcoded the location for convenience).
