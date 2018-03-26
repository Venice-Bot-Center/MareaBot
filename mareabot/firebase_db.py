import os

import pyrebase

API_KEY = os.environ['FBKEY']
AUTHDOMAIN = os.environ['FBAUTH']
DATABASEURL = os.environ['FBDATABASE']
STORAGEBUCKET = os.environ['FBSTORAGE']


class FirebaseDB:
    config = {
        "apiKey": API_KEY,
        "authDomain": AUTHDOMAIN,
        "databaseURL": DATABASEURL,
        "storageBucket": STORAGEBUCKET
    }

    db = pyrebase.initialize_app(config).database()


class LastPrevision:
    def __init__(self, firebase):
        self.db = firebase.db
        self.table = self.db.child("prevision")
        self.last = self.get()

    def set(self,last):
        return self.table.set({"last":last})

    def get(self):
        return self.table.get()

    def updated(self, new):
        if self.last != new:
            self.last = new
            self.set(new)
            return AttributeError
        return False