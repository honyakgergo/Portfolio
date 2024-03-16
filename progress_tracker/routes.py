from flask import redirect, url_for, render_template, request, flash, abort
from flask_login import login_user, current_user, login_required, logout_user
from progress_tracker import app, db, bcrypt
from progress_tracker.models import User, Session
from progress_tracker.data import test_exercises, test_users
from progress_tracker.forms import NewCourseForm, NewUserForm, LoginForm

with app.app_context():
    db.create_all()
    for test_user in test_users:
        hashed_pswd = bcrypt.generate_password_hash('alma24').decode('utf-8')
        user_obj = User(username=test_user['username'], email=test_user['email'], password=hashed_pswd)
        db.session.add(user_obj)
    for session in test_exercises:
        session_obj = Session(title=session['title'],
                              exercise_1=session['exercise_1'],
                              exercise_2=session['exercise_2'],
                              exercise_3=session['exercise_3'],
                              exercise_4=session['exercise_4'],
                              exercise_5=session['exercise_5'],
                              user_id=session['user_id'])
        db.session.add(session_obj)
    db.session.commit()
    print(Session.query.all())


@app.route('/')
@app.route('/home')
def home():
    return render_template('text.html', title='ProgressTracker')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/message_board')
def message_board():
    return render_template('message_board.html', title='Messages')


@app.route('/session/new', methods=["GET", "POST"])
@login_required
def create():
    form = NewCourseForm()
    if request.method == "POST":
        if form.validate_on_submit():
            current_session = Session(title=form.title.data,
                                      exercise_1=form.exercise_1.data,
                                      exercise_2=form.exercise_2.data,
                                      exercise_3=form.exercise_3.data,
                                      exercise_4=form.exercise_4.data,
                                      exercise_5=form.exercise_5.data,
                                      user_id=current_user.id)
            db.session.add(current_session)
            db.session.commit()
            flash('The given details of your session have been saved!', 'success')
            return redirect(url_for('sessions'))
    return render_template('create.html', title='New session', form=form)


@app.route('/session/<int:session_id>/update', methods=["GET", "POST"])
@login_required
def update_session(session_id):
    current_session = Session.query.get_or_404(session_id)
    if current_session.user != current_user:
        abort(403)
    form = NewCourseForm()
    if form.validate_on_submit():
        current_session.title = form.title.data
        current_session.exercise_1 = form.exercise_1.data
        current_session.exercise_2 = form.exercise_2.data
        current_session.exercise_3 = form.exercise_3.data
        current_session.exercise_4 = form.exercise_4.data
        current_session.exercise_5 = form.exercise_5.data
        db.session.commit()
        flash('It has been updated', 'success')
        return redirect(url_for('session', session_id=current_session.id))
    elif request.method == 'GET':
        form.title.data = current_session.title
        form.exercise_1.data = current_session.exercise_1
        form.exercise_2.data = current_session.exercise_2
        form.exercise_3.data = current_session.exercise_3
        form.exercise_4.data = current_session.exercise_4
        form.exercise_5.data = current_session.exercise_5
    return render_template('create.html', title='Update Session', form=form, legend='Update the session')


@app.route('/session/<int:session_id>/delete', methods=["POST"])
@login_required
def delete_session(session_id):
    current_session = Session.query.get_or_404(session_id)
    if current_session.user != current_user:
        abort(403)
    db.session.delete(current_session)
    db.session.commit()
    flash('This session has been deleted!', 'success')
    return redirect(url_for('sessions'))


@app.route('/register', methods=["GET", "POST"])
def register():
    form = NewUserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account is ready', 'success')
            print(User.query.all())
            return redirect(url_for('home'))
    return render_template('register.html', title='Create new account', form=form)


@app.route('/sessions')
def sessions():
    session_db = db.session.execute(db.select(Session)).scalars()
    return render_template('sessions.html', exercises=session_db, title='Sessions')


@app.route('/session/<int:session_id>')
def session(session_id):
    current_session = Session.query.get_or_404(session_id)
    all_sessions = [current_session]
    return render_template('session.html', title=current_session.title, exercise=current_session)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful!', 'danger')
    return render_template('login.html', title='Log in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Felhasználói fiók')