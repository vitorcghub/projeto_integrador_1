from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Escola
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_user import roles_required, UserManager

auth_escola = Blueprint('auth_escola', __name__)

@auth_escola.route('/cadastro_escola', methods=['GET', 'POST'])
@roles_required('Diretor(a)')
def school():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        cnpj = request.form.get('cnpj')

        school = Escola.query.filter_by(email=email).first()
        if school:
            flash('Este email já existe.', category='error')
        elif len(email) < 4:
            flash('O email deve conter mais que 3 caracteres.', category='error')
        elif len(nome) < 2:
            flash('O nome deve conter ao menos 1 caractere.', category='error')
        elif len(str(telefone)) not in range(10,12):
            flash('O telefone deve conter de 10 a 11 dígitos com o código de área.', category='error')
        elif len(str(cnpj)) != 14:
            flash('Você deve usar 14 dígitos para o CNPJ', category='error')
      
        return redirect(url_for('views.home_diretor')) 
    return render_template("cadastro_escola.html", school=current_user)