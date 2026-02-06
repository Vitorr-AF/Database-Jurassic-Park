from sqlalchemy.orm import Session
from models import Dinossauro

def criar_dinossauro(db: Session, dino: Dinossauro):
    db.add(dino)
    db.commit()
    db.refresh(dino)
    return dino


def listar_dinossauros(db: Session):
    return db.query(Dinossauro).all()


def buscar_dinossauro(db: Session, dino_id: int):
    return db.query(Dinossauro).filter(Dinossauro.id == dino_id).first()


def atualizar_peso(db: Session, dino_id: int, novo_peso):
    dino = buscar_dinossauro(db, dino_id)
    if dino:
        dino.peso = novo_peso
        db.commit()
        db.refresh(dino)
    return dino


def deletar_dinossauro(db: Session, dino_id: int):
    dino = buscar_dinossauro(db, dino_id)
    if dino:
        db.delete(dino)
        db.commit()
        return True
    return False
