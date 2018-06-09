from datetime import datetime
from flask import request, render_template, flash, send_file

from app import app, db
from forms import *
from models import *

@app.route('/', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
