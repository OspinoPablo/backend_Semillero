from flask import blueprints, request, jsonify
from Models.gun_type_model import GunsType, gun_type_schema, guns_type_schema, db

gun_type_routes = blueprints.Blueprint("gunsTipe", __name__)

#Metodos GET, POST, PUT, DELETE --------------------------- ELIAN ------------------------------
@gun_type_routes.route('/get', methods=['GET'])
def get_gun_type():
    guntype = GunsType.query.all()
    return jsonify(guns_type_schema.dump(guntype))

#-------POST-----------
@gun_type_routes.route('/post', methods=['POST'])
def create_gun_type():
    try:
        data = request.get_json()
        db.session.add(GunsType(**data))
        db.session.commit()

        return gun_type_schema.jsonify(GunsType(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el tipo de arma", "details": str(e)}), 400

#-------PUT-----------
@gun_type_routes.route('/put/<id>', methods=['PUT'])
def update_gun_type(id):
    try:
        gun_type = GunsType.query.get(id)
        if not gun_type:
                return jsonify({"error": "Tipo de arma no encontrado"}), 404

        dataa = request.json
            
        for k, v in dataa.items():
            setattr(gun_type, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Tipo de arma actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el Tipo de arma", "details": str(e)}), 500

#-------DELETE--------
@gun_type_routes.route('/delete/<id>', methods=['DELETE'])
def delete_gun_type(id):
    try:
        guntypee = GunsType.query.get(id)

        if not guntypee:
            return jsonify({"error": "Tipo de arma no encontrado"}), 404

        db.session.delete(guntypee)
        db.session.commit()

        return jsonify({"mensaje": "Tipo de arma eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el Tipo de arma", "details": str(e)}), 500
