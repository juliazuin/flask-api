# flask-api

## Setup

### Pré-requisitos
- Docker
- Docker Compose

### Levante os containers
```bash
docker-compose up -d
```

### Parar os containers
```bash
docker-compose down
```

## API Endpoints

### GET - Listar usuários
```bash
curl http://localhost:5000/users
```

Com formatação JSON:
```bash
curl -s http://localhost:5000/users | jq .
```

### POST - Criar usuário
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"João","email":"joao@example.com"}' \
  http://localhost:5000/users
```

Com formatação JSON na resposta:
```bash
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"name":"Maria","email":"maria@example.com"}' \
  http://localhost:5000/users | jq .
```

## MongoDB

### Acessar MongoDB via mongosh
```bash
docker exec -it mongodb mongosh --username admin --password admin --authenticationDatabase admin
```

Dentro do shell, você pode usar:
```javascript
show dbs              // Listar todos os bancos
use usuarios          // Selecionar banco 'usuarios'
db.users.find()       // Listar todos os usuários
db.users.find().pretty()  // Listar com formatação
```

## Testes

### Rodando os testes
```bash
pytest tests/test_application.py -v
```

### Testes com mongomock
Os testes utilizam a biblioteca `mongomock` para simular o MongoDB em memória, sem precisar de um container MongoDB real rodando.

**Configuração:**
- `config.TestConfig`: Define a URI de teste com `mongodb://localhost/usuarios`
- `conftest.py`: Contém a fixture `app_with_mongomock` que substitui PyMongo real pelo mongomock
- `tests/test_application.py`: Testes que usam a fixture para testar as rotas

**Como funciona `app_with_mongomock`:**
1. Cria um cliente mongomock em memória
2. Faz patch do PyMongo para usar mongomock em vez de conectar ao MongoDB real
3. Fornece a app configurada para os testes
4. Todos os dados são armazenados em memória durante os testes

### Exemplo de teste
```python
def test_create_user(self, app):
    client = app.test_client()
    user_data = {"name": "John Doe", "email": "johndoe@example.com"}
    response = client.post('/users', json=user_data)
    assert response.status_code == 201
    assert response.get_json() == {"message": "User created successfully"}
```

Cada teste tem seu próprio banco de dados em memória isolado, garantindo que os testes não interferam uns com os outros.

Run Bandit:
```bash 
bandit -r . -x './venv','./tests/'
```