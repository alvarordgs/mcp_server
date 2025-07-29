.PHONY: run dev install test clean

# Rodar o projeto em modo desenvolvimento
dev:
	poetry run uvicorn src.mcp_server.main:app --reload

# Rodar o projeto em modo produção
run:
	poetry run uvicorn src.mcp_server.main:app --host 0.0.0.0 --port 8000

# Instalar dependências
install:
	poetry install

# Rodar testes
test:
	poetry run pytest

# Limpar cache
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete 