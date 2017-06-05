"""Create views and route them to jinja2 files."""
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound
)
from python_learning_journal.models import Entry
import datetime
import os

@view_config(route_name='list_view', renderer='../templates/listing.jinja2')
def list_view(request):
    """View for the main listing page."""
    journal_entries = request.dbsession.query(Entry).all()
    return {"journal_entries": journal_entries}


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Detailed view for one journal entry based on it's id."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)

    if not entry:
        raise HTTPNotFound

    if request.method == 'GET':
        return {
            'entry': entry
        }

    if request.method == 'POST':
        return HTTPFound(
            location=request.route_url('update_view', id=entry.id)
        )

    return {}


@view_config(route_name='create_view', renderer='../templates/create.jinja2')
def create_view(request):
    """View for new listing route."""
    if request.method == "POST":
        if not request.POST['title'] or not request.POST['body']:
            return {
                'title': request.POST['title'],
                'body': request.POST['body']
            }

        new_entry = Entry(
            title=request.POST['title'],
            body=request.POST['body'],
            creation_date=datetime.datetime.now()
        )

        request.dbsession.add(new_entry)
        return HTTPFound(
            location=request.route_url('list_view')
        )

    return {}


@view_config(route_name='update_view', renderer='../templates/update.jinja2')
def update_view(request):
    """View to make changes to a journal entry."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)

    if not entry:
        raise HTTPNotFound

    if request.method == 'GET':
        return {
            'title': entry.title,
            'body': entry.body
        }

    if request.method == 'POST':
        entry.title = request.POST['title']
        entry.body = request.POST['body']
        request.dbsession.flush()

        return HTTPFound(
            location=request.route_url('detail_view', id=entry.id)
        )

    return {}