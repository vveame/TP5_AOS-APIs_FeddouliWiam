from flask import Blueprint, request, jsonify, abort
from service.filiere_service import FiliereService
from dto.request_filiere_dto import RequestFiliereDTO
from security.jwt_middleware import jwt_required

bp = Blueprint("filiere", __name__, url_prefix="/v1/filieres")

service = FiliereService()

@bp.route("/", methods=["GET"])
@jwt_required
def get_all_filieres():
    filieres = service.get_all()
    # Convert objects to dict for JSON serialization
    result = [f.__dict__ for f in filieres]
    return jsonify(result)

@bp.route("/", methods=["POST"])
@jwt_required
def add_filiere():
    data = request.json
    dto = RequestFiliereDTO(code=data.get("code"), libelle=data.get("libelle"))
    result = service.add_filiere(dto)
    return jsonify(result.__dict__), 200

@bp.route("/<int:id>", methods=["GET"])
@jwt_required
def get_filiere(id):
    res = service.get_by_id(id)
    if not res:
        abort(404, description="Filiere not found")
    return jsonify(res.__dict__)

@bp.route("/<int:id>", methods=["DELETE"])
@jwt_required
def delete_filiere(id):
    deleted = service.delete(id)
    if not deleted:
        abort(404, description="Filiere not found")
    return jsonify({"status": "deleted"})

@bp.route("/<int:id>", methods=["PUT"])
@jwt_required
def update_filiere(id):
    data = request.json
    dto = RequestFiliereDTO(code=data.get("code"), libelle=data.get("libelle"))
    res = service.update(id, dto)
    if not res:
        abort(404, description="Filiere not found")
    return jsonify(res.__dict__)