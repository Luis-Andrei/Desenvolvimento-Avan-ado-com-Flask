# Daily Diet API

API para controle de dieta diária, permitindo o registro e gerenciamento de refeições.

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a API

Para iniciar o servidor, execute:
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Documentação

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Refeições

- `POST /api/v1/refeicoes/` - Criar uma nova refeição
- `GET /api/v1/refeicoes/` - Listar todas as refeições
- `GET /api/v1/refeicoes/{refeicao_id}` - Obter detalhes de uma refeição específica
- `PUT /api/v1/refeicoes/{refeicao_id}` - Atualizar uma refeição
- `DELETE /api/v1/refeicoes/{refeicao_id}` - Deletar uma refeição

## Exemplo de Uso

### Criar uma refeição
```json
{
    "nome": "Café da manhã",
    "descricao": "Pão integral com queijo e café",
    "data_hora": "2024-01-01T08:00:00",
    "dentro_da_dieta": true
}
``` 