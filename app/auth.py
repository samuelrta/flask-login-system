from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_manager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
     return render_template('login.html') 

@auth.route('/login', methods=['POST'])
def login_post():
  
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    CPF_login = User.query.filter_by(cpf=email).first()
    PIS_login = User.query.filter_by(pis=email).first()

    alert = False
    
    if (not user and not CPF_login and not PIS_login):
        flash('Email, PIS, CPF invalidos.')
        alert = True
    if CPF_login:
        if not check_password_hash(CPF_login.password, password):
            flash('CPF invalido')
            alert = True
    if user:
        if not check_password_hash(user.password, password):
            flash('Senha invalido.')
            alert = True
    if PIS_login:
        if not check_password_hash(PIS_login.password, password):
            flash('Senha invalida.')
            alert = True

    if alert:
            return redirect(url_for('auth.login'))

    if user and not alert:
        login_user(user, remember=remember)
    if CPF_login and not alert:
        login_user(CPF_login, remember=remember)
    if PIS_login and not alert:
        login_user(PIS_login, remember=remember)

    return redirect(url_for('main.index'))


@auth.route('/signup')
def signup():
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    city = request.form.get('city')
    country = request.form.get('country')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')   
    street = request.form.get('street')
    number = request.form.get('number')
    complement = request.form.get('complement')
    cpf = request.form.get('cpf')
    pis = request.form.get('pis')
    password = request.form.get('password')
      

    user = User.query.filter_by(email=email).first() 

    if user: 
        flash ('E-mail já cadastrado')
        return redirect(url_for('auth.signup'))

    
    new_user = User(name=name, email=email, city=city, country=country, state=state, zip_code=zip_code, street=street, number=number, complement=complement, cpf=cpf, pis=pis, password=generate_password_hash(password, method='sha256'))

 
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()   
    return redirect(url_for('main.index'))
    


@auth.route('/profile', methods=['POST'])
def update():

    new_name = request.form.get('name')
    new_email = request.form.get('email')
    new_city= request.form.get('city')
    new_country = request.form.get('country')
    new_state= request.form.get('state')
    new_zip_code = request.form.get('zip_code')
    new_street = request.form.get('street')
    new_number = request.form.get('number')
    new_complement = request.form.get('complement')
    new_cpf = request.form.get('cpf')
    new_pis = request.form.get('pis')
    new_password = request.form.get('password')

    check_user = User.query.filter_by(email=new_email).first()
    check_CPF = User.query.filter_by(cpf=new_cpf).first()
    check_PIS = User.query.filter_by(pis=new_pis).first()

    alert = False

    if check_user:
        flash('Email utilizado por outra conta')
        alert = True

    if check_CPF:
        flash('CPF utilizado por outra conta')
        alert = True

    if check_PIS:
        flash('PIS utilizado por outra conta')
        alert = True

    if alert:
        return redirect(url_for('auth.update'))

    if new_name:
        current_user.name = new_name

    if new_email:
        current_user.email = new_email

    if new_city:
        current_user.city = new_city

    if new_country:
        current_user.country = new_country

    if new_state:
        current_user.state = new_state

    if new_zip_code:
        current_user.zip_code = new_zip_code

    if new_street:
        current_user.street = new_street

    if new_number:
        current_user.number = new_number

    if new_complement:
        current_user.complement = new_complement

    if new_cpf:
        current_user.cpf = new_cpf

    if new_pis:
        current_user.pis = new_pis

    if new_password:
        current_user.password = new_password=generate_password_hash(new_password, method='sha256')  

    db.session.commit()
   
    return redirect(url_for('main.index'))

