from flask import jsonify, request, blueprints
from Models.users_model import Usuarios, usuarios_schema, usuario_schema, db

users_routes = blueprints.Blueprint("users", __name__)

#--------------------------------------------- USUARIOS -----------------------------------------------

#-------GET-----------
@users_routes.route('/get', methods=['GET'])
def get_usuarios():
    usuarios = Usuarios.query.all()
    return jsonify(usuarios_schema.dump(usuarios))

#-------POST-----------
@users_routes.route('/post', methods=['POST'])
def create_usuario():
    try:
        data = request.get_json()
        db.session.add(Usuarios(**data))
        db.session.commit()
        return usuario_schema.jsonify(Usuarios(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el usuario", "details": str(e)}), 400

#-------PUT-----------    
@users_routes.route('/put/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        usuario = Usuarios.query.get(id)
        if not usuario:
                return jsonify({"error": "Usuario no encontrado"}), 404

        data = request.get_json()

        for k, v in data.items():
            setattr(usuario, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el usuario", "details": str(e)}), 500

#-------DELETE--------
@users_routes.route('/delete/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuarios.query.get(id)

        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        db.session.delete(usuario)
        db.session.commit()

        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el usuario", "details": str(e)}), 500

