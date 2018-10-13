from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Base(db.Model):
	__abstract__ = True
	created_at = db.Column(db.DateTime,default=datetime.utcnow)
	updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)


user_job = db.Table(
	'user_job',
	db.Column('user_id',db.Integer,db.ForeignKey('user.id',ondelete='CASCADE')),
	db.Column('job_id',db.Integer,db.ForeignKey('job.id',ondelete='CASCADE'))
)

class User(Base,UserMixin):
	__tablename__ = 'user'
	
	#普通用户权限
	ROLE_USER = 10
	#企业用户权限
	ROLE_COMPANY = 20
	#管理员用户权限
	ROLE_ADMIN = 30 

	id = db.Column(db.Integer,primary_key=True)
		
	username = db.Column(db.String(32),unique=True, nullable=False)
	email = db.Column(db.String(64),unique=True,index=True,nullable=False)
	_password = db.Column('password',db.String(256),nullable=False)
	role = db.Column(db.SmallInteger,default=ROLE_USER)
	resume = db.Column(db.String(64))
#	resume = db.relationship('Resume',uselist=False)
	collect_jobs = db.relationship('Job',secondary=user_job)
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

	@property
	def is_admin(self):
		return self.role == self.ROLE_ADMIN

	@property
	def is_company(self):
		return self.role == self.ROLE_COMPANY

class Job(Base):
	__tablename__ = 'job'

	id = db.Column(db.Integer,primary_key=True)

	name = db.Column(db.String(21))
	salary_low = db.Column(db.Integer,nullable=False)
	salary_high = db.Column(db.Integer,nullable=False)
	location = db.Column(db.String(24))

	tags = db.Column(db.String(128))
	experience_requirement = db.Column(db.String(32))
	degree_requirement = db.Column(db.String(32))
	is_fulltime = db.Column(db.Boolean,default=True)

	is_open = db.Column(db.Boolean,default=True)
	company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='CASCADE'))
	company = db.relationship('Company',uselist=False)
	views_count = db.Column(db.Integer,default=0)

	def __repr__(self):
		return '<Job {}>'.format(self.name)

class Company(Base):
	__tablename__ = 'company'

	id = db.Column(db.Integer,primary_key=True)

	name = db.Column(db.String(64),nullable=False,index=True,unique=True)
	logo = db.Column(db.String(64),nullable=True)
	site = db.Column(db.String(64),nullable=False)
	contact =  db.Column(db.String(32),nullable=False)
	email = db.Column(db.String(64),nullable=False)
	location = db.Column(db.String(24),nullable=False)

	describe = db.Column(db.String(128),nullable=False)
	about = db.Column(db.String(1024))
	tags = db.Column(db.String(128))
	stack = db.Column(db.String(128))

	team_introduction = db.Column(db.String(256))
	welfares = db.Column(db.String(256))

	user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
	user = db.relationship('User',uselist=False,backref=db.backref('company',uselist=False))

	def __repr__(self):
		return '<Company {}>'.format(self.name)


class Dilivery(Base):
	__tablename__ = 'delivery'

	STATUS_WAITING = 1

	STATUS_REJECT = 2

	STATUS_ACCEPT = 3

	id = db.Column(db.Integer,primary_key=True)
	job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))

	status = db.Column(db.SmallInteger,default=STATUS_WAITING)
	response = db.Column(db.String(256))