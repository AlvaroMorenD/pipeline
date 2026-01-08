# Usamos una imagen ligera de Python
FROM python:3.11-alpine

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos tu archivo específico al contenedor
COPY ej1.py .

# Ejecutamos el script. 
# El flag -u es para que los prints se vean al instante en la terminal
CMD ["python", "-u", "ej1.py"]
