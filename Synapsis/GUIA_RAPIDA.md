# 🚀 GUÍA RÁPIDA: Cómo Usar CyberChat

## PASO 1: Configurar tu clave de OpenRouter
Edita el archivo `config_simple.sh` y cambia 'tu_clave_aqui' por tu clave real:

```bash
nano config_simple.sh
# O usa cualquier editor de texto
```

Cambia esta línea:
```
export OPENROUTER_KEYS='tu_clave_aqui'
```
Por:
```
export OPENROUTER_KEYS='sk-or-v1-tu_clave_real_aqui'
```

## PASO 2: Elegir tu modelo IA
Ya tienes descargados estos modelos (NO necesitas descargar más):

- `deepseek-coder:6.7b` ⭐ (Recomendado para pentesting)
- `phi3:3.8b` (Más rápido, general)

En `config_simple.sh` ya está configurado `deepseek-coder:6.7b`

## PASO 3: Elegir tu nombre de hacker
Cambia 'HACKER' por el nombre que quieras:
```
export HACKER_NAME='TU_NOMBRE'
```

## Modo filtro libre (sin restricciones)
Configura el modo sin filtros para respuestas de hacking completas y técnicas:
```
export SYNAPSIS_NO_FILTER='1'  # 1 activa modo libre, 0 modo normal
```


## PASO 4: Iniciar CyberChat
Ejecuta cualquiera de estos comandos:

```bash
# Opción 1: Script automático (recomendado)
./iniciar_cyberchat.sh

# Opción 2: Manual
source config_simple.sh
./start_chat.sh
```

## PASO 5: Usar la interfaz
1. Selecciona opción 2: "💻 Interfaz Terminal Cyberpunk"
2. Escribe tus preguntas sobre pentesting
3. Usa comandos como 'help', 'scan', 'exploit', etc.

## 💡 COMANDOS ÚTILES EN CYBERCHAT:
- `help` - Ver todos los comandos
- `scan` - Simular escaneo de puertos
- `exploit` - Simular ejecución de exploits
- `history` - Ver historial de conversación
- `quit` - Salir

## 🔧 SOLUCIÓN DE PROBLEMAS:
- Si dice "Address already in use": Mata procesos en puerto 8080
- Si no responde: Verifica que tu clave de OpenRouter sea correcta
- Si es lento: Cambia a modelo `phi3:3.8b` en config_simple.sh

¡Eso es todo! CyberChat está listo para usar. 🚀