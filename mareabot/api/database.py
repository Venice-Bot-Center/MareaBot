# coding=utf-8

from flask.ext.sqlalchemy import SQLAlchemy

from mareabot.app import app
from mareabot.config import DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
db = SQLAlchemy(app)
