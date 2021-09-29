from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile(): 
    return render_template('profile.html', id=current_user.id, name=current_user.name, email = current_user.email, city = current_user.city, country = current_user.country, state = current_user.state, zip_code = current_user.zip_code, street = current_user.street, number = current_user.number, complement = current_user.complement, cpf = current_user.cpf, pis = current_user.pis, password = current_user.password) 
    
