from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Add this import

app = Flask(__name__)

# Configure the PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Reon%402002@localhost:5432/blinktrim'


# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)  # Add this line

from Project import routes
