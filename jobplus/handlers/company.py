from flask import Blueprint
from flask import render_template
from jobplus.decorators import company_required

company = Blueprint('company',__name__, url_prefix='/company')

@company.route('/')
@company_required
def index():
    return render_template('company/index.html')
