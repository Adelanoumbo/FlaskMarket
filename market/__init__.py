from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
app = application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


from market import routes