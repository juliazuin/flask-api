from application import create_app
import os


if os.getenv("FLASK_ENV") == "development":
    # app = create_app(os.path.join(os.path.dirname(__file__), "config.py"))
    app = create_app("config.LocalConfig")
else:
    app = create_app("config.ProdConfig")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
