import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), '..', 'banco.db')


def get_conn():
    return sqlite3.connect(DB)
