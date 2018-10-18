from flask import Blueprint, flash
from flask import render_template,redirect,url_for
from jobplus.decorators import user_required
from jobplus.forms import UserForm
from flask_login import login_required, current_user

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/profile',methods=['POST','GET'])
@user_required
def index():
    form = UserForm()
    if form.validate_on_submit():
        form.user_data(current_user)
        flash('填写数据成功，跳转到首页!','success')
        return redirect(url_for('front.index'))
    return render_template('user/index.html',form=form)

