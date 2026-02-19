

# 🦖 Jurassic Park Database & Backend

Projeto de banco de dados relacional e backend em Python para simular
a gestão de um parque de dinossauros, inspirado no universo de Jurassic Park.

O projeto cobre desde a **modelagem do banco em PostgreSQL**
até um **CRUD utilizando SQLAlchemy ORM**.

---

## 🎯 Objetivo do Projeto

Criar um sistema capaz de gerenciar:

- Espécies de dinossauros
- Dinossauros individuais
- Recintos e habitats
- Funcionários e suas alocações
- Visitantes e ingressos
- Compras realizadas
- Alimentação dos dinossauros
- Incidentes ocorridos no parque

Tudo garantindo **integridade referencial** e **regras de negócio no banco**.

---

## 🛠️ Tecnologias Utilizadas

- **PostgreSQL**
- **Python 3.12**
- **SQLAlchemy (ORM)**
- **psycopg2**
- **python-dotenv**

---

## 🧠 Conceitos Aplicados

- Modelagem relacional
- Normalização de dados
- Relacionamentos 1:N e N:N
- Chaves primárias e estrangeiras
- Constraints (`CHECK`, `NOT NULL`)
- Regras de negócio no banco
- CRUD com ORM
- Variáveis de ambiente para configuração segura

---

## 📂 Estrutura do Projeto

```

jurassic-park-backend/
├─ sql/
│   └─ schema.sql
├─ database.py
├─ models.py
├─ crud_dinosauros.py
├─ main.py
├─ .env.example
├─ requirements.txt
└─ README.md

````

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/jurassic-park-backend.git
cd jurassic-park-backend
````

### 2️⃣ Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/jp_db
```

⚠️ O arquivo `.env` **não deve ser versionado**.

---

## ▶️ Executando o projeto

```bash
python main.py
```

O script realiza:

* criação de um dinossauro
* listagem dos dinossauros
* atualização de dados
* (opcional) exclusão

---

## 🧪 Exemplo de Código

```python
novo = Dinossauro(
    nome="Blue",
    especie_id=1,
    recinto_id=2,
    data_nascimento=date(2018, 6, 12),
    peso=75,
    altura=1.8,
    sexo="F"
)
```

## Comandos

### Resetar banco

```bash
python manage.py reset
```

### Importar dados

```bash
python manage.py seed dados.json
```

### Resetar e importar em sequência

```bash
python manage.py resetseed dados.json
```


---

## 📈 Próximos Passos

* Transformar o projeto em uma **API REST com FastAPI**
* Adicionar **Pydantic Schemas**
* Implementar **Alembic Migrations**
* Criar endpoints para visitantes, compras e incidentes
* Dockerizar o projeto
* Criar dados de Exemplo

---

## 👤 Autor

Desenvolvido por **Vitor Augusto**
📌 GitHub: [https://github.com/Vitorr-AF](https://github.com/Vitorr-AF)
