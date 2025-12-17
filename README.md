
## 📘 README
### URL Shortener 🔗

<p align="left">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/FastAPI-REST-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red" />
  <img src="https://img.shields.io/badge/Status-Portfolio%20Project-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

Servicio backend desarrollado con **FastAPI** que permite acortar URLs, redirigir a su destino original y recopilar estadísticas de uso y métricas de analítica.

### URL Shortener 🔗

Servicio backend desarrollado con **FastAPI** que permite acortar URLs, redirigir a su destino original y recopilar estadísticas de uso y métricas de analítica.

Este proyecto ha sido desarrollado como parte de un **portfolio backend**, con el objetivo de demostrar diseño de APIs REST, trabajo con bases de datos relacionales, analítica básica y buenas prácticas de desarrollo y control de versiones.

---

### ✨ Funcionalidades

#### Core
- Creación de URLs cortas a partir de URLs originales.
- Redirección automática al destino original.
- Contabilización de clics por enlace.

#### Analytics
- Estadísticas detalladas por URL.
- Ranking de URLs más clicadas.
- Resumen global del uso del servicio.
- Paginación de resultados para manejar grandes volúmenes de datos.
- Registro de fechas de creación y último acceso.

---

### 📊 Endpoints principales

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

### 🛠️ Stack tecnológico

- **Lenguaje:** Python
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Validación de datos:** Pydantic v2
- **Base de datos:** SQLite (entorno de desarrollo)
- **Servidor ASGI:** Uvicorn
- **Control de versiones:** Git + GitFlow

---

### ⚙️ Ejecución en local

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPO>
   cd URL_Shortener
   ```

2. Crear y activar entorno virtual.

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Acceder a:
   - API: `http://127.0.0.1:8000`
   - Docs: `http://127.0.0.1:8000/docs`

---

### 🧠 Decisiones técnicas destacables

- Uso de paginación (`limit` / `offset`) para escalabilidad.
- Endpoints orientados a analítica y reporting.
- Versionado semántico con releases claras.
- Flujo GitFlow aplicado estrictamente (`main`, `develop`, `feature/*`).
- Proyecto acotado y coherente, pensado para ser explicable en entrevistas.

---

### 🔭 Posibles extensiones futuras (no implementadas)

- Sistema de usuarios y autenticación.
- Exportación de estadísticas (CSV).
- Migración a PostgreSQL para producción.
- Frontend ligero para consumo visual del servicio.

---

Este proyecto representa un backend completo, funcional y bien estructurado, diseñado para demostrar competencias reales en desarrollo backend y analítica básica.
