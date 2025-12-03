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