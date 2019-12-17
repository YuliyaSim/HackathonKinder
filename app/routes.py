from flask import render_template, url_for
from flask_login import LoginManager, login_user,login_required,current_user
from werkzeug.utils import redirect

from app import app, db, login_manager
from app.models import User, Child, Activity
from app.forms import RegisterForm, AddChild, LoginForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        username=form.username.data,
                        email=form.email.data,
                        password=form.password.data,
                        address_street=form.address_street.data,
                        address_city=form.address_city.data,
                        address_country=form.address_country.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('profile',user_id=new_user.id))
    else:
        print(form.errors)
        print('Johnny boy')

    return render_template('registration.html', register_form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                print(user)
                return redirect(url_for('profile', user_id=user.id))
        return "<h1>Invalid username or password (I know that's you, Mel)</h1>"
    else:
        print(form.errors)
    return render_template('login.html', login_form=form)


@app.route('/dashboard')
def dashboard():
    children = Child.query.all()
    return render_template('dashboard.html',children=children)

@app.route('/activities')
def activities():
    activities = Activity.query.all()
    return render_template('activities.html', activities=activities)


@login_required
@app.route('/profile/<int:user_id>', methods=['GET', 'POST'])
def profile(user_id):
    children = Child.query.filter_by(user_id=user_id)
    return render_template('profile.html', children=children)


@app.route('/addchild', methods=['GET', 'POST'])
def addchild():

    form = AddChild()

    if form.validate_on_submit():
        new_child = Child(nickname=form.nickname.data,
                          age=form.age.data,
                          gender=form.gender.data,
                          language=form.language.data,
                          activity1=form.activity1.data,
                          activity2=form.activity2.data,
                          activity3=form.activity3.data,
                          user_id = current_user.id
                          )
        db.session.add(new_child)
        db.session.commit()
        return redirect(url_for('profile', user_id=new_child.user_id))
    else:
        print(form.errors)

    return render_template('add_child.html', child_form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')
