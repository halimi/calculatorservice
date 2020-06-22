from pyramid.config import Configurator


def main():
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('calculator', '/calculator')
        config.scan('.views')
        return config.make_wsgi_app()
