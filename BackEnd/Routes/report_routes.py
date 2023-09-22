from flask import blueprints, request, jsonify
from Models.reports_model import Reportes, reportes_schema, reporte_schema, db

reports_routes = blueprints.Blueprint("reports", __name__)

#--------------------------------------------- REPORTES -----------------------------------------------

#-------GET-----------    
@reports_routes.route('/get', methods=['GET'])
def get_reportes():
    reportes = Reportes.query.all()
    return jsonify(reportes_schema.dump(reportes))

#-------POST-----------
@reports_routes.route('/post', methods=['POST'])
def create_reporte():
    try:
        data = request.get_json()
        db.session.add(Reportes(**data))
        db.session.commit()

        return reporte_schema.jsonify(Reportes(**data)), 201
    except Exception as e:
        return jsonify({"error": "Error al crear el reporte", "details": str(e)}), 400

#-------PUT-----------
@reports_routes.route('/put/<id>', methods=['PUT'])
def update_reporte(id):
    try:
        reporte = Reportes.query.get(id)
        if not reporte:
                return jsonify({"error": "Reporte no encontrado"}), 404

        data = request.json
            
        for k, v in data.items():
            setattr(reporte, k, v)

        db.session.commit()

        return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el usuario", "details": str(e)}), 500

#-------DELETE--------
@reports_routes.route('/delete/<id>', methods=['DELETE'])
def delete_reporte(id):
    try:
        reporte = Reportes.query.get(id)

        if not reporte:
            return jsonify({"error": "Reporte no encontrado"}), 404

        db.session.delete(reporte)
        db.session.commit()

        return jsonify({"mensaje": "Reporte eliminado correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el reporte", "details": str(e)}), 500
