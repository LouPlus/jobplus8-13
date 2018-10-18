from flask import Blueprint,render_template, flash, redirect,url_for, request
from flask_login import login_required, current_user
#from jobplus.forms import UserProfileForm

user = Blueprint('user', __name__, url_prefix='/user')

#@user.route('/profile',methods=)