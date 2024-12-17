# Sistema de Reservas de Canchas de Fútbol - Frontend

Este es el proyecto final de la carrera Tecnicatura en Desarrollo Web en la Universidad Nacional del Comahue (CURZA). El sistema facilita la gestión de reservas de canchas de fútbol, permitiendo a los usuarios registrarse, realizar y cancelar reservas de forma eficiente. Además, las reservas son automatizadas para pasar al estado de "completadas" utilizando Celery y Redis.

## Contenido

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)

## Características

- **Autenticación de Usuarios:**: Sistema de autenticación para usuarios registrados.
- **Gestión de Canchas**: CRUD para manejar las canchas disponibles.
- **Gestión de Reservas**: CRUD para crear, ver y gestionar reservas de canchas.
- **Automatización de Estados**: Las reservas pasan automáticamente a "completadas" utilizando Celery y Redis.
- **Interfaz de Usuario Intuitiva**: Diseñada con Vue.js 3 y Tailwind CSS para una experiencia fluida y moderna.
- **Dockerización**: Contenerización de la aplicación para un despliegue sencillo y eficiente.

## Tecnologías Utilizadas

- **Vue.js 3**.
- **TypeScript**
- **Axios ** Para consumir de la api.
- **Tailwind CSS** Para los estilos
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
frontend/  
│  
├── .vscode/             # Configuración de VS Code  
├── cypress/             # Pruebas end-to-end con Cypress  
├── node_modules/        # Dependencias de Node.js  
├── public/              # Archivos públicos  
├── src/                 # Código fuente principal  
│   ├── assets/          # Recursos estáticos (imágenes, íconos, etc.)  
│   ├── components/      # Componentes reutilizables de Vue.js  
│   ├── interfaces/      # Definición de interfaces para TypeScript  
│   ├── layout/          # Estructura del diseño general  
│   ├── router/          # Configuración del enrutador Vue  
│   ├── stores/          # Manejo del estado con Pinia o Vuex  
│   ├── views/           # Vistas principales (páginas)  
│   ├── App.vue          # Componente raíz de la aplicación  
│   ├── axios.ts         # Configuración de Axios para las peticiones HTTP  
│   ├── main.ts          # Archivo de entrada principal  
│   ├── env.d.ts         # Tipado de variables de entorno  
│   ├── index.html       # Archivo base del frontend  
│   ├── package-lock.json  
│   └── package.json     # Configuración de dependencias y scripts  
│  
├── cypress.config.ts    # Configuración de Cypress  
└── .gitignore           # Archivos ignorados por Git  

```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](./LICENSE).
