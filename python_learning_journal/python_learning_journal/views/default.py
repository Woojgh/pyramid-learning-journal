""""I don't know what I'm doing."""
from pyramid.view import view_config
import io
import os


HERE = os.path.dirname(__file__)

@view_config(route_name='list_view', renderer='../templates/listing.jinja2')
def list_view(request):
    return {}


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    return {}


@view_config(route_name='create_view', renderer='../templates/create.jinja2')
def create_view(request):
    return {}


@view_config(route_name='update_view', renderer='../templates/update.jinja2')
def update_view(request):
    return {}
