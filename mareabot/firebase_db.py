import os

import pyrebase

API_KEY = os.environ["FBKEY"]
AUTHDOMAIN = os.environ["FBAUTH"]
DATABASEURL = os.environ["FBDATABASE"]
STORAGEBUCKET = os.environ["FBSTORAGE"]


class FirebaseDB:
    config = {
        "apiKey": API_KEY,
        "authDomain": AUTHDOMAIN,
        "databaseURL": DATABASEURL,
        "storageBucket": STORAGEBUCKET,
    }

    db = pyrebase.initialize_app(config).database()
