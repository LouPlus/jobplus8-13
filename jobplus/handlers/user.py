from flask import Blueprint
from flask import render_template
from jobplus.decorators import user_required

user = Blueprint('user', __name__,url_prefix='/user')

@user.route('/user')
@user_required
def index():
    return render_template('user/index.html')

