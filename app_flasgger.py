from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f'Hello!'

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns the message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
      - name: lastname
        in: query
        type: string
        required: false
        default: no last name provided
      - name: birthday
        in: query
        type: string
        required: false
        default: no birthday provided
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'no last name provided')
    birthday = request.args.get('birthday', 'no birthdate provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()
    return jsonify({'message': f'Hello {nameCapital} {lastnameCapital}! Your birthday is {birthday}.'})

if __name__ == '__main__':
    app.run(debug=True)