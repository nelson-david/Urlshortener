from app import app, db
from app.models import Urls
from flask import render_template, jsonify, request, redirect, url_for

import secrets

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/process_url/", methods=['POST'])
def process_url():
	real_url = request.form['url_input']
	fake_url = secrets.token_hex(1)

	new_url = Urls(real_url=real_url, fake_url=fake_url)
	db.session.add(new_url)
	db.session.commit()

	return jsonify({'real_url':real_url, 'fake_url':f'http://127.0.0.1:8000/g/{fake_url}'})

@app.route('/g/<url>/')
def return_url(url):
	check_url = Urls.query.filter_by(fake_url=url).first()
	if check_url:
		return redirect(f'https://{check_url.real_url}')
	return redirect(url_for('home'))