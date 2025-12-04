from application import create_app
import os


if os.getenv("FLASK_ENV") == "development":
    app = create_app(os.path.join(os.path.dirname(__file__), "config.py"))
else:
    app = create_app(os.path.join(os.path.dirname(__file__), "config.py"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
