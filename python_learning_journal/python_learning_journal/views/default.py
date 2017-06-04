"""Create views and route them to jinja2 files."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from python_learning_journal.data.data import JOURNAL_ENTRIES_DICT
import io
import os


HERE = os.path.dirname(__file__)

@view_config(route_name='list_view', renderer='../templates/listing.jinja2')
def list_view(request):
    """View for the main listing page."""
    return {"journal_entries": JOURNAL_ENTRIES_DICT}


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Detailed view for one journal entry based on it's id."""
    the_id = int(request.matchdict['id'])
    try:
        # TODO: FIX SO THAT WE GET CORRECT ENTRY!!
        entry = JOURNAL_ENTRIES_DICT[the_id]

    except IndexError:
        raise HTTPNotFound

    return {
        'entry': entry
    }


@view_config(route_name='create_view', renderer='../templates/create.jinja2')
def create_view(request):
    return {}


@view_config(route_name='update_view', renderer='../templates/update.jinja2')
def update_view(request):
    """View to make changes to a journal entry."""
    the_id = int(request.matchdict['id'])
    try:
        # TODO: FIX SO THAT WE GET CORRECT ENTRY!!
        entry = JOURNAL_ENTRIES_DICT[the_id]

    except IndexError:
        raise HTTPNotFound

    return {
        'entry': entry
    }
