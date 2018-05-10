from flask import Flask

# create the app and set up the configuration
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('couplinganalyzer.config')
app.config.from_pyfile('config.py')

# need to import the views AFTER the app is properly initialized
import views
