"""Initialize Flask app"""
from flask import Flask
# Blueprint folders
from app.about import about
# Extensions
from app.extensions import (
    # bcrypt,
    # cache,
    csrf_protect,
    mongo_engine,
    # mongo_client_db,
    # debug_toolbar,
    # flask_static_digest,
    login_manager,
    # migrate,
)


def init_app(config_object="config.Config"):
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    # databases
    mongo_engine.init_app(app)
    # mongo_client_db.init_app(app)
    # bcrypt.init_app(app)
    # cache.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    # debug_toolbar.init_app(app)
    # migrate.init_app(app, db)
    # flask_static_digest.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(about.about_bp)
    return None
