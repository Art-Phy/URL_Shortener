## CHANGELOG

Todas las modificaciones relevantes del proyecto se documentan en este archivo siguiendo versionado semántico.

---

### [v0.4.0] Infraestructura integrada y acceso local

#### Añadido

- Integración completa de PostgreSQL dentro de Docker Compose.
- Levantamiento conjunto de aplicación y base de datos mediante un único comando.
- Configuración de hostname local para acceso al servicio mediante:
  - `http://backend-lab.local:8002`
- Acceso a documentación Swagger mediante:
  - `http://backend-lab.local:8002/docs`

####  Mejoras

- Simplificación del proceso de despliegue y desarrollo.
- Eliminación de dependencias externas para la base de datos.
- Mayor portabilidad del entorno completo.
- Arquitectura más cercana a un entorno productivo real.
- Mejor experiencia de uso y pruebas locales.

---

###  [v0.3.0] Dockerización y despliegue

#### Añadido

- Dockerización completa de la aplicación mediante `Dockerfile`.
- Orquestación de servicios mediante `docker-compose.yml`.
- Integración de PostgreSQL como base de datos para entorno containerizado.
- Configuración mediante variables de entorno externas (`.docker.env`).
- Archivo `.dockerignore` para optimizar la construcción de imágenes Docker.
- Persistencia de datos mediante volúmenes Docker.
- Preparación para despliegue en Raspberry Pi y servidores Linux.
- Despliegue validado en Raspberry Pi mediante Docker Compose.

#### Mejoras

- Entorno de desarrollo y despliegue completamente reproducible.
- Separación de configuración sensible fuera del repositorio.
- Estandarización del proceso de arranque de la aplicación.
- Mejora de la portabilidad entre diferentes sistemas operativos.
- Preparación para futuros despliegues en VPS o infraestructura propia.

---

### [v0.2.0] Analytics avanzadas

#### Añadido
- Registro de fecha de creación (`created_at`) y último acceso (`last_accessed`) por URL.
- Endpoint de estadísticas individuales por URL (`GET /stats/code/{short_code}`).
- Endpoint de ranking de URLs más clicadas (`GET /stats/top`).
- Endpoint de resumen global de uso (`GET /stats/summary`) con:
  - total de URLs creadas
  - total de clics
  - media de clics por URL
  - URL más popular
- Endpoint de estadísticas paginadas (`GET /stats`) con soporte para `limit` y `offset`.

#### Mejoras
- Diseño de endpoints orientado a analítica y reporting.
- Separación clara entre modelos ORM, esquemas Pydantic y lógica de negocio.
- README ampliado con descripción funcional, stack tecnológico y roadmap.

---

### [v0.1.0] MVP funcional

#### Añadido
- Endpoint para crear URLs cortas (`POST /shorten`).
- Endpoint de redirección (`GET /{short_code}`).
- Contador de clics por URL.
- Persistencia con SQLAlchemy y SQLite.
- Documentación automática de la API con Swagger (`/docs`).

---

### [v0.0.1] Estructura inicial

#### Añadido
- Estructura base del proyecto.
- Configuración inicial de FastAPI.
- Archivos fundamentales: README, LICENSE, CHANGELOG y requirements.
- Flujo de trabajo GitFlow inicializado.
