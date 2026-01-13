from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

def get_patient_data(last_name):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "data.json")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for patient in data.get("patients", []):
            if patient.get("nom").lower() == last_name.lower():
                return patient
                
        return None
        
    except FileNotFoundError:
         return None

@app.route('/api/infopatients', methods=['GET'])
def info_patients():
    nom = request.args.get('nom')
    
    if not nom:
        return jsonify({"erreur": "Veuillez rentrez un 'nom'"}), 400
        
    patient = get_patient_data(nom)
    
    if patient:
        return jsonify(patient)
    else:
        return jsonify({"erreur": "Patient non trouver"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)

### commande pour tester :
### curl "http://localhost:5001/api/infopatients?nom=Dupont" 

