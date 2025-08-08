from .. import ma
from marshmallow import fields, validate
from ..models.user import User
fields.Field.default_error_messages['required'] = {"errors": "Campo obrigatório."}

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "nome", "email","senha", "perfil")
        

    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=2, max=80))
    email = fields.Email(required=True)
    senha = fields.Str(load_only=True, required=True)
    perfil = fields.Str()