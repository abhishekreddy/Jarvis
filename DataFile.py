import sqlite3 as sql
import os
import random
from pathlib import Path

DATABASE = "Jarvis.db3"
GREETINGS_KEYWORDS=("hello", "hi", "hey", "whassup", "namasthe", "namaste", "what's up",)
GREETINGS_RESPONCES=["Hey", "Whats up bro", "Tell me bro", "Tell me Your honour", "Master I may blow you up"]

CREATE_USER_SESSION_TABLE = """ CREATE TABLE IF NOT EXISTS USER_SESSION(
                                data text PRIMARY KEY NOT NULL UNIQUE
                                ); """
UPDATE_USER_SESSION_TABLE = """ INSERT INTO USER_SESSION(data)
                                VALUES(?) """

CHECK_FOR_USER_SESSION = """SELECT EXISTS (SELECT * FROM USER_SESSION WHERE data = ?);"""

CREATE_USER_DETAILS_TABLE = """ CREATE TABLE IF NOT EXISTS USER_PROFILE(
                                id interger PRIMARY KEY UNIQUE,
                                name text NOT NULL,
                                birthday text,
                                gender CHAR,
                                aadhar INTEGER
                                ); """

CREATE_GREETING_KEY = """ CREATE TABLE IF NOT EXISTS GREET_KEY(
                                data text NOT NULL PRIMARY KEY UNIQUE
                                ); """

UPDATE_GREETING_KEY = """ INSERT INTO GREET_KEY(data)
                          VALUES(?) """

CHECK_FOR_GREETING_KEY = """SELECT EXISTS (SELECT * FROM GREET_KEY WHERE data = ?);"""

CREATE_GREETING_RESPONCE = """ CREATE TABLE IF NOT EXISTS GREET_RESPONSE(
                            id integer PRIMARY KEY UNIQUE,
                            data text NOT NULL UNIQUE
                            ); """

CHECK_FOR_GREETING_RESPONSE = """SELECT * FROM GREET_RESPONSE ORDER BY RANDOM() LIMIT 1"""

UPDATE_GREETING_RESPONSE = """ INSERT INTO GREET_RESPONSE(id, data)
                               VALUES(?,?) """

GET_ROW_COUNT = 'SELECT COUNT(*) FROM {}'
TABLE_GREET_KEY = "GREET_KEY"
TABLE_GREET_RESPONSE = "GREET_RESPONSE"
TABLE_USER_SESSION = "USER_SESSION"

class DataFile:
    """ Data File Class to Store the Data and Retrieve"""


    def __init__(self):
        """Constructor for DataFile Initialize the Database"""
        location = Path(__file__).resolve().parent #Gets the Current Directory
        self.name = DATABASE
        self.path = location
        self.db = sql.connect(os.path.join(self.path , self.name))
        self.create_table(CREATE_USER_DETAILS_TABLE)
        self.create_table(CREATE_GREETING_KEY)
        self.create_table(CREATE_GREETING_RESPONCE)
        self.update_greeting()


    def checkDataFile(self):
        location = Path(__file__).resolve().parent #Gets the Current Directory
        safelocation = Path(__file__).resolve(self)
        print(location)
        print(safelocation)

    def update_greeting(self):
        for word in GREETINGS_KEYWORDS:
            data = ((word.lower()),)
            self.update_table(TABLE_GREET_KEY, data)
        for word in GREETINGS_RESPONCES:
            data = ((self.get_table_size(TABLE_GREET_RESPONSE) + 1), (word), )
            self.update_table(TABLE_GREET_RESPONSE, data)

    def create_table(self, table):
        """Create SQLite3 table of the given type if doesnt already exits"""
        if self.db is not None:
            cursor = self.db.cursor()
            cursor.execute(table)

    def get_table_size(self, table_name):
        """Gets the number of rows in the current table"""
        if self.db is not None:
            cursor = self.db.cursor()
            cursor.execute(GET_ROW_COUNT.format(table_name))
            count = cursor.fetchall()
            return count[0][0]

    def update_table(self, table_name, data):
        """Update the table with the given data"""

        if self.db is not None:
            cursor = self.db.cursor()
            try:
                if table_name is TABLE_GREET_KEY:
                    cursor.execute(UPDATE_GREETING_KEY, data)
                elif table_name is TABLE_GREET_RESPONSE:
                    cursor.execute(UPDATE_GREETING_RESPONSE, data)
                self.db.commit()
            except sql.Error as e:
                print(e)

    def check_for_greeting(self, input):
        """Check for greeting Key"""
        if self.db is not None:
            data = ((input.lower()), )
            return self.db.cursor().execute(CHECK_FOR_GREETING_KEY, data)

    def get_greeting_response(self):
        """Get the greeting response"""
        if self.db is not None:
            response = self.db.cursor().execute(CHECK_FOR_GREETING_RESPONSE).fetchone()
            return response[1]


    def disconnect_data(self):
        if self.db is not None:
            self.db.close()

    def check_for_user_session(self, key):
        if self.db is not None:
            return self.db.cursor().execute(CHECK_FOR_USER_SESSION, ((key),))

    def create_user_session(self, key):
        if self.db is not None:
            self.db.cursor().execute(UPDATE_USER_SESSION_TABLE, ((key), ))
