# Usa una imagen base oficial de Python 3.13
FROM python:3.13-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Expone el puerto que utiliza Flask (5000 por defecto)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "run.py"]
