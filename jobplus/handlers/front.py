from flask import Blueprint, render_template
from jobplus.models import Job, Company
from jobplus.forms import UserregisterForm,CompanyregisterForm,LoginForm

front = Blueprint('front',__name__)

@front.route('/')
def index():
    job = Job.query.all()
    company = Company.query.all()
    return render_template('index.html', job=job, company=company)

@front.route('/userregister')
def userregister():
    form = UserregisterForm()
    return render_template('userregister.html',form=form)

@front.route('/companyregister')
def companyregister():
    form = CompanyregisterForm()
    return render_template('companyregister.html',form=form)

@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)


