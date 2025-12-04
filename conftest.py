import mongomock
import pytest
from unittest.mock import patch
from application import create_app


@pytest.fixture
def app_with_mongomock():
    """Fixture que cria a app com mongomock em vez de MongoDB real"""
    # Criar cliente mongomock
    mongomock_client = mongomock.MongoClient()

    # Fazer patch de PyMongo para usar mongomock
    with patch('pymongo.synchronous.mongo_client.MongoClient', return_value=mongomock_client):
        # Também fazer patch do flask_pymongo
        with patch('flask_pymongo.PyMongo.__init__', lambda x: None):
            with patch('flask_pymongo.PyMongo.init_app', lambda x, y: None):
                app = create_app('config.TestConfig')
                # Substituir mongo.db pelo mongomock
                from application.db import mongo
                mongo.db = mongomock_client['usuarios']
                yield app
