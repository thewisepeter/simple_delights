from flask import Flask
from flaskblog import db  # Import your Flask application and db object

# Set the database URI
database_uri = 'sqlite:///site.db'

# Create an instance of the Flask application
app = Flask(__name__)

# Set the database URI configuration option
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

# Initialize the Flask application with your database
db.init_app(app)

# Push the application context
app.app_context().push()

# Now you can execute db.create_all()
db.create_all()
