import sqlite3

class Database(object):
    """Creates the Database for all the tables we need."""

    def __init__(self):
        self.db = sqlite3.connect('DUNRAIL.db')


################################################################################

    """
    Here is where most of the backend will take place.
    Instantiaing tables (IF NOT EXISTS), managing and distributing volunteers etc.

    Right now the DB is stored locally on a file (and so is everything),
    but let's just get something going before we think about online hosting.
    """

if __name__ == '__main__':
    db = Database()
