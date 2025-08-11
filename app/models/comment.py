from datetime import datetime
from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    mensagens_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    mensagens = db.relationship('Message', backref=db.backref('comments', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "conteudo": self.conteudo,
            "data_criacao": self.data_criacao.isoformat(),
            "mensagens_id": self.mensagens_id
        }

