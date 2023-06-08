from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://application:Jagruthi35@jkvm1.mysql.database.azure.com:3306/students'
db = SQLAlchemy(app)

class students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    major = db.Column(db.String(50))
    phone = db.Column(db.String(50))

    def __repr__(self):
        return f"<students(name='{self.name}', email='{self.email}', major='{self.major}', phone='{self.phone}')>"

# Create the table
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        major = request.form['major']
        phone = request.form['phone']
        student = students(name=name, email=email, major=major, phone=phone)
        db.session.add(student)
        db.session.commit()
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

