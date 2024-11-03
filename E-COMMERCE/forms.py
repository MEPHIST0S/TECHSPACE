from extensions import *

class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long"),
        Regexp(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])',
               message="Password must contain at least one number, one lowercase, one uppercase letter and one special case!")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    submit = SubmitField('Sign Up')
    
class OTPVerificationForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired()])
    submit = SubmitField('Verify OTP')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send Message')
    
class ReviewForm(FlaskForm):
    review_text = TextAreaField('Your Review', validators=[DataRequired()])
    rating = IntegerField('Rating (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5)])
    submit = SubmitField('Submit Review')
    
class SubscribeForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = EmailField('Your Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Subscribe Now')