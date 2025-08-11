from .. import ma
from marshmallow import fields, validate
from ..models.message import Message
from .comment_schema import CommentSchema
from .user_schema import UserSchema
fields.Field.default_error_messages['required'] = {"errors": "Campo obrigatório."}

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        fields = ("id", "conteudo", "data_criacao", "comments", "autor", "titulo")

    id = fields.Int(dump_only=True)
    conteudo  = fields.Str(required=True, validate=validate.Length(min=1, max=140))
    titulo = fields.Str(required=True, validate=validate.Length(min=1, max=140))
    data_criacao = fields.DateTime(dump_only=True)

    # Campo aninhado de comentários
    comments = fields.Nested(CommentSchema, many=True, dump_only=True)
    autor = fields.Nested(UserSchema, dump_only=True)