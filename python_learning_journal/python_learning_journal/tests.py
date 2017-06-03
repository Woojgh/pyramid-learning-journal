# from pyramid import testing
# from pyramid.httpexceptions import HTTPNotFound
# from python_learning_journal.views.entries import JOURNAL_ENTRIES

# import pytest


# @pytest.fixture
# def list_response():
#     """Return a response from the home page."""
#     from python_learning_journal.views.default import list_view
#     request = testing.DummyRequest()
#     response = list_view(request)
#     return response


# def test_home_view_returns_response_given_request(list_response):
#     """Home view returns a Response object when given a request."""
#     assert "entry" in list_response
#     assert "entries" in list_response
#     assert list_response["entries"] == JOURNAL_ENTRIES


# def test_home_view_is_good(list_response):
#     """Home view response comes with a status 200 OK."""
#     assert list_response.status_code == 200


# # ++++++++++++_+_+_+_+_+_+_+MONKIEBARS+_+_+_+_+_+_+_+_+_+


# @pytest.fixture
# def testapp():
#     """Create a test application to use for functional tests."""
#     from python_learning_journal import main
#     from webtest import TestApp
#     app = main({})
#     return TestApp(app)


# def test_home_route_returns_home_content(testapp):
#     """Tests what the h1 and titles should contain"""
#     response = testapp.get('/')
#     html = response.html
#     assert 'Pena' in str(html.find('h1').text)
#     assert 'Learning Journal' in str(html.find('title').text)


# def test_home_route_listing_has_all_expenses(testapp):
#     """tests the total size of the lists on the home page"""
#     response = testapp.get('/')
#     html = response.html
#     assert len(JOURNAL_ENTRIES) == len(html.find_all('li'))


# def test_detail_route_with_bad_id(testapp):
#     """tests an edge case if you got outside the smount of journal entries"""
#     response = testapp.get('/expense/400', status=404)
#     assert "DIDIDIDIDIDIDID YOU KNOW ITS GOAT TIMEIEMIEMEI!@!!!d" in response.text
