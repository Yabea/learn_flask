# coding:utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import Users, Role, Permissions
