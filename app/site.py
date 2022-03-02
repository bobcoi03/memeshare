from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import get_db
from app.auth import session

from app.generateMemes import GenerateMemes

bp = Blueprint('site', __name__, url_prefix='/')

@bp.route('/')
def home():

    try:
        if session['user_id'] is not None:

            print(session)
        
            return render_template('site/home.html')

    except KeyError:

        return redirect('/auth/login')

@bp.route('/random-memes')
def random():

	generate_memes = GenerateMemes()

	list_of_url_memes = generate_memes.generate_memes()

	print(list_of_url_memes[0])

	try:
		if session['user_id'] is not None:
			print(session)
			return render_template('site/random_memes.html', list_of_url_memes = list_of_url_memes)

	except KeyError:
		return redirect('/auth/login')




