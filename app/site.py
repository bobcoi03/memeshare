from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import get_db
from app.auth import session

bp = Blueprint('site', __name__, url_prefix='/')

@bp.route('/')
def home():

    try:
        if session['user_id'] is not None:

            print(session)
        
            return render_template('site/home.html')

    except KeyError:

        return redirect('/auth/login')


