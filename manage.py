import sys
import json
from sqlalchemy import text
from database import engine
from importador import importar_dados


def reset_db():
    with engine.connect() as conn:
        conn.execute(text("""
            TRUNCATE TABLE
                alimentacao,
                incidentes,
                compras,
                funcionario_recinto,
                dinosauros,
                visitantes,
                especies,
                ingressos,
                funcionarios,
                recintos,
                habitats
            RESTART IDENTITY CASCADE;
        """))
        conn.commit()

    print("Banco resetado com sucesso!")


def seed_db(arquivo):
    importar_dados(arquivo)
    print("Seed concluído!")


def reset_and_seed(arquivo):
    reset_db()
    seed_db(arquivo)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python manage.py reset")
        print("  python manage.py seed dados.json")
        print("  python manage.py resetseed dados.json")
        sys.exit(1)

    comando = sys.argv[1]

    if comando == "reset":
        reset_db()

    elif comando == "seed":
        if len(sys.argv) < 3:
            print("Informe o arquivo JSON.")
            sys.exit(1)
        seed_db(sys.argv[2])

    elif comando == "resetseed":
        if len(sys.argv) < 3:
            print("Informe o arquivo JSON.")
            sys.exit(1)
        reset_and_seed(sys.argv[2])

    else:
        print("Comando inválido.")