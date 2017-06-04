from pyramid import testing
from pyramid.response import Response
from python_learning_journal.views.default import JOURNAL_ENTRIES_DICT
import pytest


@pytest.fixture
def testapp():
    """Create an instance of our app for testing."""
    from python_learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


@pytest.fixture
def list_view_response():
    """Return a list view response."""
    from python_learning_journal.views.default import list_view
    request = testing.DummyRequest()
    return list_view(request)


@pytest.fixture
def detail_view_response():
    """Return a detail view response."""
    from python_learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    return detail_view(request)


@pytest.fixture
def create_view_response():
    """Return a create view response."""
    from python_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    return create_view(request)


@pytest.fixture
def update_view_response():
    """Return a update view response."""
    from python_learning_journal.views.default import update_view
    request = testing.DummyRequest()
    return update_view(request)


def test_list_view_returns_dict_given_request(list_view_response):
    """Assert if list view returns a valid response."""
    assert isinstance(list_view_response, dict)


def test_detail_view_returns_dict_given_request(detail_view_response):
    """Assert if detail view returns a valid response."""
    assert isinstance(detail_view_response, dict)


def test_create_view_returns_dict_given_request(create_view_response):
    """Assert if create view returns a valid response."""
    assert isinstance(create_view_response, dict)


def test_update_view_returns_dict_given_request(update_view_response):
    """Assert if update view returns a valid response."""
    assert isinstance(update_view_response, dict)


def test_list_view_returns_proper_len_of_content(list_view_response):
    """Assert list view returns proper length of content."""
    assert len(list_view_response.get('journal_entries')) == len(JOURNAL_ENTRIES_DICT)


def test_detail_view_contains_journal_entry_attrs(detail_view_response):
    """Asser that detail view response contains correct data."""
    for key in ['id', 'title', 'creation_date', 'body']:
        assert key in detail_view_response.keys()


def test_layout(testapp):
    """Assert that layout file contains correct data."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'JourNull' in html.find('h1').text


def test_root_contents(testapp):
    """Assert that listing view contais the correct ammount of article tags."""
    response = testapp.get('/', status=200)
    html = response.html
    assert len(JOURNAL_ENTRIES_DICT) == len(html.finaAll('article'))