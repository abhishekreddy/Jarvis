import nltk
import os
import random
from DataFile import DataFile

BOTNAME = "Jarvis"
USERNAME = "Anonymous"

GREETINGS_KEYWORDS=("hello", "hi", "hey", "whassup", "namasthe", "namaste", "what's up",)
GREETINGS_RESPONCES=["Hey", "Whats up bro", "Tell me bro", "Tell me Your honour", "Master I may blow you up"]

class ProcessSentence:
    """This class to process the user sentence"""

    def __init__(self):
        self.username = USERNAME
        self.botname  = BOTNAME
        self.db = DataFile()

    def get_user_name(self):
        return self.username

    def get_bot_name(self):
        return self.botname

    def set_user_name(self, name):
        self.username = name

    def set_bot_name(self, name):
        self.botname = name

    def check_for_greeting(self, sentence):
        """Check for greeting setence and respond"""
        words = sentence.split()
        for word in words:
            greeting = self.db.check_for_greeting(word.lower())
            if greeting is not None:
                return self.db.get_greeting_response()

    def process_sentence(self, sentence):
        """Process the user sentence"""

