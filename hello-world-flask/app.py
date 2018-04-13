from flask import  request, redirect, render_template, session, url_for

import flask

app = flask.Flask(__name__)
app.secret_key = 'change_me_plz'


@app.route('/', methods=['GET'])
def home_page():
    return flask.render_template('index.html', **{
        'subject': 'world',
    })
