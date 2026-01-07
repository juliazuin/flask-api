import os


class LocalConfig:
    mongo_user = os.getenv("MONGODB_USER")
    mongo_pass = os.getenv("MONGODB_PASSWORD")
    mongo_host = os.getenv("MONGODB_HOST")
    mongo_db = os.getenv("MONGODB_DB")

    MONGO_URI = (
        f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}/{mongo_db}?authSource=admin"
    )


class ProdConfig:
    mongo_user = os.getenv("MONGODB_USER")
    mongo_pass = os.getenv("MONGODB_PASSWORD")
    mongo_host = os.getenv("MONGODB_HOST")
    mongo_db = "users"
    
    MONGODB_SETTINGS = {
        "MONGO_URI": "mongodb+srv://admin:<db_password>@cluster0.er82gea.mongodb.net/users?appName=Cluster0"
    }


class TestConfig:
    MONGO_URI = "mongodb://localhost/usuarios"  # mongomock vai capturar isso
