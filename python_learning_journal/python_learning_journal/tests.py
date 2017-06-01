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
def create_view():
    """Return a create view response."""
    from python_learning_journal.views.default import create_view
    request = testing.DummyRequest()
    return create_view(request)





# @pytest.fixture
# def home_response():
#     """Return a response from the home page."""
#     from expense_tracker.views.default import home_page
#     request = testing.DummyRequest()
#     response = home_page(request)
#     return response
#
#
# def test_home_view_returns_response_given_request(home_response):
#     """Home view returns a Response object when given a request."""
#     assert isinstance(home_response, Response)
#
#
# def test_home_view_is_good(home_response):
#     """Home view response comes with a status 200 OK."""
#     assert home_response.status_code == 200
#
#
# def test_home_view_returns_proper_content(home_response):
#     """Home view response includes the content we added."""
#     expected_text = '<h1 style="color: blue;">Hey, this is HTML in some external file.</h1>'
#     assert expected_text in home_response.text
