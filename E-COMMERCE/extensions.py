from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from sqlalchemy.sql import func
from math import ceil
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, NumberRange
from app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, logout_user, login_required, login_user, current_user
from flask_mail import Mail