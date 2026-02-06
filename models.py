from sqlalchemy import (
    Column, Integer, String, Numeric, Date, Boolean,
    ForeignKey, CheckConstraint
)
from sqlalchemy.orm import relationship
from database import Base


class Especie(Base):
    __tablename__ = "especies"

    id = Column(Integer, primary_key=True)
    nome_pop = Column(String(100), nullable=False)
    nome_sci = Column(String(100), nullable=False)
    periodo = Column(String(50))
    tipo = Column(String(20))
    gene_sapo = Column(Boolean, default=False)
    numero_oficial = Column(Integer, default=0, nullable=False)

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
    nome = Column(String(100), nullable=False)
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
