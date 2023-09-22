from flask import blueprints, request, jsonify
from Models.gun_type_model import GunsType, gun_type_schema, guns_type_schema, db

gun_type_routes = blueprints.Blueprint("gunsTipe", __name__)

#Metodos GET, POST, PUT, DELETE --------------------------- ELIAN ------------------------------