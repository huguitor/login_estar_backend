repo backend:

markdown
Copiar
Editar
# login_estar_backend

Backend Django REST API para sistema de usuarios y notas con autenticación JWT.

## Setup

1. Clonar el repo

```bash
git clone https://github.com/huguitor/login_estar_backend.git
cd login_estar_backend
Crear y activar entorno virtual

bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
Instalar dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Crear archivo .env en la raíz del proyecto con las variables:

env
Copiar
Editar
SECRET_KEY=tu_clave_secreta_segura_generada
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Ejecutar migraciones

bash
Copiar
Editar
python manage.py migrate
Ejecutar servidor

bash
Copiar
Editar
python manage.py runserver
Endpoints principales
Registro usuario: POST /api/user/register/

JSON:

json
Copiar
Editar
{
  "username": "usuario",
  "password": "1234",
  "password2": "1234"
}
Login y obtención de tokens JWT: POST /api/token/

JSON:

json
Copiar
Editar
{
  "username": "usuario",
  "password": "1234"
}
Respuesta:

json
Copiar
Editar
{
  "refresh": "token_refresh",
  "access": "token_access"
}
Obtener perfil propio: GET /api/user/me/ (requiere token Authorization: Bearer <access>)

Lista y creación de notas: GET y POST /api/notes/ (requiere token)

Detalle, edición y eliminación de nota: GET, PUT, PATCH, DELETE /api/notes/<id>/ (requiere token)

Pruebas con curl
Ejemplo para crear usuario:

bash
Copiar
Editar
curl -X POST http://localhost:8000/api/user/register/ -H "Content-Type: application/json" -d "{\"username\": \"hugo\", \"password\": \"1234\", \"password2\": \"1234\"}"
Ejemplo para login:

bash
Copiar
Editar
curl -X POST http://localhost:8000/api/token/ -H "Content-Type: application/json" -d "{\"username\": \"hugo\", \"password\": \"1234\"}"
Ejemplo para crear nota (reemplaza <token_access> por el token válido):

bash
Copiar
Editar
curl -X POST http://localhost:8000/api/notes/ -H "Content-Type: application/json" -H "Authorization: Bearer <token_access>" -d "{\"title\": \"Mi nota\", \"content\": \"Esto es una prueba\"}"
