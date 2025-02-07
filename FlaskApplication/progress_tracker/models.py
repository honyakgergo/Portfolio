from progress_tracker import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    sessions = db.relationship('Session', backref='user', lazy=True)

    def __repr__(self):
        return f"User({self.username},{self.email})"


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    exercise_1 = db.Column(db.String(50), nullable=False)
    exercise_2 = db.Column(db.String(50), nullable=False)
    exercise_3 = db.Column(db.String(50), nullable=False)
    exercise_4 = db.Column(db.String(50), nullable=False)
    exercise_5 = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Session({self.title}, {self.user_id})"
