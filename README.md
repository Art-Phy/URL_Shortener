
### URL Shortener 🔗

Servicio backend desarrollado con **FastAPI** que permite acortar URLs largas, redirigir a su destino original y obtener estadísticas de uso.

Actualmente el proyecto se encuentra en fase de desarrollo activo, siguiendo un flujo de trabajo **GitFlow** y aplicando buenas prácticas de arquitectura, documentación y control de versiones.

---

#### ✨ Funcionalidades actuales

- Crear URLs cortas a partir de URLs originales mediante la API (`POST /shorten`).
- Redirigir a la URL original usando el código corto (`GET /{short_code}`).
- Contabilizar el número de clics por cada enlace.
- Consultar estadísticas detalladas de un enlace concreto (`GET /stats/code/{short_code}`).
- Obtener el ranking de los enlaces más clicados (`GET /stats/top`).
- Ver un resumen global de uso del servicio (`GET /stats/summary`), incluyendo:
  - total de URLs creadas
  - total de clics
  - media de clics por URL
  - enlace más clicado

> La documentación interactiva de la API está disponible en `/docs` (Swagger UI).

---

#### 🛠️ Stack tecnológico

- **Lenguaje:** Python
- **Framework:** FastAPI
- **Base de datos:** SQLite (en desarrollo, con ORM SQLAlchemy)
- **Validación de datos:** Pydantic v2
- **ORM:** SQLAlchemy
- **Control de versiones:** Git + GitFlow
- **Servidor de desarrollo:** Uvicorn

---

#### 🚀 Roadmap (próximos pasos)

Algunas de las mejoras previstas para futuras versiones:

- Paginación y filtros avanzados en endpoints de estadísticas.
- Sistema de usuarios y autenticación para gestionar URLs por cuenta.
- Migración de SQLite a una base de datos más robusta (por ejemplo, PostgreSQL) para entornos productivos.
- Panel o frontend sencillo para consumir el servicio desde navegador.
- Exportación de estadísticas (por ejemplo, a CSV).

---

#### ⚙️ Ejecución en local (modo desarrollo)

1. Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPO>
   cd URL_Shortener

2. Crear y activar un entorno virtual (opcional pero recomendado)

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt

4. Ejecutar el servidor
    ```bash
    uvicorn app.main:app --reload

5. Abrir el navegador:
    - API root: http://127.0.0.1:8000/
    - Documentación interactiva: http://1227.0.0.1:8000/docs

---

Este proyecto forma parte de mi portfolio como desarrollador backend y está diseñado para demostrar conceptos como diseño de APIs REST, analítica básica, buenas prácticas con GitFlow y trabajo con bases de datos relacionales desde Python.