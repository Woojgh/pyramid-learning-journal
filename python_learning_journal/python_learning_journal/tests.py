from pyramid import testing
from pyramid.response import Response
import pytest

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


def test_list_view_returns_response_given_request(list_view_response):
    """Assert if list view returns a valid response."""
    assert isinstance(list_view_response, Response)


def test_detail_view_returns_response_given_request(detail_view_response):
    """Assert if detail view returns a valid response."""
    assert isinstance(detail_view_response, Response)


def test_create_view_returns_response_given_request(create_view_response):
    """Assert if create view returns a valid response."""
    assert isinstance(create_view_response, Response)


def test_update_view_returns_response_given_request(update_view_response):
    """Assert if update view returns a valid response."""
    assert isinstance(update_view_response, Response)


def test_list_view_is_good(list_view_response):
    """Assert that list view response returns a status 200 OK."""
    assert list_view_response.status_code == 200


def test_detail_view_is_good(detail_view_response):
    """Assert that detail view response returns a status 200 OK."""
    assert detail_view_response.status_code == 200


def test_create_view_is_good(create_view_response):
    """Assert that create view response returns a status 200 OK."""
    assert create_view_response.status_code == 200


def test_update_view_is_good(update_view_response):
    """Assert that update view response returns a status 200 OK."""
    assert update_view_response.status_code == 200


# def test_home_view_returns_proper_content(home_response):
#     """Home view response includes the content we added."""
#     expected_text = '<h1 style="color: blue;">Hey, this is HTML in some external file.</h1>'
#     assert expected_text in home_response.text
