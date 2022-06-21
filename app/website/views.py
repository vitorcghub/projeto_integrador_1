from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from flask_user import roles_required, UserManager
#from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/home_diretor', methods=['GET', 'POST'])
@roles_required('Diretor(a)')
def home_diretor():
    # if request.method == 'POST':
    #     note = request.form.get('note')

    #     if len(note) < 1:
    #         flash('A nota está muito curta!', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Nota adicionada!', category='success')

    return render_template("home_diretor.html", user=current_user)

@views.route('/home_doadorprofessor', methods=['GET', 'POST'])
@roles_required('Doador(a)/Professor(a)')
def home_doadorprofessor():
    # if request.method == 'POST':
    #     note = request.form.get('note')

    #     if len(note) < 1:
    #         flash('A nota está muito curta!', category='error')
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)
    #         db.session.add(new_note)
    #         db.session.commit()
    #         flash('Nota adicionada!', category='success')

    return render_template("home_doadorprofessor.html", user=current_user)


# @views.route('/', methods=['GET', 'POST'])
# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')

#         if len(note) < 1:
#             flash('A nota está muito curta!', category='error')
#         else:
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('Nota adicionada!', category='success')

#     return render_template("home.html", user=current_user)


# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})