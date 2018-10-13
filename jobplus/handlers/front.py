from flask import Blueprint, render_template
from jobplus.models import Job, Company

front = Blueprint('front',__name__,url_prefix='/')

@front.route('/')
def index():
    job = Job.query.all()
    company = Company.query.all()
    return render_template('index.html', job=job, company=company)

