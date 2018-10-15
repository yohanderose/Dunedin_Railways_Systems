from volunteer import Volunteer, Event
from train import StationMaster
import sqlite3
import numpy as np
import pandas as pd

################################################################################
# SETUP
def open():
    conn = sqlite3.connect('TEST.db')
    return conn, conn.cursor()


def close(conn):
    conn.commit()
    conn.close()


# CREATE db
conn, c = open()

# FOR DEBUGGING ONLY!!!!!!!!!!!!!!!!!!!!!!
c.execute("""DROP TABLE Events""")
c.execute("""DROP TABLE Volunteers""")

c.execute("""CREATE TABlE IF NOT EXISTS Events (
    id varchar2 Primary Key,
    datetime varchar2,
    guests varchar2,
    train varchar2,
    description varchar2
    )""")

c.execute("""CREATE TABlE IF NOT EXISTS Volunteers (
    id varchar2 Primary Key,
    surname varchar2,
    firstname varchar2,
    email varchar2,
    phone varchar2
    )""")

close(conn)

# CREATE Sarah and her Carriage sets
sarah = StationMaster()


################################################################################
# METHODS

def createEvent(guests, date, description=""):
    # make some condition so no two events have the same id
    e = Event(guests, date, description)

    # INSERT Event details
    conn, c = open()
    insert = [str(e.id), str(pd.to_datetime(e.date, infer_datetime_format=True)),
              str(e.guests), str(e.train.name), str(e.description)]
    c.execute("""INSERT INTO Events VALUES(?,?,?,?,?)""", insert)

    # CREATE *eventID*Volunteers View
    c.execute("""CREATE VIEW {} AS
    SELECT * FROM Volunteers
    """.format(e.id))

    # 1.FOR EVERY Volunteer in *eventID*Volunteers
    c.execute("""SELECT * FROM {}""".format(e.id))
    volunteers = c.fetchall()
    print(volunteers)
    # 2. SEND e.description to volunteer.email
    close(conn)


def createVolunteer(last, first, phone="", email=""):
    v = Volunteer(last, first, phone, email)

    conn, c = open()

    insert = [str(v.id), str(v.last), str(v.first), str(v.phone), str(v.email)]
    c.execute("""INSERT INTO Volunteers VALUES(?,?,?,?,?)""", insert)

    close(conn)


################################################################################
# PROGRAM

if __name__ == '__main__':
    
    createVolunteer("de Rose", "Yohan", "0211121015", "yohanderose@gmail.com")
    createVolunteer("Turnbull", "Jack", "0221121015", "deryo530@student.otago.ac.nz")

    createEvent(300, "10-10-2018", "Yeah the bois.")
    print("DONE")
