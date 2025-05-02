from flask import Flask  # Import Flask to create a web app
from flask_sqlalchemy import SQLAlchemy

# Set up the Flask app
app = Flask(__name__)

# Add database settings (replace 'brukernavn' and 'passord' with your actual username and password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://brukernavn:passord@127.0.0.1/users'  # Database connection info
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off extra tracking to save resources

# Connect the app to the database
db = SQLAlchemy(app)

# Define a User table for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(150), nullable=False, unique=True)  # Username must be unique and not empty

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()  # Set up the User table in the database
    print("Database table created!")  # Let the developer know the table was created

# Start the app in debug mode (useful for development)
if __name__ == '__main__':
    app.run(debug=True)  # Runs the app and shows errors if something breaks