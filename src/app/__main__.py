# src/app/__main__.py
from . import app   # imports Flask app from __init__.py

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
