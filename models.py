from sqlalchemy import (
    Column, Integer, String, Numeric, Date, Boolean,
    ForeignKey, CheckConstraint, DateTime, Text
)
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Habitat(Base):
    __tablename__ = "habitats"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    clima = Column(String(50))
    continente = Column(String(50))
    descricao = Column(String)

    especies = relationship("Especie", back_populates="habitat")


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cargo = Column(String(50))

    recintos = relationship(
        "FuncionarioRecinto",
        back_populates="funcionario"
    )


class Ingresso(Base):
    __tablename__ = "ingressos"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(20))
    preco = Column(Numeric(8, 2))
    data_ingresso = Column(Date, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "tipo IN ('normal','vip','premium')",
            name="ingressos_tipo_check"
        ),
    )

    visitantes = relationship("Visitante", back_populates="ingresso")


class Visitante(Base):
    __tablename__ = "visitantes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer)
    ingresso_id = Column(Integer, ForeignKey("ingressos.id"))

    ingresso = relationship("Ingresso", back_populates="visitantes")
    compras = relationship("Compra", back_populates="visitante")
    incidentes = relationship("Incidente", back_populates="visitante")


class FuncionarioRecinto(Base):
    __tablename__ = "funcionario_recinto"

    funcionario_id = Column(
        Integer,
        ForeignKey("funcionarios.id"),
        primary_key=True
    )
    recinto_id = Column(
        Integer,
        ForeignKey("recintos.id"),
        primary_key=True
    )

    funcionario = relationship("Funcionario", back_populates="recintos")
    recinto = relationship("Recinto", backref="funcionarios")


class Compra(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True)
    visitante_id = Column(Integer, ForeignKey("visitantes.id"))
    ingresso_id = Column(Integer, ForeignKey("ingressos.id"))
    data_compra = Column(DateTime, default=datetime.utcnow, nullable=False)

    visitante = relationship("Visitante", back_populates="compras")
    ingresso = relationship("Ingresso")


class Incidente(Base):
    __tablename__ = "incidentes"

    id = Column(Integer, primary_key=True)
    data = Column(DateTime, nullable=False)
    tipo = Column(String(50))
    dino_id = Column(Integer, ForeignKey("dinosauros.id"))
    recinto_id = Column(Integer, ForeignKey("recintos.id"))
    visitante_id = Column(Integer, ForeignKey("visitantes.id"))

    dinossauro = relationship("Dinossauro")
    recinto = relationship("Recinto")
    visitante = relationship("Visitante", back_populates="incidentes")


class Alimentacao(Base):
    __tablename__ = "alimentacao"

    id = Column(Integer, primary_key=True)
    dino_id = Column(Integer, ForeignKey("dinosauros.id"))
    data = Column(DateTime, nullable=False)
    alimento = Column(String(100))
    quantidade_kg = Column(Numeric(8, 2))

    dinossauro = relationship("Dinossauro")


class Especie(Base):
    __tablename__ = "especies"

    id = Column(Integer, primary_key=True)
    nome_pop = Column(String(100), nullable=False)
    nome_sci = Column(String(100), nullable=False)
    periodo = Column(String(50))
    tipo = Column(String(20))
    gene_sapo = Column(Boolean, default=False)
    numero_oficial = Column(Integer, default=0, nullable=False)

    habitat_id = Column(Integer, ForeignKey("habitats.id"))

    habitat = relationship("Habitat", back_populates="especies")
    dinosauros = relationship("Dinossauro", back_populates="especie")

    __table_args__ = (
        CheckConstraint(
            "tipo IN ('carnivoro', 'herbivoro', 'onivoro')",
            name="especies_tipo_check"
        ),
    )


class Recinto(Base):
    __tablename__ = "recintos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    area = Column(Numeric(10, 2))
    capacidade = Column(Integer)
    clima_controlado = Column(Boolean, default=False)
    nivel_seguranca = Column(Integer, default=3)

    dinosauros = relationship("Dinossauro", back_populates="recinto")

    __table_args__ = (
        CheckConstraint(
            "nivel_seguranca BETWEEN 1 AND 5",
            name="recintos_nivel_seguranca_check"
        ),
    )


class Dinossauro(Base):
    __tablename__ = "dinosauros"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=True)
    especie_id = Column(Integer, ForeignKey("especies.id"))
    recinto_id = Column(Integer, ForeignKey("recintos.id"))
    data_nascimento = Column(Date)
    peso = Column(Numeric(8, 2))
    altura = Column(Numeric(6, 2))
    sexo = Column(String(1), nullable=False)

    especie = relationship("Especie", back_populates="dinosauros")
    recinto = relationship("Recinto", back_populates="dinosauros")

    __table_args__ = (
        CheckConstraint("sexo IN ('F','M')", name="dinosauros_sexo_check"),
    )
