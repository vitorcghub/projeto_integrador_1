from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Usuario, Profissao, ProfissaoUsuario
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_user import roles_required, UserManager
import datetime
 

auth_usuario = Blueprint('auth_usuario', __name__)


@auth_usuario.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        diretor = Usuario.query.filter_by(email=email).first()
        if diretor:
            if check_password_hash(diretor.senha, senha):
                flash('Usuário logado com sucesso!', category='success')
                login_user(diretor, remember=True)
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('Este email não existe.', category='error')
        
        return redirect(url_for('views.home_diretor'))
    return render_template("login.html", user=current_user)


@auth_usuario.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_usuarios.login'))


@auth_usuario.route('/cadastro_usuario', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        telefone = request.form.get('telefone')
        cpf_cnpj = request.form.get('cpf_cnpj')
        profissao = request.form.get('profissao')

        user = Usuario.query.filter_by(email=email).first()
        if user:
            flash('Este email já existe.', category='error')
        #elif profissao != 'Diretor(a)' or profissao != 'Doador(a)/Professor(a)':
         #   flash('Escolha uma das opções válidas, digitando-as corretamente', category='error')
        elif len(email) < 4:
            flash('O email deve conter mais que 3 caracteres.', category='error')
        elif len(nome) < 2:
            flash('O primeiro nome deve conter ao menos 1 caractere.', category='error')
        elif len(str(telefone)) not in range(10,12):
            flash('Seu telefone deve conter de 10 a 11 dígitos com o código de área.')
        elif len(str(cpf_cnpj)) != 11: #or len(str(cpf_cnpj)) != 14:
            flash('Você deve usar 11 dígitos para CPF ou 14 dígitos para CNPJ')
        elif senha1 != senha2:
            flash('As senhas devem ser iguais.', category='error')
        elif len(senha1) < 7:
            flash('A senha deve ter ao menos 6 caracteres.', category='error')
        else:
            if profissao == 'Diretor(a)':
                check_profissao = Profissao.query.filter_by(nome=profissao).first()
                if check_profissao:
                    diretor = Usuario(email=email, nome=nome, email_confirmed_at=datetime.datetime.utcnow(),
                    senha=generate_password_hash(senha1, method='sha256'))
                    db.session.add(diretor)
                    db.session.commit()
                else:
                    diretor = Usuario(email=email, nome=nome, email_confirmed_at=datetime.datetime.utcnow(),
                    senha=generate_password_hash(senha1, method='sha256'))
                    diretor.profissao.append(Profissao(nome=profissao))
                    db.session.add(diretor)
                    db.session.commit()
                login_user(diretor, remember=True)
                flash('Conta criada, Diretor(a)!', category='success')
                return redirect(url_for('auth_escola.school'))
            elif profissao == 'Doador(a)/Professor(a)':
                check_profissao = Profissao.query.filter_by(nome=profissao).first()
                if check_profissao:
                    doador_professor = Usuario(email=email, nome=nome, email_confirmed_at=datetime.datetime.utcnow(),
                    senha=generate_password_hash(senha1, method='sha256'))
                    db.session.add(doador_professor)
                    db.session.commit()
                else:
                    doador_professor = Usuario(email=email, nome=nome, email_confirmed_at=datetime.datetime.utcnow(),
                    senha=generate_password_hash(senha1, method='sha256'))
                    doador_professor.profissao.append(Profissao(nome='Doador(a)/Professor(a)'))
                    db.session.add(doador_professor)
                    db.session.commit()
                login_user(doador_professor, remember=True)
                flash('Conta criada, Doador(a)/Professor(a)', category='success')
                return redirect(url_for('views.home_doadorprofessor')) 
            else:
                flash('Escolha uma das opções válidas, digitando-as corretamente', category='error')

    return render_template("cadastro_usuario.html", user=current_user)

