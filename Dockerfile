FROM python:3.9.20

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto donde corre Flask
EXPOSE 5000

# Comando para correr la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

