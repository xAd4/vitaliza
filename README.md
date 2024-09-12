##Vitaliza
Vitaliza es una plataforma web destinada a facilitar la comunicación entre pacientes y personal médico. Su enfoque principal es permitir a los usuarios enviar citas y mensajes para aclarar dudas, con la garantía de que un miembro capacitado del personal se pondrá en contacto con ellos.

#Características
Autenticación de Usuarios:

Registro de nuevos usuarios.
Inicio de sesión para usuarios registrados.
Recuperación de contraseñas a través de correo electrónico.
Gestión de Contenidos para Staff:

Edición de la sección "Sobre nosotros" incluyendo título y contenido.
Actualización de la lista de tratamientos y servicios ofrecidos, con la capacidad de modificar nombres y descripciones.
Acceso completo a todas las citas y mensajes enviados por los clientes.
Capacidad para eliminar citas y mensajes desde la base de datos.
Visualización y gestión de todos los modelos creados desde el panel de administración de Django.
Para Clientes:

Información detallada sobre los servicios y el personal médico.
Formulario para agendar citas.
Formulario para enviar mensajes y aclarar dudas.
Información de contacto de la empresa y su dirección.
Instalación
Sigue estos pasos para configurar el proyecto en tu entorno local:

#Clona el Repositorio:
```
git clone https://github.com/tu_usuario/vitaliza.git
cd vitaliza
```


#Configura el Entorno Virtual:
```
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

#Instala las Dependencias
```
pip install -r requirements.txt
```
#Configura las Variables de Entorno:

Crea un archivo .env en el directorio raíz del proyecto y añade las siguientes variables:
```
DEBUG=True
SECRET_KEY=tu_clave_secreta
NAME=nombre_base_datos
USER=tu_usuario
PASSWORD=tu_contraseña
HOST=localhost
PORT=3306
```
#Realiza las Migraciones y Carga Datos Iniciales:
```
python manage.py migrate
python manage.py loaddata initial_data
```
#Ejecuta el Servidor de Desarrollo:
```
python manage.py runserver
```
#Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.
