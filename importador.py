import json
from datetime import datetime, date
from sqlalchemy.exc import IntegrityError
from database import SessionLocal
from models import (
    Habitat, Recinto, Funcionario, Ingresso,
    Especie, Visitante, Dinossauro,
    FuncionarioRecinto, Compra, Incidente, Alimentacao
)


def importar_dados(caminho):
    db = SessionLocal()

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    try:
        # HABITATS
        for h in dados.get("habitats", []):
            if not db.query(Habitat).filter_by(nome=h["nome"]).first():
                db.add(Habitat(**h))

        # RECINTOS
        for r in dados.get("recintos", []):
            if not db.query(Recinto).filter_by(nome=r["nome"]).first():
                db.add(Recinto(**r))

        # FUNCIONARIOS
        for f in dados.get("funcionarios", []):
            if not db.query(Funcionario).filter_by(nome=f["nome"]).first():
                db.add(Funcionario(**f))

        # INGRESSOS
        for i in dados.get("ingressos", []):
            if not db.query(Ingresso).filter_by(
                tipo=i["tipo"],
                data_ingresso=date.fromisoformat(i["data_ingresso"])
            ).first():
                db.add(
                    Ingresso(
                        tipo=i["tipo"],
                        preco=i["preco"],
                        data_ingresso=date.fromisoformat(i["data_ingresso"])
                    )
                )

        db.commit()

        # ESPECIES
        for e in dados.get("especies", []):
            if db.query(Especie).filter_by(nome_pop=e["nome_pop"]).first():
                continue

            habitat = db.query(Habitat).filter_by(
                nome=e["habitat_nome"]
            ).first()

            db.add(
                Especie(
                    nome_pop=e["nome_pop"],
                    nome_sci=e["nome_sci"],
                    periodo=e.get("periodo"),
                    tipo=e.get("tipo"),
                    gene_sapo=e.get("gene_sapo", False),
                    numero_oficial=e.get("numero_oficial", 0),
                    habitat_id=habitat.id if habitat else None
                )
            )

        # VISITANTES
        for v in dados.get("visitantes", []):
            if db.query(Visitante).filter_by(nome=v["nome"]).first():
                continue

            ingresso = db.query(Ingresso).filter_by(
                tipo=v["ingresso_tipo"]
            ).first()

            db.add(
                Visitante(
                    nome=v["nome"],
                    idade=v.get("idade"),
                    ingresso_id=ingresso.id if ingresso else None
                )
            )

        db.commit()

        # DINOSSAUROS
        for d in dados.get("dinossauros", []):
            if d.get("nome") is not None:
                if db.query(Dinossauro).filter_by(nome=d["nome"]).first():
                    continue

            especie = db.query(Especie).filter_by(
                nome_pop=d["especie_nome"]
            ).first()

            recinto = db.query(Recinto).filter_by(
                nome=d["recinto_nome"]
            ).first()

            db.add(
                Dinossauro(
                    nome=d["nome"],
                    especie_id=especie.id if especie else None,
                    recinto_id=recinto.id if recinto else None,
                    data_nascimento=date.fromisoformat(d["data_nascimento"])
                    if d.get("data_nascimento") else None,
                    peso=d.get("peso"),
                    altura=d.get("altura"),
                    sexo=d.get("sexo", "F")
                )
            )

        db.commit()

        # FUNCIONARIO_RECINTO
        for fr in dados.get("funcionario_recinto", []):
            funcionario = db.query(Funcionario).filter_by(
                nome=fr["funcionario_nome"]
            ).first()

            recinto = db.query(Recinto).filter_by(
                nome=fr["recinto_nome"]
            ).first()

            if funcionario and recinto:
                existe = db.query(FuncionarioRecinto).filter_by(
                    funcionario_id=funcionario.id,
                    recinto_id=recinto.id
                ).first()

                if not existe:
                    db.add(
                        FuncionarioRecinto(
                            funcionario_id=funcionario.id,
                            recinto_id=recinto.id
                        )
                    )

        # COMPRAS
        for c in dados.get("compras", []):
            visitante = db.query(Visitante).filter_by(
                nome=c["visitante_nome"]
            ).first()

            ingresso = db.query(Ingresso).filter_by(
                tipo=c["ingresso_tipo"]
            ).first()

            if visitante and ingresso:
                db.add(
                    Compra(
                        visitante_id=visitante.id,
                        ingresso_id=ingresso.id,
                        data_compra=datetime.fromisoformat(
                            c["data_compra"]
                        )
                    )
                )

        # INCIDENTES
        for i in dados.get("incidentes", []):
            dino = db.query(Dinossauro).filter_by(
                nome=i.get("dino_nome")
            ).first()

            recinto = db.query(Recinto).filter_by(
                nome=i.get("recinto_nome")
            ).first()

            visitante = db.query(Visitante).filter_by(
                nome=i.get("visitante_nome")
            ).first()

            db.add(
                Incidente(
                    data=datetime.fromisoformat(i["data"]),
                    tipo=i.get("tipo"),
                    dino_id=dino.id if dino else None,
                    recinto_id=recinto.id if recinto else None,
                    visitante_id=visitante.id if visitante else None
                )
            )

        # ALIMENTACAO
        for a in dados.get("alimentacao", []):
            dino = db.query(Dinossauro).filter_by(
                nome=a["dino_nome"]
            ).first()

            if dino:
                db.add(
                    Alimentacao(
                        dino_id=dino.id,
                        data=datetime.fromisoformat(a["data"]),
                        alimento=a.get("alimento"),
                        quantidade_kg=a.get("quantidade_kg")
                    )
                )

        db.commit()
        print("✅ Importação concluída com sucesso!")

    except IntegrityError as e:
        db.rollback()
        print("❌ Erro de integridade:", e)

    finally:
        db.close()


if __name__ == "__main__":
    importar_dados("dados.json")