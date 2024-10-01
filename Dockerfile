# Dockerfile
FROM python:3.9

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que utiliza Flask
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
