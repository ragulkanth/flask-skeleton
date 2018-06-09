from os import getenv 

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#for the mysql configuration
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("CONTACT_FORM_DB_URI") or 'sqlite:////tmp/contact_form.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#csrf config
app.config['CSRF_SECRET_KEY'] = b'rf5yQkNh00W54EgLBttbnsw8iiZmkk75nDPV'

#session initiated
SESSION_TYPE = 'sqlalchemy'
app.config.from_object(__name__)
Session(app)

#database is initiated
db = SQLAlchemy(app)

#importing the views
from views import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
