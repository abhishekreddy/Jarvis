from DataFile import DataFile
from enum import Enum

USERNAME = "Ananymous"

class User:
    """User Session"""
    valid = False
    username = USERNAME
    def __init__(self):
        """Instantitae user Session"""
        self.db = DataFile()

    def get_session_validity(self):
        return self.valid

    def create_user_session(self, name, key):
        """Creates the user session with the given name and passkey"""


