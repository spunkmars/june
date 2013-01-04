import os
import tempfile
from june.app import create_app


class TestDatabase(object):
    def setUp(self):
        app = create_app()
        self.db_fd, self.db_path = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % self.db_path
        app.config['TESTING'] = True
        self.app = app.test_client()

        #: rv = self.app.get('/')
        #: assert 'something' in rv.data

        #from june.account import models
        #models.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)
