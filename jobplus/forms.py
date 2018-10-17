# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import (StringField,PasswordField,SubmitField,BooleanField,ValidationError)
from wtforms.validators import Length,Email,EqualTo,Required
from jobplus.models import db,User

class UserregisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24,message="密码在6-24之间")])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class CompanyregisterForm(FlaskForm):
    username = StringField('企业名称',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = StringField('密码',validators=[Required(),Length(6,24,message='密码在6-24之间')])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password =self.password.data
        db.session.add(user)
        db.session.commit()
        return user



class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱没有注册')
    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码不正确')

class UserForm(FlaskForm):
    name = StringField('姓名',validators=[Required(),Length(2,6)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    phonenumber = StringField('电话号码',validators=[Required(),Length(11,12)])
    workyear = StringField('工作年限',validators=[Required(),Length(0,70)])
    resume = StringField('上传简历')
    submit = SubmitField('提交')

    def user_data(self):
        user = User()
        user.name = self.user.data
       # user.email = slef.email.data
       # user.password = self.password.data
        user.phonenumber = self.phonenumber.data
       # user.workyear = self.workyear.data
        user.resume = self.resume.data


