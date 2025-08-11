from datetime import datetime
from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(255), nullable=False)
    titulo = db.Column(db.String(45), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "conteudo": self.conteudo,
            "titulo": self.titulo,
            "data_criacao": self.data_criacao.isoformat()
        }