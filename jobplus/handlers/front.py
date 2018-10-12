from flask import Blueprint
from jobplus.models import *

front = Blueprint('front',__name__)

@front.route('/')
def index():
	pass