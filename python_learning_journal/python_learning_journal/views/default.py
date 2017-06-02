""""I don't know what I'm doing."""
from pyramid.response import Response
import io
import os


HERE = os.path.dirname(__file__)

def list_view(request):
    with io.open(os.path.join(HERE, '../templates/entry.html')) as the_file:
        imported_html = the_file.read()

    return Response(imported_html)


def detail_view(request):
    with io.open(os.path.join(HERE, '../templates/entry.html')) as the_file:
        imported_html = the_file.read()

    return Response(imported_html)


def create_view(request):
    with io.open(os.path.join(HERE, '../templates/new.html')) as the_file:
        imported_html = the_file.read()

    return Response(imported_html)


def update_view(request):
    with io.open(os.path.join(HERE, '../templates/edit.html')) as the_file:
        imported_html = the_file.read()

    return Response(imported_html)
