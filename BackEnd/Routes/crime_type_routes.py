from flask import blueprints, request, jsonify
from Models.crime_type_model import CrimesType, crime_type_schema, crimes_type_schema, db

crime_type_routes = blueprints.Blueprint("crimesTipe", __name__)

#Metodos GET, POST, PUT, DELETE --------------------------- SAMUEL ------------------------------

#-------GET-----------    
@crime_type_routes.route('/get', methods=['GET'])
def get_crimes_type():
    crime_type = CrimesType.query.all()
    return jsonify(crimes_type_schema.dump(crime_type))

#-------POST-----------
@crime_type_routes.route('/post', methods=['POST'])
def create_crime_type():
    try:
        data = request.get_json()
        db.session.add(CrimesType(**data))
        db.session.commit()

        return crime_type_schema.jsonify(CrimesType(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el tipo de crimen", "details": str(e)}), 400

#-------PUT-----------
@crime_type_routes.route('/put/<id>', methods=['PUT'])
def update_crime_type(id):
    try:
        crime_type = CrimesType.query.get(id)
        if not crime_type:
                return jsonify({"error": "Tipo de crimen no encontrado"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(crime_type, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Tipo de crimen actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el tipo de crimen", "details": str(e)}), 500

#-------DELETE--------
@crime_type_routes.route('/delete/<id>', methods=['DELETE'])
def delete_crime_type(id):
    try:
        crime_type = CrimesType.query.get(id)

        if not crime_type:
            return jsonify({"error": "Tipo de crimen no encontrado"}), 404

        db.session.delete(crime_type)
        db.session.commit()

        return jsonify({"mensaje": "Tipo de crimen eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el tipo de crimen", "details": str(e)}), 500
