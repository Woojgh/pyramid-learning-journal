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


def test_list_view_returns_proper_content(list_view_response):
    """Assert that List view response has proper contnent."""
    expected_text = """<nav class="main-nav">
        <div class="icon-menu"></div>
        <ul>
          <li class="tab" data-content="entries"><a href="/" class="icon-home"> Home</a></li>
          <li class="tab"><a href="/journal/new-entry">New Entry</a></li>
          <li class="tab" data-content="about"><a href="/about" class="icon-address-book"> About</a></li>
        </ul>
      </nav>"""
    assert expected_text in list_view_response.text


def test_detail_vieiw_returns_proper_content(detail_view_response):
    """Assert that Detail view response has proper content."""
    expected_text = """<nav class="main-nav">
        <div class="icon-menu"></div>
        <ul>
          <li class="tab" data-content="entries"><a href="/" class="icon-home"> Home</a></li>
          <li class="tab"><a href="/journal/new-entry">New Entry</a></li>
          <li class="tab" data-content="about"><a href="/about" class="icon-address-book"> About</a></li>
        </ul>
      </nav>"""
    assert expected_text in detail_view_response.text


def test_create_view_returns_proper_content(create_view_response):
    """Assert that create view has proper content."""
    expected_text = """<section id="write" class="tab-content">
        <h1>New Entrees</h1>
        <form action="#" id="new-form">
          <label>
            <input type="text" id="entry-title" placeholder="Entry title" required>
          </label>
          <textarea id="entry-body" rows="8" cols="40" required></textarea>
          <label>
            <input type="text" id="entry-author" placeholder="Author Name" required>
          </label>
          <label>
            <input type="text" id="entry-author-url" placeholder="Author's URL" required>
          </label>
          <label>
            <input type="text" id="entry-category" placeholder="Category" required>
          </label>
          <button type="submit">Submit</button>
        </form>
      </section>"""
    assert expected_text in create_view_response.text


def test_update_view_returns_proper_content(update_view_response):
    """Asser that update view has proper content."""
    expected_text = """<main class="clearfix">
      <h1>Blog Stats</h1>
      <section id="blog-stats">
        <dt>Total entries:</dt> <dd class="entries"></dd>
        <dt>Total words:</dt> <dd class="words"></dd>
        <h2>Author Stats</h2>
        <p><em>Details on who is writing, and how much writing they are doing...</em></p>
        <ul class="author-stats">
        </ul>
      </section>
    </main>"""
    assert expected_text in update_view_response.text