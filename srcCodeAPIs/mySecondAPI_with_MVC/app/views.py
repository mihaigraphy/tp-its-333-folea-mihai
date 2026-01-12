from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/')
def index():
    return "Simple API !"

### EXO2 - API with simple display
@app.route('/display')
def simple_display():
    return render_template('index.html')

### EXO3 - API with parameters display 
@app.route('/display_param')
def display_param():
    nom = "Mihai"
    return render_template('display_param.html', nom=nom) 

### EXO4 - API with parameters retrieved from URL 
