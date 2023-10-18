from dynaconf import FlaskDynaconf


def init_app(app):
    return FlaskDynaconf(app)
