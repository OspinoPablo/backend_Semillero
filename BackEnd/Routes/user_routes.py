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
def create_user():
    try:
        # Obtener los datos del request
        data = request.json

        # Crear un nuevo usuario con los datos del request
        new_user = Usuarios(
            correo=data['correo'],
            contrasena=data['contrasena'],
            usuario=data.get('usuario'),
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            telefono=data['telefono'],
            imagen_perfil=data.get('imagen_perfil')
        )

        # Añadir el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'Usuario creado exitosamente'}, 201

    except Exception as e:
        return {'error': str(e)}, 500


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

