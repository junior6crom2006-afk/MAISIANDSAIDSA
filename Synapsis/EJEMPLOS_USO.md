# 💀 EJEMPLOS DE USO CYBERCHAT

## 🚀 INICIO RÁPIDO (3 comandos):

```bash
# 1. Editar configuración (cambia 'tu_clave_aqui' por tu clave real)
nano config_simple.sh

# 2. Iniciar CyberChat
./iniciar_cyberchat.sh

# 3. Seleccionar opción 2 en el menú
```

## 💡 QUÉ HACER UNA VEZ DENTRO:

### Comandos básicos:
- Escribe: `help` → Ver todos los comandos
- Escribe: `scan` → Simular escaneo de puertos
- Escribe: `exploit` → Simular ejecución de exploits

### Preguntas de ejemplo para pentesting:
- "¿Cómo hacer un escaneo con nmap?"
- "¿Qué es un buffer overflow?"
- "¿Cómo crear un payload con msfvenom?"
- "¿Cómo hacer reconocimiento pasivo?"

### Comandos del sistema:
- `history` → Ver historial
- `session` → Info de la sesión
- `clear` → Limpiar pantalla
- `quit` → Salir

## ⚙️ CAMBIAR CONFIGURACIÓN:

### Para usar modelo más rápido:
```bash
# Edita config_simple.sh
export SYNAPSIS_CHAT_MODEL='phi3:3.8b'  # Más rápido
```

### Para cambiar nombre:
```bash
# Edita config_simple.sh
export HACKER_NAME='TU_NOMBRE'  # Tu nombre hacker
```

## 🔧 SI ALGO SALE MAL:

### Si dice "Address already in use":
```bash
# Matar procesos en puerto 8080
pkill -f "python3 chat_server.py"
```

### Si no responde la IA:
- Verifica que tu clave de OpenRouter sea correcta
- Comprueba conexión a internet
- Cambia a modelo `phi3:3.8b`

### Si es muy lento:
- Cambia modelo a `phi3:3.8b` en config_simple.sh
- Verifica que tengas buena conexión

## 🎯 RECUERDA:
- ✅ Ya tienes 2 modelos descargados (no necesitas más)
- ✅ Solo necesitas configurar tu clave de OpenRouter
- ✅ Todo funciona en entornos controlados
- ✅ Usa `./iniciar_cyberchat.sh` para inicio rápido

¡Listo para hackear de forma ética! 🔒⚡