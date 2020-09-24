import pytest

from server import app as flask_app

""" Sets up the flask app for testing before running each test.  """

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
