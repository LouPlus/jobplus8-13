from flask import Blueprint
from flask import render_template
from jobplus.decorators import admin_required

admin = Blueprint('admin', __name__,url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

