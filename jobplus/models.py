from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

#
class Base(db.Model):
	__abstract__ = True
	created_at = db.Column(db.DateTime,default=datetime.utcnow)
	updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

#关联 user表与job表
user_job = db.Table(
	'user_job',
	db.Column('user_id',db.Integer,db.ForeignKey('user.id',ondelete='CASCADE')),
	db.Column('job_id',db.Integer,db.ForeignKey('job.id',ondelete='CASCADE'))
)


#用户表
class User(Base,UserMixin):
	__tablename__ = 'user'
	
	#普通用户权限
	ROLE_USER = 10
	#企业用户权限
	ROLE_COMPANY = 20
	#管理员用户权限
	ROLE_ADMIN = 30 

	id = db.Column(db.Integer,primary_key=True)
	#用户名	
	username = db.Column(db.String(32),unique=True, nullable=False)
	#邮箱
	email = db.Column(db.String(64),unique=True,index=True,nullable=False)
	#密码
	_password = db.Column('password',db.String(256),nullable=False)
	#角色
	role = db.Column(db.SmallInteger,default=ROLE_USER)
	#简历 （连接地址）
	resume = db.Column(db.String(64))
#	resume = db.relationship('Resume',uselist=False)
	#关联 user与job的关联 （与上边的关联表对应） 
	collect_jobs = db.relationship('Job',secondary=user_job)
	#
	uoload_resume_url = db.Column(db.String(64))	

	def __repr__(self):
		return '<User:{}>'.format(self.name)

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, orig_password):
		self._password = generate_password_hash(orig_password)

	def check_password(self, password):
		return check_password_hash(self._password, password)
    #判断是不是管理员
	@property
	def is_admin(self):
		return self.role == self.ROLE_ADMIN
    #判断是不是企业用户
	@property
	def is_company(self):
		return self.role == self.ROLE_COMPANY

#职位表
class Job(Base):
	__tablename__ = 'job'

	id = db.Column(db.Integer,primary_key=True)
    #职位名称
	name = db.Column(db.String(21))
	#工资最低
	salary_low = db.Column(db.Integer,nullable=False)
	#工资最高
	salary_high = db.Column(db.Integer,nullable=False)
	#职位地址 在什么地方工作
	location = db.Column(db.String(24))
    #职位标签
	tags = db.Column(db.String(128))
	#工作年限要求
	experience_requirement = db.Column(db.String(32))
	#学历要求
	degree_requirement = db.Column(db.String(32))
	#全职还是兼职
	is_fulltime = db.Column(db.Boolean,default=True)
   	#岗位是否在招牌 
	is_open = db.Column(db.Boolean,default=True)
	#公司的ID
	company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='CASCADE'))
	#对应的公司
	company = db.relationship('Company',uselist=False)
	#查看次数
	views_count = db.Column(db.Integer,default=0)

	def __repr__(self):
		return '<Job {}>'.format(self.name)

#企业表
class Company(Base):
	__tablename__ = 'company'

	id = db.Column(db.Integer,primary_key=True)
    #企业名称
	name = db.Column(db.String(64),nullable=False,index=True,unique=True)
	#企业logo
	logo = db.Column(db.String(64),nullable=True)
	#企业网址
	site = db.Column(db.String(64),nullable=False)
	#联系方式
	contact =  db.Column(db.String(32),nullable=False)
	#邮箱
	email = db.Column(db.String(64),nullable=False)
	#地理位置
	location = db.Column(db.String(24),nullable=False)
    #一句话描述
	describe = db.Column(db.String(128),nullable=False)
	#详细介绍
	about = db.Column(db.String(1024))
	#公司标签
	tags = db.Column(db.String(128))
	#公司技术栈
	stack = db.Column(db.String(128))
    
    #公司团队
	team_introduction = db.Column(db.String(256))
	#公司福利
	welfares = db.Column(db.String(256))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
	user = db.relationship('User',uselist=False,backref=db.backref('company',uselist=False))

	def __repr__(self):
		return '<Company {}>'.format(self.name)

#企业投递管理表
class Dilivery(Base):
	__tablename__ = 'delivery'
    
    #等待企业审核
	STATUS_WAITING = 1
    #被拒绝
	STATUS_REJECT = 2
    #已接受 等待面试
	STATUS_ACCEPT = 3

	id = db.Column(db.Integer,primary_key=True)
	
	job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    
    #状态信息
	status = db.Column(db.SmallInteger,default=STATUS_WAITING)
	#企业的回应
	response = db.Column(db.String(256))
