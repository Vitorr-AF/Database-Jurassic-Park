from database import SessionLocal
from models import Dinossauro
from crud_dinosauros import *
from datetime import date

db = SessionLocal()

# CREATE
novo = Dinossauro(
    nome="Blue",
    especie_id=1,
    recinto_id=2,
    peso=75,
    altura=1.8,
    data_nascimento=date(2018, 6, 12),
    sexo="F"
)

criado = criar_dinossauro(db, novo)
print("Criado:", criado.id)

# READ
for d in listar_dinossauros(db):
    print(d.id, d.nome)

# UPDATE
atualizar_peso(db, criado.id, 1600)

# DELETE
# deletar_dinossauro(db, criado.id)

db.close()
