import os
import sqlite3
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", "highscores.sqlite"))
connection.row_factory = sqlite3.Row

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass
connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", os.getenv("DATABASE_FILENAME") or "default highscores.sqlite"))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
