from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)

#create secret key for cookies using secrets module secrets.token_hex(16)
app.config['SECRET_KEY'] = '5ae713ccef5009b0ef8174f6bdd01a1d'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/student_hub'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from app import routes