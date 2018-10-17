from flask import Blueprint
from flask import render_template
from jobplus.decorators import user_required
from jobplus.forms import UserForm

user = Blueprint('user', __name__)

@user.route('/user')
@user_required
def index():
    form = UserForm()
    if form.validate_on_submit():
        form.user_data()
        flash('填写数据成功，跳转到首页!','success')
        return redirect(url_for('front.index'))
    return render_template('user/index.html',form=form)

