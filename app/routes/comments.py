from flask import Blueprint, request
from ..schemas.comment_schema import CommentSchema
from ..controllers import comment_controller
from ..middlewares.message_required import mensagem_existe
from ..middlewares.comment_required import comentario_existe
from flask_jwt_extended import jwt_required, get_jwt_identity

comments_bp = Blueprint('comments', __name__)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

@comments_bp.route('/mensagens/<int:mensagens_id>/comentarios', methods=['GET'])
@mensagem_existe
@jwt_required()
def get_comments(mensagens_id):
    comments = comment_controller.listar_comentarios(mensagens_id)
    return comments_schema.jsonify(comments), 200

@comments_bp.route('/mensagens/<int:mensagens_id>/comentarios/<int:comment_id>', methods=['GET'])
@mensagem_existe
@comentario_existe
@jwt_required()
def get_comment(mensagens_id, comment_id):
    return comment_schema.jsonify(request.comentario), 200

@comments_bp.route('/mensagens/<int:mensagens_id>/comentarios', methods=['POST'])
@mensagem_existe
@jwt_required()
def create_comment(mensagens_id):
    data = request.get_json()
    print(data)
    data['mensagens_id'] = mensagens_id
    validated_data = comment_schema.load(data)
    user_id = get_jwt_identity()
    validated_data['user_id'] = user_id
    print(data) 
    comment = comment_controller.criar_comentario(validated_data)
    return comment_schema.jsonify(comment), 201

@comments_bp.route('/mensagens/<int:mensagens_id>/comentarios/<int:comment_id>', methods=['PUT'])
@mensagem_existe
@comentario_existe
@jwt_required()
def update_comment(mensagens_id, comment_id):
    data = request.get_json()
    data['mensagens_id'] = mensagens_id
    user_id = get_jwt_identity()
    if str(request.comentario.user_id) != str(user_id):
        return {"error": "Acesso negado."}, 403
    validated_data = comment_schema.load(data)
    updated = comment_controller.atualizar_comentario(request.comentario, validated_data)
    return comment_schema.jsonify(updated), 200

@comments_bp.route('/mensagens/<int:mensagens_id>/comentarios/<int:comment_id>', methods=['PATCH'])
@mensagem_existe
@comentario_existe
@jwt_required()
def partial_update_comment(mensagens_id, comment_id):
    data = request.get_json()
    validated_data = comment_schema.load(data, partial=True)
    updated = comment_controller.atualizar_comentario(request.comentario, validated_data)
    return comment_schema.jsonify(updated), 200

@comments_bp.route('/mensagens/<int:mensagens_id>/comentarios/<int:comment_id>', methods=['DELETE'])
@mensagem_existe
@comentario_existe
@jwt_required()
def delete_comment(mensagens_id, comment_id):
    comment_controller.deletar_comentario(request.comentario)
    return '', 204