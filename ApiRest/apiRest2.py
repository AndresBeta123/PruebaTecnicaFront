from flask import Flask, json, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Variable global para almacenar los datos procesados
processed_users = []

# Funciones para la extraccion de todos los usuarios
def preProces():
    try:
        # Limitar la solicitud a los primeros 10 contactos
        url = 'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts?limit=4'
        headers = {
            'Authorization': 'Basic SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Esto generará una excepción para códigos de estado HTTP 4xx/5xx
        users = response.json().get('items', [])
        
        global processed_users
        processed_users = []
        for user in users:
            user_id = user.get('id')
            nombre = user.get('lookupName')
            correo = get_email(user_id, headers)
            telefono = get_phone(user_id, headers)
            ciudad = get_city(user_id, headers)
            
            processed_user = {
                'id': user_id,
                'nombre': nombre,
                'correo': correo,
                'telefono': telefono,
                'ciudad': ciudad
            }
            processed_users.append(processed_user)
        
        return True
    
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log the error
        return False
    except Exception as err:
        print(f'Other error occurred: {err}')  # Log the error
        return False

#Funcion que trae el Correo de un usuario
def get_email(contact_id, headers):
    try:
        # Obtener el correo
        email_url = f'http://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{contact_id}/emails/0'
        email_response = requests.get(email_url, headers=headers)
        if email_response.status_code == 404:
            email = None
        else:
            email_response.raise_for_status()
            email = email_response.json().get('address', None)
        return email
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log the error
        return None, None, None
    except Exception as err:
        print(f'Other error occurred: {err}')  # Log the error
        return None, None, None  

#Funcion que trae el Telefono de un usuario
def get_phone(contact_id, headers):
    try:
        # Obtener el teléfono
        phone_url = f'http://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{contact_id}/phones/1'
        phone_response = requests.get(phone_url, headers=headers)
        if phone_response.status_code == 404:
            phone = None
        else:
            phone_response.raise_for_status()
            phone = phone_response.json().get('number', None)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log the error
        return None, None, None
    except Exception as err:
        print(f'Other error occurred: {err}')  # Log the error
        return None, None, None  

#Funcion que trae la Ciudad de un usuario
def get_city(contact_id, headers):
    try:
        # Obtener la ciudad
        contact_url = f'http://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{contact_id}'
        contact_response = requests.get(contact_url, headers=headers)
        contact_response.raise_for_status()
        contact_data = contact_response.json()
        city = contact_data.get('address', {}).get('city', None)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log the error
        return None, None, None
    except Exception as err:
        print(f'Other error occurred: {err}')  # Log the error
        return None, None, None     

#Esta ruta retorna lo almacenado en processed_users 
@app.route('/users', methods=['GET'])
def get_users():
    global processed_users
    if not processed_users:
        if not preProces():
            return jsonify({'error': 'Failed to load user data'}), 500
    # Asegurarse de que el JSON sea devuelto correctamente sin caracteres escapados
    return jsonify(processed_users)

#Esta ruta permite la creacion de un usuario solo recibe primer y segundo nombre en un json
@app.route('/create', methods=['POST'])
def post_user():
    url = 'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0',
    }
    
    data = request.get_json()
    payload = json.dumps(data)
    response = requests.post(url, headers=headers, data=payload)
    return jsonify(response.json()), response.status_code

#Esta ruta elimina un usuario solo recibe la id del usuario
@app.route('/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    user_id = data.get('id')
    
    if not user_id:
        return jsonify({"error": "User ID is required."}), 400
    
    url = f'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{user_id}'
    headers = {
        'Authorization': 'Basic SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0',
    }
    
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 200:
        return jsonify({"message": "User deleted successfully."}), 200
    else:
        return jsonify({"error": "Failed to delete user."}), response.status_code

#Esta ruta permite la actualizacion o modificacion de la informacion de un usuario, requiere de la id, el primer y segundo nombre y la ciudad
@app.route('/update', methods=['PATCH'])
def update_user():
    data = request.get_json()
    user_id = data.get('id')
    city = data.get('city')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    
    if not user_id:
        return jsonify({"error": "User ID is required."}), 400
    
    if not city:
        return jsonify({"error": "City is required."}), 400
    
    if not first_name:
        return jsonify({"error": "First name is required."}), 400
    
    if not last_name:
        return jsonify({"error": "Last name is required."}), 400
    
    url = f'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{user_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0',
    }
    
    payload = json.dumps({
        "address": {
            "city": city
        },
        "name": {
            "first": first_name,
            "last": last_name
        }
    })
    
    response = requests.patch(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return jsonify({"message": "User updated successfully."}), 200
    else:
        return jsonify({"error": "Failed to update user."}), response.status_code

#Esta ruta permite Hacer la busqueda de un usuario mediante el nombre no requiere de un nombre exacto trae todas las coincidencias 
@app.route('/search', methods=['GET'])
def search_user():
    lookup_name = request.args.get('lookupName')
    
    if not lookup_name:
        return jsonify({"error": "Lookup name is required."}), 400
    
    # Construir la URL para la búsqueda con el operador LIKE
    query = f"lookupName LIKE '%{lookup_name}%'"
    url = f"https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts?q={query}"
    
    headers = {
        'Authorization': 'Basic SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta una excepción para códigos de estado 4xx/5xx
        data = response.json()  # Si la respuesta es JSON, se convierte a un diccionario de Python
        return jsonify(data), response.status_code
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": str(http_err)}), response.status_code
    except Exception as err:
        return jsonify({"error": str(err)}), 500

#Esta ruta permite hacer la busqueda de un unico usuario mostrando su informacion mediante la id 
@app.route('/searchById/<int:contact_id>', methods=['GET'])
def get_userByID(contact_id):
    headers = {
        'Authorization': 'Basic SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0'
    }
    try:
        contact_url = f'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{contact_id}'
        contact_response = requests.get(contact_url, headers=headers)
        contact_response.raise_for_status()
        contact_data = contact_response.json()

        nombre = contact_data.get('lookupName')
        ciudad = contact_data.get('address', {}).get('city', None)

        email_url = f'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{contact_id}/emails/0'
        email_response = requests.get(email_url, headers=headers)
        email = email_response.json().get('address', None) if email_response.status_code != 404 else None

        phone_url = f'https://imaginecx--tst2.custhelp.com/services/rest/connect/v1.3/contacts/{contact_id}/phones/1'
        phone_response = requests.get(phone_url, headers=headers)
        phone = phone_response.json().get('number', None) if phone_response.status_code != 404 else None

        user_info = {
            'id': contact_id,
            'nombre': nombre,
            'ciudad': ciudad,
            'correo': email,
            'telefono': phone
        }
        return jsonify(user_info)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None


if __name__ == '__main__':
    # Cargar datos al iniciar la aplicación
    preProces()
    app.run(debug=True)
