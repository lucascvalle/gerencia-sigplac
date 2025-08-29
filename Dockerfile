# Use uma imagem base oficial do Python.
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner.
WORKDIR /app

# Copia o arquivo de dependências e instala as dependências.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o diretório de trabalho.
COPY . .

# Coleta os arquivos estáticos.
RUN python manage.py collectstatic --no-input

# Executa as migrações do banco de dados.
RUN python manage.py migrate --no-input

# Expõe a porta em que o aplicativo será executado.
EXPOSE 8000

# Comando para iniciar a aplicação.
# O nome 'gerencia.wsgi' deve corresponder ao nome do seu projeto Django.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gerencia.wsgi"]
