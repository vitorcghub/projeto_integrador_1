from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager 
from flask_user import  UserManager


DB_NAME = "database.db"
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'univesp10'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USE_SSL'] = True
    # app.config['MAIL_USE_TLS'] = False
    # app.config['  db.create_all()USER_ENABLE_EMAIL'] = True
    # app.config['USER_ENABLE_USERNAME'] = False
    app.config['USER_EMAIL_SENDER_NAME'] = "Flask-User Basic App" 
    app.config['USER_EMAIL_SENDER_EMAIL'] = "noreply@example.com"

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    from .auth_usuario import auth_usuario
    from .auth_escola import auth_escola

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_usuario, url_prefix='/')
    app.register_blueprint(auth_escola, url_prefix='/' )

    from .models import Usuario, Escola, Recursos, Profissao, ProfissaoUsuario

    create_database(app)

    user_manager = UserManager(app, db, Usuario)
    login_manager = LoginManager()
    login_manager.login_view = 'auth_usuario.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Usuario.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):   
        db.create_all(app=app)
        print('Base de dados criada!')

