from database import SessionLocal
from models import Dinossauro
from crud_dinosauros import *

db = SessionLocal()

# CREATE
novo = Dinossauro(
    nome="Blue",
    especie_id=1,
    recinto_id=2,
    peso=1500,
    altura=3.2,
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
