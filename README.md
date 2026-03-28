---
title: DarkMax Bot
emoji: 🤖
colorFrom: blue
colorTo: red
sdk: docker
sdk_version: latest
app_file: Dockerfile
pinned: false
---

# DarkMax Bot

Bot de Telegram con IA para consultas de ciberseguridad, hacking, OSINT y programación.

## Características

- Autenticación por keys (user, vip, admin)
- Integración con OpenRouter (múltiples modelos)
- Soporte para chats privados y grupos
- Panel de administración
- Persistencia de sesiones y keys

## Requisitos

- Go 1.25.5 o superior
- Token de bot de Telegram (obtenido via [@BotFather](https://t.me/BotFather))
- API keys de OpenRouter (obtenidas en [OpenRouter](https://openrouter.ai))

## Configuración

1. Clona el repositorio:
   ```bash
   git clone <repo-url>
   cd IAMax
   ```

2. Instala dependencias:
   ```bash
   go mod tidy
   ```

3. Copia el archivo de entorno de ejemplo y configúralo:
   ```bash
   cp .env.example .env
   ```

4. Edita el archivo `.env` con tus credenciales:
   - `TELEGRAM_BOT_TOKEN`: Token de tu bot de Telegram
   - `OPENROUTER_KEYS`: Lista de keys de OpenRouter separadas por comas
   - `ADMIN_KEY`: Clave de administrador (opcional)
   - `ENCRYPTION_KEY`: Clave para encriptar datos (opcional, 32 caracteres)

5. Compila el bot:
   ```bash
   go build -o darkmax
   ```

6. Ejecuta el bot:
   ```bash
   ./darkmax
   ```

## Características de Seguridad

- Encriptación AES-256 de `keys.json`
- Verificación de integridad con checksums
- Rate limiting global y por usuario
- Rotación automática de API keys
- Notificaciones automáticas a admins si keys fallan
- Limpieza automática de cache
- Manejo de textos largos con chunking

## Ejecución

### Desarrollo
```bash
go run darkmax.go
```

### Producción
```bash
go build -o darkmax darkmax.go
./darkmax
```

### Docker
```bash
docker build -t darkmax .
docker run --env-file .env darkmax
```

## Monitoreo

- Logs en consola y `audit.log`
- Cache se limpia automáticamente cada 5 min
- Verificación de keys cada hora
- Notificaciones automáticas a admins si hay problemas

## Solución de Problemas

- Si falla con "Integrity check failed": Borra `keys.json.enc` y `keys.json.checksum`
- Si keys se desactivan: Rota las keys en OpenRouter y actualiza `.env`
- Para textos largos: El bot los procesa en chunks automáticamente

## Comandos de administrador

- `/deletekey KEY` – Elimina una key
- `/keyinfo KEY` – Muestra información de una key
- `/setrank KEY user|vip|admin` – Cambia el rango de una key
- `/togglekey KEY` – Activa/desactiva una key
- `/listkeys` – Lista todas las keys
- `/sessions` – Lista sesiones activas
- `/changeadminkey NUEVA` – Cambia la key de administrador

## Estructura de archivos

- `darkmax.go` – Código fuente principal
- `keys.json` – Base de datos de keys y sesiones (se crea automáticamente)
- `.env` – Variables de entorno (no incluido en el repositorio)
- `.gitignore` – Archivos ignorados por git

## Seguridad

- Nunca compartas tu archivo `.env` o `keys.json`.
- Rota las keys de OpenRouter periódicamente.
- Usa una clave de administrador segura.
- Considera usar un firewall para restringir el acceso al bot.

## Licencia

Este proyecto es de código abierto. Consulta el archivo LICENSE para más detalles.