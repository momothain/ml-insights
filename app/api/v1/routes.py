from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/endpoint', methods=['GET'])
def endpoint():
    return {"message": "Hello, API!"}
