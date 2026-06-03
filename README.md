
## README
### URL Shortener

<p align="left">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/FastAPI-REST-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql" />
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker" />
  <img src="https://img.shields.io/badge/Docker%20Compose-Orchestration-2496ED?logo=docker" />
  <img src="https://img.shields.io/badge/Status-Portfolio%20Project-success" />
  <img src="https://img.shields.io/badge/Raspberry%20Pi-Deployed-C51A4A?logo=raspberrypi" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</>

### URL Shortener

Servicio backend desarrollado con **FastAPI** que permite acortar URLs, redirigir a su destino original y recopilar estadísticas de uso y métricas de analítica.

Este proyecto ha sido desarrollado como parte de un **portfolio backend**, con el objetivo de demostrar diseño de APIs REST, trabajo con bases de datos relacionales, analítica básica, Docker, PostgreSQL y buenas prácticas de desarrollo y control de versiones.

---

### Funcionalidades

#### Core
- Creación de URLs cortas a partir de URLs originales.
- Redirección automática al destino original.
- Contabilización de clics por enlace.
- Persistencia de datos mediante SQLAlchemy.

#### Analytics
- Estadísticas detalladas por URL.
- Ranking de URLs más clicadas.
- Resumen global del uso del servicio.
- Paginación de resultados para manejar grandes volúmenes de datos.
- Registro de fechas de creación y último acceso.

#### DevOps & Deployment
- Dockerización completa de la aplicación.
- Orquestación mediante Docker Compose.
- Integración con PostgreSQL.
- Gestión de configuración mediante variables de entorno.
- Preparado para despliegue en Raspberry Pi, VPS o servidores Linux.
- Stack completo levantado mediante Docker Compose.
- Acceso mediante hostname local (`backend-lab.local`).
- Healthchecks para supervisión del estado de los servicios.

---

### Endpoints principales

- `POST /shorten` → crear URL corta
- `GET /{short_code}` → redirigir a la URL original
- `GET /stats/code/{short_code}` → estadísticas de una URL concreta
- `GET /stats/top` → ranking de URLs más clicadas
- `GET /stats/summary` → resumen global del servicio
- `GET /stats?limit=&offset=` → estadísticas paginadas

La documentación interactiva está disponible en:

```
/docs
```

---

### Stack tecnológico

#### Backend

- **Lenguaje:** Python
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Validación de datos:** Pydantic v2
- **Servidor ASGI:** Uvicorn

#### Base de datos

- PostgreSQL
- Alembic (migraciones versionadas)

#### Infraestructura

- Docker
- Docker Compose

#### Control de versiones

- Git
- GitFlow

---

### Ejecución mediante Docker Compose

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPO>
cd URL_Shortener
```

2. Configurar variables de entorno:

```bash
cp .docker.env.example .docker.env
```

3. Construir y arrancar servicios:

```bash
docker compose up --build
```

4. Acceder a:

- API: `http://backend-lab.local:8002`
- Docs: `http://backend-lab.local:8002/docs`


---

### Decisiones técnicas destacables

- Diseño de APIs REST con FastAPI.
- Validación de datos mediante Pydantic.
- SQLAlchemy ORM.
- PostgreSQL.
- Alembic y migraciones versionadas.
- Analytics y reporting.
- Paginación de resultados.
- Docker.
- Docker Compose.
- Persistencia mediante volúmenes Docker.
- Healthchecks de servicios.
- Gestión de variables de entorno.
- Despliegue reproducible.
- GitFlow.
- Versionado semántico.

---

### Posibles extensiones futuras (no implementadas)

- Sistema de usuarios y autenticación JWT.
- Exportación de estadísticas (CSV).
- Dashboard web para visualización de métricas.
- Integración de Redis para caché.
- Monitorización y observabilidad.


---

Este proyecto representa un backend completo, funcional y desplegable, diseñado para demostrar competencias reales en desarrollo backend moderno, diseño de APIs, analítica y despliegue de aplicaciones containerizadas.
