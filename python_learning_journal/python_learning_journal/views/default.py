"""Creating functions for view callables"""
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound
)
from python_learning_journal.models.entries import Entry
import datetime


@view_config(route_name='list', renderer='../templates/index.jinja2')
def list_view(request):
    """View for the home route."""
    entries = request.dbsession.query(Entry).all()
    return {
        'page': 'List',
        'entry': entries,
    }


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    """View for the detail route."""
    the_id = int(request.matchdict['id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    if not entry:
        raise HTTPNotFound

    return {
        'page': 'Entry',
        'entry': entry
    }


@view_config(route_name="new", renderer="../templates/new_entry.jinja2")
def create_view(request):
    """View for adding a new expense to the database."""
    if request.method == "POST" and request.POST:
        if not request.POST['title']:
            return {
                'title': request.POST['title'],
                'error': "Hey dude, you're missing a little something"
            }
        new_entry = Entry(
            title=request.POST['title'],
            entry=request.POST['entry'],
            creation_date=datetime.datetime.now()
        )
        request.dbsession.add(new_entry)
        return HTTPFound(
            location=request.route_url('list')
        )

    return {}


@view_config(route_name="edit", renderer="../templates/edit_entry.jinja2")
def update_view(request):
    """View for editing an entry."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return {
            "page": "Edit Page",
            "title": entry.title,
            "entry": entry.entry
        }
    if request.method == "POST":
        entry.title = request.POST['title']
        entry.entry = request.POST['entry']
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=entry.id))
