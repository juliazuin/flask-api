import os


class LocalConfig:
    mongo_user = os.getenv("MONGO_USER")
    mongo_pass = os.getenv("MONGO_PASSWORD")
    mongo_host = os.getenv("MONGO_HOST")
    mongo_db = os.getenv("MONGO_DB")

    MONGO_URI = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}/{mongo_db}?authSource=admin"


class ProdConfig:
    MONGODB_SETTINGS = {
        "MONGO_URI": "mongodb://admin:admin@mongodb/usuarios?authSource=admin"
        }


class TestConfig:
    MONGO_URI = "mongodb://localhost/usuarios"  # mongomock vai capturar isso
