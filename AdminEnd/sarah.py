import sqlite3

class Database(object):
    """docstring for ."""

    def __init__(self):
        self.db = sqlite3.connect('DUNRAIL.db')


db = Database()
