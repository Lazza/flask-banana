#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Main Banana web service.'''

from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/guestbook")
def guestbook():
    name = request.args.get('name')
    if name:
        message = 'Benvenuto {}!'.format(name)
        # TODO: inserire visita nel database
    else:
        message = 'Mmm... chi sei?'
    return render_template('guestbook.html', message=message)

@app.route('/favicon.ico')
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
