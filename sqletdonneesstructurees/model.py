from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    pin = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Etudiant {self.nom}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user(username):
    return User.query.filter_by(username=username).first()


def init_db(app):
    with app.app_context():
        db.create_all()

def get_all_students():
    return Etudiant.query.all()

def add_student(nom, addr, pin):
    new_student = Etudiant(nom=nom, addr=addr, pin=pin)
    db.session.add(new_student)
    db.session.commit()

def update_student(nom, new_addr, new_pin):
    # Updating by name as per previous logic, though ID is better
    # Fetching the first match
    student = Etudiant.query.filter_by(nom=nom).first()
    if student:
        student.addr = new_addr
        student.pin = new_pin
        db.session.commit()
