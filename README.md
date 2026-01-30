# flask-api

## Setup

### Pré-requisitos
- Docker
- Docker Compose
- Kind (para desenvolvimento com Kubernetes local)
- Helm (para gerenciar charts Kubernetes)
- Kubectl (para interagir com clusters Kubernetes)

### Usando Docker Compose (Desenvolvimento Local)

#### Levantar os containers
```bash
make compose
```

### Usando Kubernetes com Kind (Desenvolvimento em Cluster)

#### Setup completo (cria cluster + instala dependências + app)
```bash
make dev
```

Isso vai executar:
1. `make setup-dev` - Cria cluster KIND, instala NGINX Ingress Controller e MongoDB via Helm
2. `make deploy-dev` - Build imagem Docker, carrega no cluster e aplica manifestos da app.

#### Apenas setup inicial (sem deploy)
```bash
make setup-dev
```

Cria o cluster KIND com:
- NGINX Ingress Controller para roteamento
- MongoDB via Helm chart

#### Deploy da aplicação no cluster
```bash
make deploy-dev
```

Constrói e deploya a aplicação nos manifestos Kubernetes

#### Remover cluster
```bash
make teardown-dev
```

#### Executar testes
```bash
make test
```

Pré-requisito:
Iniciar a venv

Executa:
- Bandit (análise de segurança)
- Black (formatação de código)
- Flake8 (linting)
- Pytest (testes unitários)

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

### Usando Makefile

Para conveniência, todos os comandos podem ser executados via Makefile:

| Comando | Descrição |
|---------|-----------|
| `make compose` | Sobe os containers com Docker Compose |
| `make setup-dev` | Configura cluster KIND com dependências |
| `make deploy-dev` | Faz build e deploy da app no KIND |
| `make dev` | Executa setup-dev + deploy-dev (completo) |
| `make teardown-dev` | Remove o cluster KIND |
| `make test` | Executa testes, linting e análise de segurança |



anotacoes gerais:
toda vez que lancar as maquinas tem que copiar a chave privada para o local ~/.ssh/id_rsa da maquina bastion

Depois vamos usar o Ansible Vault para gerenciar as credenciais de forma encriptada.

$ ansible-vault create vars.yaml
Você vai definir uma senha, que será usada para decriptar sempre que for visualizar ou editar o arquivo.


$ ansible-playbook -i hosts.ini playbook.yml --ask-vault-password

ansible-galaxy collection install community.mongodb

> Não consegui fazer o ansible funcionar, tambem tentei instalar ele na mao via script sh mas não deu certo mesmo assim. Desisti