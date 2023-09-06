from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Reon@2002@5432/blinktrim'

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

from Project import routes
