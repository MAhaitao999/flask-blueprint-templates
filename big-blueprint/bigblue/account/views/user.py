from .. import account
from flask import render_template


@account.route('/hello')
def hello():
    return render_template('hello.html')