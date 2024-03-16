from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from progress_tracker.models import User


class NewCourseForm(FlaskForm):
    title = StringField('Session Name', validators=[DataRequired(), Length(min=3, max=30)])
    exercise_1 = StringField('1.exercise', validators=[DataRequired(), Length(min=3, max=30)])
    exercise_2 = StringField('exercise_2', validators=[DataRequired(), Length(min=3, max=30)])
    exercise_3 = StringField('exercise_3', validators=[DataRequired(), Length(min=3, max=30)])
    exercise_4 = StringField('exercise_4', validators=[DataRequired(), Length(min=3, max=30)])
    exercise_5 = StringField('exercise_5', validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField('Save')


class NewUserForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail adress', validators=[DataRequired(), Email(message='The given e-mail address is '
                                                                                   'formally incorrect!')])
    password = PasswordField('Passqord', validators=[DataRequired()])
    confirm_password = PasswordField('Password again',
                                     validators=[DataRequired(), EqualTo('password', message='It does not match the '
                                                                                             'password entered above')
                                                 ])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already used. Try another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email adress is already used')


class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Keep me signed in')
    submit = SubmitField('Sign in')
