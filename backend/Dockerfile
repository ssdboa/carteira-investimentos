# backend/Dockerfile

# PASSO 1: Escolher a imagem base
# Começamos com uma imagem oficial do Python, versão 3.12, em sua variante "slim",
# que é otimizada e tem um tamanho menor.
FROM python:3.12-slim

# PASSO 2: Configurar variáveis de ambiente
# Boas práticas para rodar Python no Docker:
# 1. Impede o Python de criar arquivos .pyc (otimização de bytecode).
# 2. Garante que o output do Python (logs, prints) seja enviado direto para o terminal.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# PASSO 3: Definir o diretório de trabalho
# Todos os comandos a partir daqui serão executados dentro da pasta /app no contêiner.
WORKDIR /app

# ---- PASSO NOVO ----
# Instalar as dependências do sistema operacional necessárias
# para construir o mysqlclient.
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev

# PASSO 4: Instalar as dependências
# Copiamos APENAS o arquivo de dependências primeiro.
COPY requirements.txt .
# Isso é uma otimização de cache. Se mudarmos nosso código, mas não as dependências,
# o Docker não precisará reinstalar tudo de novo, tornando o processo muito mais rápido.
RUN pip install --no-cache-dir -r requirements.txt

# PASSO 5: Copiar o código da aplicação
# Agora sim, copiamos todo o resto do código da nossa pasta 'backend' para dentro do /app no contêiner.
COPY . .

# PASSO 6: Expor a porta
# Informa ao Docker que a aplicação dentro do contêiner vai rodar na porta 8000.
EXPOSE 8000

# PASSO 7: Definir o comando de inicialização
# Este é o comando que será executado quando o contêiner iniciar.
# Ele usa o Gunicorn para servir nossa aplicação Django.
# Assumimos que nosso projeto Django se chamará 'config'. Criaremos isso em breve.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]