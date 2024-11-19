from flask import Blueprint, jsonify, render_template
import random
import socket
import json

main = Blueprint('main', __name__)


# Leer datos de pokeneas desde el archivo
def load_pokeneas():
    with open('pokeneas.txt', 'r') as file:
        return json.load(file)

pokeneas = load_pokeneas()

# Función para obtener el Container ID
def get_container_id():
    try:
        with open('/etc/hostname', 'r') as file:
            return file.read().strip()
    except Exception as e:
        return f"Error al obtener Container ID: {e}"

@main.route('/')
def home():
    return render_template('landing.html')

@main.route('/json')
def json_route():
    pokenea = random.choice(pokeneas)   # Selecciona un Pokenea al azar
    return jsonify({
        "id": pokenea["id"],
        "name": pokenea["name"],
        "height": pokenea["height"],
        "ability": pokenea["ability"],
        "container_id": pokenea["image"]
    })

@main.route('/image')
def image_route():
    pokenea = random.choice(pokeneas)
    container_id = pokenea["image"]
    return render_template('pokenea.html', pokenea=pokenea, container_id=container_id)
