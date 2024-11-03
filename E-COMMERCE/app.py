from flask import Flask
from flask_mail import Mail, Message
from functools import wraps
import secrets

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:4444@localhost:3306/E_COMMERCE"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'edu.notexxx@gmail.com'
app.config['MAIL_PASSWORD'] = 'tucs iyyt vbak hcyo'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'edu.notexxx@gmail.com'
app.config['SECRET_KEY'] = secrets.token_hex(16)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name = "E-commerce", template_mode='bootstrap3')
login_manager = LoginManager()
mail = Mail(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from controller import *
from models import *

if __name__ == '__main__':
    from admin import *
    app.run(debug=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        if not current_user.otp_verified:
            flash('Please verify your email address before accessing this page.', 'warning')
            return redirect(url_for('verify_otp', user_id=current_user.id))
        return f(*args, **kwargs)
    return decorated_function