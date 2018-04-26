from flask import Flask, request, jsonify, make_response 
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
#from werkzeug.securit import generate_password_hash, check_password_hash
#import jwt
import datetime
from functools import wraps
from instance.config import  app_config
#render_template, flash, redirect, url_for, session, request, logging
#from dat import Companies
#from flask_mysqldb import MySQL
#from wtforms import Form, BooleanField, StringField, PasswordField, validators



app = Flask(__name__)
#app.config.from_pyfile('config.py')
#app.config['SECRET_KEY'] = 'Tthesecretkey'

@app.route('/login/<int:usre_id>', methods=['POST'])
def index(usre_id):
  return jsonify({'message':'we are here'})

@app.route('/user', methods=['GET'])
def creat_meal():
  return 'dd'




