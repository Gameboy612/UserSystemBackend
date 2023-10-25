# https://www.reddit.com/r/flask/comments/mbhqnm/use_sqlalchemy_database_from_another_file/
# https://stackoverflow.com/questions/37908767/table-roles-users-is-already-defined-for-this-metadata-instance
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()