from .. import admin
from flask import render_template


@admin.route('/fyz')
def fyz():
    return render_template('fyz.html')