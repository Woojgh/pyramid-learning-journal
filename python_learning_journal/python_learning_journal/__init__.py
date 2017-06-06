from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    if os.environ.get('DATABASE_URL', ''):
        settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.views')
    config.scan()
    return config.make_wsgi_app()
