from .. import admin
from flask import render_template


@admin.route('/mht')
def mht():
    return render_template('mht.html')
