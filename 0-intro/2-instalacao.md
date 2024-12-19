# Como Instalar o Python no Windows e no Linux

## Instalação no Windows

- Baixar o Instalador:

1. Acesse o site oficial do Python: python.org.
2. Baixe a versão mais recente do Python compatível com seu sistema operacional.
2. Executar o Instalador:
   - Dê um duplo clique no arquivo .exe baixado.
   - Certifique-se de marcar a opção "Add Python to PATH" na primeira tela.
   - Configuração e Instalação:
     - Escolha Install Now para uma instalação padrão ou Customize Installation para opções avançadas.
     - Aguarde a instalação ser concluída.
4. Verificar a Instalação:
- Abra o Prompt de Comando (cmd) e digite:
```bash
python --version
```
- Isso exibirá a versão instalada do Python.

## Instalação no Linux
- Verificar o Python Instalado:
  - Muitas distribuições Linux já vêm com o Python pré-instalado. Para verificar:
```bash
python3 --version
```
- Instalar via Gerenciador de Pacotes:

- Para distribuições baseadas em Debian/Ubuntu:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
- Para distribuições baseadas em Fedora:
```bash
sudo dnf install python3
```
- Para distribuições baseadas em Arch Linux:
```bash
sudo pacman -S python
```
- Verificar a Instalação:
Execute o comando:
```bash
python3 --version
```
- Isso exibirá a versão instalada.

### Configurar Virtual Environment (opcional):
- Instale o venv para gerenciar ambientes virtuais:
```bash
sudo apt install python3-venv
```
- Criação e ativação dos ambientes virtuais.
```bash
# cria o ambiente virtual
python -m venv nome_do_ambiente

# aciona o ambiente
.\nome_do_ambiente\Scripts\Activate # PowerShell
source nome_do_ambiente/bin/activate # Unix
```

- Caso tenha um erro no Windos:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
```
