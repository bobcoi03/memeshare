import os

from flask import Flask, redirect, render_template, url_for
from graphviz import render

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite3'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    '''
        initialize db
    '''
    from . import db
    db.init_app(app)

    '''
        Register Blueprint from auth.py & site.py
    '''
    from . import auth, site
    app.register_blueprint(auth.bp)
    app.register_blueprint(site.bp)

    return app