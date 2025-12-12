## 📄 CHANGELOG

Todas las modificaciones relevantes del proyecto se documentan en este archivo siguiendo versionado semántico.

---

### [v0.2.0] — Analytics avanzadas

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

### [v0.1.0] — MVP funcional

#### Añadido
- Endpoint para crear URLs cortas (`POST /shorten`).
- Endpoint de redirección (`GET /{short_code}`).
- Contador de clics por URL.
- Persistencia con SQLAlchemy y SQLite.
- Documentación automática de la API con Swagger (`/docs`).

---

### [v0.0.1] — Estructura inicial

#### Añadido
- Estructura base del proyecto.
- Configuración inicial de FastAPI.
- Archivos fundamentales: README, LICENSE, CHANGELOG y requirements.
- Flujo de trabajo GitFlow inicializado.
