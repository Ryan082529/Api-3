from .. import ma
from marshmallow import fields, validate
from ..models.comment import Comment
from .user_schema import UserSchema
fields.Field.default_error_messages['required'] = {"errors": "Campo obrigatório."}

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        fields = ("id", "conteudo", "data_criacao", "mensagens_id", "autor")

    id = fields.Int(dump_only=True)
    conteudo = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    data_criacao = fields.DateTime(dump_only=True)
    mensagens_id = fields.Int(required=True, load_only=True)
    autor = fields.Nested(UserSchema, dump_only=True)