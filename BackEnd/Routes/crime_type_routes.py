from flask import blueprints, request, jsonify
from Models.crime_type_model import CrimesType, crime_type_schema, crimes_type_schema, db

crime_type_routes = blueprints.Blueprint("crimesTipe", __name__)

#Metodos GET, POST, PUT, DELETE --------------------------- SAMUEL ------------------------------