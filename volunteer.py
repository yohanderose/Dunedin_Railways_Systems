from uuid import uuid4
from train import StationMaster

"""
Here is probably the most important class.

"""


class Event(object):
    def __init__(self, guests, date, description=""):
        self.id = 'e' + str(uuid4())[:8]
        self.date = date
        self.guests = guests
        self.description = description
        if guests < 272:
            self.train = StationMaster.Q
        else:
            self.train = StationMaster.W

    # Alter event details...


class Volunteer(object):

    def __init__(self, last, first, phone="", email=""):
        self.id = 'v_' + str(uuid4())[:8]
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

        # Change details methods...
        # ID especially, also email and phone


################################################################################
