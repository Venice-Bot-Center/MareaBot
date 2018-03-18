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

    def set(self):
        return self.table.set({"last":self.last})

    def get(self):
        return self.table.get().last

    def updated(self, new):
        if self.last != new:
            self.last = new
            self.set()
            return AttributeError
        return False


class User:

    def __init__(self, id_user, firebase, hight=-400, flag=False):
        self.id = id_user
        self.db = firebase.db
        self.table = self.db.child("user")
        self.hight = hight
        self.flag = flag
        self.get()

    def set(self):
        """
        Set the User data into the firebase
        :return: dictionary with the imputted datas
        """
        return self.table.child(self.id).set({"hight": self.hight, "all": self.flag})

    def get(self):
        """
        Get the data of the user
        :return: enupla, hight and after flag
        """
        user = self.table.child(self.id).get()
        self.hight = user.hight
        self.flag = user.all
        return self.hight, self.flag

    def delete(self):
        """
        Delete the user
        """
        self.table.child(self.id).remove()

    def __lt__(self, other):
        """
        Sort by hight sort
        :param other: the other User
        :return: True if self if the smaller, False otherwise
        """
        return self.hight < other.hight
