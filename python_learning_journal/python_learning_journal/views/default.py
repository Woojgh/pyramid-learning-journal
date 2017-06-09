"""Create views and route them to jinja2 files."""
from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound
)
from python_learning_journal.models import Entry
import datetime
from pyramid.security import remember, forget
from python_learning_journal.security import check_credentials


@view_config(route_name='list_view', renderer='../templates/listing.jinja2', require_csrf=False)
def list_view(request):
    """View for the main listing page."""
    journal_entries = request.dbsession.query(Entry).all()
    return {"journal_entries": journal_entries, 'authenticated': request.authenticated_userid}


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2', require_csrf=False)
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


@view_config(route_name='create_view', renderer='../templates/create.jinja2', permission='secret', require_csrf=True)
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


@view_config(route_name='update_view', renderer='../templates/update.jinja2', permission='secret', require_csrf=True)
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


@view_config(route_name='login_view', renderer='../templates/login.jinja2', require_csrf=False)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(
                location=request.route_url('list_view'),
                headers=headers
            )

        else:
            return {'error': 'Bad request'}
    return {}


@view_config(route_name='logout_view', require_csrf=False)
def logout(request):
    headers = forget(request)
    return HTTPFound(request.route_url('list_view'), headers=headers)


# @view_config(route_name='api_journal_list', renderer='json')
# def api_list(request):
#     entries = request.dbsession.query(Entry).all()
#     return {'entries': entries}
