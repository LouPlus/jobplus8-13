from flask import Blueprint, render_template
from jobplus.models import Job, Company

front = Blueprint('front',__name__,url_prefix='/')

@front.route('/')
def index():
    job = Job.query.all()
    company = Company.query.all()
    return render_template('index.html', job=job, company=company)

@front.route('/userregister')
def userregister():
    return 'userregister'
#后面几个路由都需要添加

@front.route('/companyregister')
def companyregister():
    return 'companyregister'

@front.route('/login')
def login():
    return  'login'

