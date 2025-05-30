from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_bcrypt import Bcrypt, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://brukernavn:passord@127.0.0.1/flask_kurs1'
app.config['SECRET_KEY'] = 'passord' #Passordet til MariaDB
# Lager en variabel for SQLalchemy
db = SQLAlchemy(app)

#Gjør at flask og log inn kan sammarbeide
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
 
#Bruker for å reloader bruker
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Lager tabell i SQL
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True) #unique=True betyr at det ikke kan være to brukernavn som er like
    password = db.Column(db.String(150), nullable=False)
 
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)], render_kw={"placeholder": "Username"}) #Setter inn brukernavn og krever at minst skal ha 3 karakterer
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=150)], render_kw={"placeholder": "Password"}) #Setter inn passord og krever at minst skal ha 8 karakterer
 
    submit = SubmitField('Login')
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() #Skjekker om bruker er i database
        print(user.password, form.password.data)
        if user:
            if  user.password == form.password.data: #Sjekker om passordet er korrekt
                login_user(user)
                return redirect(url_for('dashboard'))
 
    return render_template('login.html', form=form)
 
@app.route('/dashboard', methods=['GET', 'POST']) #Kommer til hovedskjerm, kun når man er logget inn
@login_required
def dashboard():
    return render_template('dashboard.html')
 
if __name__ == '__main__':
   app.run(debug=True)
