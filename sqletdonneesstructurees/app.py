from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies, unset_jwt_cookies, verify_jwt_in_request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended.exceptions import NoAuthorizationError
from model import db, init_db, get_all_students, add_student, update_student, create_user, get_user
import os

app = Flask(__name__)
# Security configuration
app.config['SECRET_KEY'] = 'dev-secret-key' # For flash messages
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False # Simplified for exercise

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
jwt = JWTManager(app)

### Swagger Specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Student Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
### End Swagger Specific ###

# Helper to redirect to login if not authorized
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return redirect(url_for('login_page'), 302)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return redirect(url_for('login_page'), 302)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        
        if user and user.check_password(password):
            access_token = create_access_token(identity=username)
            resp = redirect(url_for('index'))
            set_access_cookies(resp, access_token)
            return resp
        else:
            flash('Invalid username or password')
            return render_template('login.html')
            
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    if get_user(username):
        flash('Username already exists')
        return redirect(url_for('login_page'))
        
    create_user(username, password)
    flash('Registration successful! Please login.')
    return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    resp = redirect(url_for('login_page'))
    unset_jwt_cookies(resp)
    return resp

@app.route('/')
@jwt_required()
def index():
    students = get_all_students()
    return render_template('index.html', students=students)

@app.route('/new', methods=['POST'])
@jwt_required()
def new_student():
    nom = request.form['nom']
    addr = request.form['addr']
    pin = request.form['pin']
    add_student(nom, addr, pin)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
@jwt_required()
def update_student_route():
    nom = request.form['nom']
    addr = request.form['addr']
    pin = request.form['pin']
    update_student(nom, addr, pin)
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
