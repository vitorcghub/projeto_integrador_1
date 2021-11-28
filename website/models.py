from . import db
#from flask_login import UserMixin
from flask_user import UserManager, UserMixin
from sqlalchemy.sql import func

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    telefone = db.Column(db.Integer)
    cpf_cnpj = db.Column(db.Integer, unique=True)
    rua = db.Column(db.String(150))
    bairro = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    estado = db.Column(db.String(2))
    cep = db.Column(db.Integer)
    senha = db.Column(db.String(150))
    email_confirmed_at = db.Column(db.DateTime())
    escola = db.relationship('Escola')
    recursos = db.relationship('Recursos')
    profissao = db.relationship('Profissao', secondary='profissao_usuario')

class Profissao(db.Model):
        __tablename__ = 'profissao'
        id = db.Column(db.Integer(), primary_key=True)
        nome = db.Column(db.String(50), unique=True)

class ProfissaoUsuario(db.Model):
        __tablename__ = 'profissao_usuario'
        id = db.Column(db.Integer(), primary_key=True)
        id_usuario = db.Column(db.Integer(), db.ForeignKey('usuario.id', ondelete='CASCADE'))
        id_profissao = db.Column(db.Integer(), db.ForeignKey('profissao.id', ondelete='CASCADE'))

class Escola(db.Model, UserMixin):
    __tablename__ = 'escola'
    id = db.Column(db.Integer, primary_key=True)
    ue = db.Column(db.Integer, unique=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    telefone = db.Column(db.Integer)
    rua = db.Column(db.String(150))
    bairro = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    estado = db.Column(db.String(2))
    cep = db.Column(db.Integer)
    cnpj = db.Column(db.Integer)
    diretor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Recursos(db.Model):
    __tablename__ = 'recursos'
    id = db.Column(db.Integer, primary_key=True)
    recurso = db.Column(db.String(200))
    materia = db.Column(db.String(150))
    periodo = db.Column(db.String(150))
    qtde = db.column(db.Integer)
    obs = db.Column(db.String(10000))
    recurso_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()




