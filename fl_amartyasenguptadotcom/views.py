from __future__ import with_statement
from fl_amartyasenguptadotcom import app
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
	render_template, flash, _app_ctx_stack
from datetime import datetime
import time

###################
# 1.  Why can't I change username and password?
# 2.  What is up with not being able to do db configurations properly?
###################


# Home

@app.route('/')
def index():
	return render_template('index.html')