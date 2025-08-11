from flask import request, abort
from functools import wraps
from ..controllers import comment_controller

def comentario_existe(f):
    @wraps(f)
    def decorated_function(mensagens_id, comment_id, *args, **kwargs):
        comment = comment_controller.obter_comentario(comment_id)
        if comment is None or comment.mensagens_id != mensagens_id:
            abort(404, description="Comentário não encontrado para a mensagem informada.")
        request.comentario = comment
        return f(mensagens_id, comment_id, *args, **kwargs)
    return decorated_function