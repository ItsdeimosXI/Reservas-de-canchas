# Reservas de Canchas - API

API desarrollada con Django Rest Framework para la gestión de reservas de canchas, que incluye funcionalidades para el registro de usuarios, gestión de canchas y reservas.

## Contenido

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Endpoints Principales](#endpoints-principales)

## Características

- **Registro de Usuarios**: Sistema de autenticación para usuarios registrados.
- **Gestión de Canchas**: CRUD para manejar las canchas disponibles.
- **Gestión de Reservas**: CRUD para crear, ver y gestionar reservas de canchas.

## Tecnologías Utilizadas

- **Python** y **Django** como base del proyecto.
- **Django Rest Framework** para la creación de la API.
- **SQLite** como base de datos (configurable a otras bases de datos).
- **Docker** para el despliegue y configuración del entorno.
- **Docker Compose** para la configuración de los servicios.

## Instalación

### Pre-requisitos

- **Docker** y **Docker Compose** instalados en tu máquina.

### Clonar el repositorio

```bash
git clone https://github.com/ItsdeimosXI/Reservas-de-canchas.git
cd Reservas-de-canchas
```

 1 - Copia el archivo de entorno .env.example a .env y configura las variables necesarias.

```bash
cp .env.example .env
```
 2 - Construye y levanta los contenedores de Docker.

```bash
docker-compose up --build
```
Esto instalará las dependencias definidas en requirements.txt y ejecutará el servidor.


## Ejecución

Una vez que el entorno esté configurado y los contenedores corriendo, la API estará disponible en http://localhost:8000.
Para detener los contenedores, puedes ejecutar:
```bash
docker-compose down 
```
## Estructura del proyecto
```bash
Reservas-de-canchas/
│
├── backend/
│   ├── app/                # Aplicación principal de Django
│   ├── canchas/            # Aplicación para gestionar canchas
│   ├── reservas/           # Aplicación para gestionar reservas
│   ├── db.sqlite3          # Base de datos SQLite
│   └── manage.py           # Script de administración de Django
│
├── config/
│   └── django-image/       # Configuración del entorno de Django en Docker
│       └──  Dockerfile              # Dockerfile para el backend
│       └──  requirements.txt        # Dependencias de Python
│       └──  runserver.sh            # Script para ejecutar el servidor
├── .env                    # Archivo de variables de entorno
├── .gitignore              # Archivos ignorados por Git
├── docker-compose.yml      # Configuración de Docker Compose

```

## Endpoints Principales
A continuación se describen los endpoints principales de la API:

/api/auth/: Endpoints para el registro y autenticación de usuarios.
/api/canchas/: CRUD para gestionar las canchas.
/api/reservas/: CRUD para gestionar las reservas de canchas.
