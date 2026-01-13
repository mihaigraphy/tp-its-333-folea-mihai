import unittest
import os
from app import app, db
from model import Etudiant, User

class StudentAppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_database.db'
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, self.db_name)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False # If using WTF
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()
            # Create a test user
            from model import create_user
            create_user('testuser', 'testpass')

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_unauthorized_access(self):
        rv = self.app.get('/', follow_redirects=True)
        # Should redirect to login
        assert b'Connexion' in rv.data

    def test_login_and_access(self):
        self.login('testuser', 'testpass')
        rv = self.app.get('/')
        assert b'Liste des' in rv.data

    def test_add_student(self):
        self.login('testuser', 'testpass')
        rv = self.app.post('/new', data=dict(
            nom='Alice',
            addr='123 Wonderland',
            pin='1111'
        ), follow_redirects=True)
        assert b'Alice' in rv.data

    def test_swagger(self):
        rv = self.app.get('/swagger/')
        assert rv.status_code == 200
        assert b'swagger-ui' in rv.data
        
        rv = self.app.get('/static/swagger.json')
        assert rv.status_code == 200
        assert b'openapi' in rv.data

if __name__ == '__main__':
    unittest.main()
