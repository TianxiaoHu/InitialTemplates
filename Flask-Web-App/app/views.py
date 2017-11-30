# -*- coding:utf-8 -*-
from app import app
from flask import render_template, jsonify, request, g, url_for
# from config import SQLALCHEMY_DATABASE_LOC, PAGINATION_PER_PAGE

### actions about db before and after request ###

# @app.before_request
# def before_request():
# 	g.conn = sqlite3.connect(SQLALCHEMY_DATABASE_LOC)
# 	g.cursor = g.conn.cursor()

# @app.teardown_request
# def teardown_request(exception):
# 	if hasattr(g, 'cursor'):
# 		g.cursor.close()
# 	if hasattr(g, 'conn'):
# 		g.conn.close()

### return html templates ###

@app.route('/')
def index():
	return render_template('index.html')
