from .. import ma
from marshmallow import fields, validate
from ..models.comment import Comment
from .user_schema import UserSchema
fields.Field.default_error_messages['required'] = {"errors": "Campo obrigatório."}

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        fields = ("id", "content", "created_at", "message_id", "autor")

    id = fields.Int(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    created_at = fields.DateTime(dump_only=True)
    message_id = fields.Int(required=True, load_only=True)
    autor = fields.Nested(UserSchema, dump_only=True)