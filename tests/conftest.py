# from models import Song
import pytest
from app import app,db
import tempfile

@pytest.fixture(scope='module')
def test_client():
    # flask_app = Flask(__name__)
    app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        # Establish an application context
        with app.app_context():
            # app.init_db()
            yield test_client 

# @pytest.fixture(scope='module')
# def new_song():
#     new_song = Song('test song', 1200)
#     return new_song

# @pytest.fixture(scope='module')
# def test_client():
#     flask_app = create_app('flask_test.cfg')

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client 