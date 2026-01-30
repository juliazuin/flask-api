import os

MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_DB = os.getenv("MONGODB_DB")
MONGO_URI = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_DB}?authSource=admin"


class LocalConfig:
    MONGO_URI = MONGO_URI


class ProdConfig:
    MONGO_URI = MONGO_URI


class TestConfig:
    MONGO_URI = "mongodb://localhost/usuarios"  # mongomock vai capturar isso
