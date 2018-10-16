from flask import Blueprint, render_template
from jobplus.models import Job, Company,User
from jobplus.forms import UserregisterForm,CompanyregisterForm,LoginForm
from flask import flash
from flask_login import login_user,logout_user,login_required
from flask import redirect,url_for


front = Blueprint('front',__name__)

@front.route('/')
def index():
    job = Job.query.all()
    company = Company.query.all()
    return render_template('index.html', job=job, company=company)

@front.route('/userregister',methods=['GET','POST'])
def userregister():
    form = UserregisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录!','success')
        return redirect(url_for('.login'))
    return render_template('userregister.html',form=form)

@front.route('/companyregister',methods=['GET','POST'])
def companyregister():
    form = CompanyregisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录!','success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html',form=form)

@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user,form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html',form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录','success')
    return redirect(url_for('.index'))
