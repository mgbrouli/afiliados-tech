from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.database import Base
import datetime

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Colimn(Float)
    link_afiliado = Column(String)
    criado_em = Colimn(DateTime, default=datetime.datetime.utcnow)