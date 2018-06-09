from flask import session
from wtforms import Form, PasswordField, validators
from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
from app import app 

class BaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = app.config['CSRF_SECRET_KEY']
        csrf_time_limit = timedelta(minutes=20)

        @property
        def csrf_context(self):
            return session

