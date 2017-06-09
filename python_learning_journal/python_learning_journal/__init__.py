from pyramid.config import Configurator
import os
import twitter


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
    print(api.VerifyCredentials())
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.scan()
    return config.make_wsgi_app()
