from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/')
def index():
    return jsonify({
        "message": "Simple API !"
    })
### curl -i -X GET http://localhost:5000/

### EXO2 - API with simple display
@app.route('/display')
def simple_display():
    return render_template('index.html')
### curl -i -X GET http://localhost:5000/display

### EXO3 - API with parameters display 
@app.route('/display_param')
def display_param():
    nom = "Mihai"
    return render_template('display_param.html', nom=nom) 
### curl -i -X GET http://localhost:5000/display_param

### EXO4 - API with parameters retrieved from URL 
@app.route('/display_param_url/<nom>')
def display_param_url(nom):
    return render_template('display_param_url.html', nom=nom)
### curl -i -X GET http://localhost:5000/display_param_url/Mihai
