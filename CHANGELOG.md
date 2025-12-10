
## Changelog
Todas las modificaciones del proyecto se registrarán aquí siguiendo versión semántica.

### v0.1.0 - 10.12.2025
- Endpoint POST `/shorten` para crear URLs cortas
- Redirección GET `/{short_code}` con contador de clics
- DB funcional con SQLAlchemy y almacenamiento SQLite

#### Funcionalidades actuales
- Crear una URL corta a partir de una URL original
- Redirigir desde el código corto
- Contabilizar clics por acceso
- API documentada automáticamente en `/docs`

---

### v0.0.1 - 09.12.2025
- Se crea estructura base del proyecto
- Añadidos archivos iniciales: main.py, README, LICENSE, requirements, CHANGELOG
