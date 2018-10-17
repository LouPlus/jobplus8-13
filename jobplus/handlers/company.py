from flask import Blueprint,render_template, flash, redirect,url_for, request
from flask_login import login_required, current_user
from jobplus.forms import CompanyProfileForm
from jobplus.models import User, Job, Company, Dilivery

company = Blueprint('company',__name__, url_prefix='/company')

@company.route('/')
def index():
	page = request.args.get('page',1,type=int)
	pagination = User.query.filter(
		User.role==User.ROLE_COMPANY
	).order_by(User.created_at.desc()).paginate(
		page=page,
		per_page=12,
		error_out=False
	)
	return render_template('company/index.html',pagination=pagination,active='company')

#@company.route('/profile', methods=['GET','POST'])