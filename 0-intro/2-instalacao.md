# Instalação do Python

## Ambiente Linux
- Se utilizará a ferramenta *uv* para o donwload e execução de código Python.
- Em razão de ambientes virtuais e dependências, é complexo o gerenciamento de projetos em Python.
- *uv* é gerenciador de pacote e projetos recentemente lançado, escrito em Rust.

- Download: 
```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Inicializar Projeto
```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Instalando Python
```bash
  uv python install 3.11
```

- Rodando Programa
```bash
  uv run script.py
```

- Criando um Ambiente Virtual para Execução
```bash
  uv venv
```
- Adicionando e Removendo Pacotes
```bash
  uv add pandas
  uv remove pandas
```