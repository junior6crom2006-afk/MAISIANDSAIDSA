# � CyberChat Terminal v2.0

Interfaz de chat cyberpunk para pentesting, malware, exploits y desarrollo de herramientas de seguridad.

## 🔥 Características Cyberpunk

- **💀 Diseño Cyberpunk**: Interfaz hacker con ASCII art, colores neón y efectos visuales
- **🔐 Encriptación Cuántica**: Todo el tráfico simulado como encriptado
- **🎯 Comandos de Hacking**: Sistema de comandos especializados para pentesting
- **⚡ IA Especializada**: Modelos optimizados para temas técnicos de seguridad
- **🔥 Efectos Visuales**: Glitches aleatorios y animaciones cyberpunk
- **🛡️ Modo Seguro**: Entornos controlados para desarrollo de exploits

## 🚀 Inicio Rápido

```bash
cd /home/max/Documentos/Darkmax/Synapsis
./start_chat.sh
# Selecciona opción 2: "💻 Interfaz Terminal Cyberpunk [HACKER MODE]"
```

## ⚙️ Configuración Personalizada

### Variables de Entorno

```bash
# Modelo IA (recomendado para pentesting)
export SYNAPSIS_CHAT_MODEL="codellama:13b"

# Tu nombre de hacker
export HACKER_NAME="NEO"

# Sistema objetivo (visual)
export TARGET_SYSTEM="CORPORATE_NETWORK"

# APIs opcionales
export OPENROUTER_KEYS="tu_clave_openrouter"
export OPENAI_API_KEY="tu_clave_openai"
```

### Archivo de Configuración

Carga configuraciones predefinidas:

```bash
source cyberchat_config.sh
./start_chat.sh
```

## 📋 Comandos del Sistema

| Comando | Descripción | Uso |
|---------|-------------|-----|
| `help` | Manual del hacker | Muestra todos los comandos |
| `clear` | Reinicio del sistema | Limpia pantalla y reinicia interfaz |
| `history` | Historial de comandos | Muestra conversación completa |
| `session` | Info de sesión | Detalles técnicos de la sesión |
| `scan` | Escaneo de puertos | Simula escaneo de red |
| `exploit` | Ejecución de exploits | Simula explotación de vulnerabilidades |
| `encrypt` | Encriptación cuántica | Simula encriptación de mensajes |
| `decrypt` | Desencriptación | Simula desencriptación |
| `quit` / `exit` | Desconexión | Salir del sistema |

## 🎨 Interfaz Cyberpunk

### Header del Sistema
```
███████╗██╗   ██╗███╗   ██╗ █████╗ ██████╗ ███████╗██╗███████╗
██╔════╝╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██║██╔════╝
███████╗ ╚████╔╝ ██╔██╗ ██║███████║██████╔╝███████╗██║███████╗
╚════██║  ╚██╔╝  ██║╚██╗██║██╔══██║██╔═══╝ ╚════██║██║╚════██║
███████║   ██║   ██║ ╚████║██║  ██║██║     ███████║██║███████║
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝╚══════╝

╔══════════════════════════════════════════════════════════╗
║                 CYBERCHAT TERMINAL v2.0                  ║
║              [red]ROOT ACCESS GRANTED[/red] • [green]FIREWALL BYPASSED[/green]           ║
╚══════════════════════════════════════════════════════════╝
```

### Información del Sistema
```
╔══════════════════════════════════════════════════════════╗
║  🔧 System: HACKER    📊 Data: [cyan]NEO[/cyan]                      ║
║  🔧 System: SESSION   📊 Data: [yellow]BDA316FE[/yellow]                      ║
║  🔧 System: TARGET    📊 Data: [red]CORPORATE_NETWORK[/red]                 ║
║  🔧 System: MODEL     📊 Data: [blue]codellama:13b[/blue]                   ║
║  🔧 System: STATUS    📊 Data: [green]ONLINE • ENCRYPTED[/green]            ║
║  🔧 System: SECURITY  📊 Data: [red]HIGH • QUANTUM ENCRYPTED[/red]          ║
╚══════════════════════════════════════════════════════════╝
```

### Mensajes Hacker
```
╭─ ⚡ NEO [14:30:25] ─────────────────────────────────────╮
│ ¿Cómo puedo hacer un escaneo de puertos con nmap?      │
╰────────────────────────────────────────────────────────╯

╭─ 🤖 AI_CORE [14:30:28] ─────────────────────────────────╮
│ Para escanear puertos con nmap:                        │
│                                                        │
│ nmap -sV -O target_ip                                  │
│                                                        │
│ -sV: detección de versiones                            │
│ -O: detección de OS                                    │
╰────────────────────────────────────────────────────────╯
```

## 🔧 Modelos Recomendados

### Para Pentesting y Hacking
- **codellama:13b**: Modelo especializado en código y seguridad
- **deepseek-coder:6.7b**: Excelente para análisis de vulnerabilidades
- **llama3.1:8b**: Conocimientos técnicos generales

### Para Desarrollo de Malware
- **codellama:13b**: Generación de código malicioso
- **deepseek-coder:6.7b**: Análisis de payloads

### Para Análisis Forense
- **llama3.1:8b**: Análisis de logs y evidencias
- **codellama:13b**: Scripting forense

## 🛡️ Modo Seguro

**IMPORTANTE**: Esta herramienta está diseñada para entornos controlados y educativos. Todos los temas de pentesting, malware y exploits deben ejecutarse únicamente en:

- ✅ Máquinas virtuales locales
- ✅ Entornos de laboratorio
- ✅ Sistemas de prueba autorizados
- ✅ CTF (Capture The Flag) oficiales

**NO USAR** en sistemas reales sin autorización expresa.

## 🔌 Solución de Problemas

### Error de Timeout
```bash
# Reduce el timeout en chat_terminal.py
# Cambia timeout=15 a timeout=30 en call_chat_api()
```

### Modelo No Encontrado
```bash
# Verifica modelos disponibles
ollama list

# Descarga un modelo específico
ollama pull codellama:13b
```

### Problemas de API
```bash
# Verifica configuración de APIs
echo $OPENROUTER_KEYS
echo $OPENAI_API_KEY

# Configura una API válida
export OPENROUTER_KEYS="sk-or-v1-tu_clave"
```

## 🎯 Casos de Uso

### Pentesting Ético
```
Hacker: NEO
Objetivo: CORPORATE_NETWORK
Modelo: codellama:13b
```

### Desarrollo de Herramientas
```
Hacker: TOOL_DEV
Objetivo: SANDBOX_ENV
Modelo: deepseek-coder:6.7b
```

### Análisis de Seguridad
```
Hacker: SECURITY_ANALYST
Objetivo: COMPROMISED_SYSTEM
Modelo: llama3.1:8b
```

## 🚨 Disclaimer

Esta herramienta es para fines educativos y de investigación en ciberseguridad. El uso indebido puede violar leyes de protección de datos, leyes de acceso no autorizado y otras regulaciones. Los autores no se hacen responsables del mal uso de esta herramienta.

┌─ 🤖 IA (14:30:27) ──────────────────────────────┐
│ ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú? │
└─────────────────────────────────────────────────┘
```

## 🔧 Configuración

### Variables de Entorno
```bash
# OpenRouter (recomendado)
export OPENROUTER_KEYS="tu_clave_aqui"

# O OpenAI
export OPENAI_API_KEY="tu_clave_aqui"

# Modelo personalizado
export SYNAPSIS_CHAT_MODEL="otro_modelo"
```

## 📖 Uso Detallado

### Iniciar Chat
1. Ejecuta `./start_chat.sh`
2. Selecciona opción 2 (Terminal)
3. La aplicación se inicia automáticamente

### Chatear
- Escribe tu mensaje y presiona Enter
- Las respuestas aparecen formateadas
- El historial se mantiene automáticamente

### Comandos Especiales
- **help**: Ver todos los comandos disponibles
- **clear**: Limpiar pantalla y mostrar header
- **history**: Ver conversación completa
- **session**: Información técnica de la sesión

## 🎯 Estados de la Aplicación

### Estados de Conexión
- **🟢 Conectado**: Todo funciona correctamente
- **🟡 Esperando**: Procesando respuesta de IA
- **🔴 Error**: Problemas de conexión o API

### Indicadores Visuales
- **👤 Tú**: Tus mensajes (verde)
- **🤖 IA**: Respuestas de IA (azul)
- **⚠️ Error**: Mensajes de error (rojo)
- **💡 Info**: Información del sistema (amarillo)

## 🔍 Solución de Problemas

### Error: "El servidor de chat no está ejecutándose"
```
Solución: Ejecuta primero ./start_chat.sh y selecciona opción 1 o 3
```

### Error: "No hay API key configurada"
```
Solución: export OPENROUTER_KEYS="tu_clave"
```

### Error: "rich no está instalado"
```
Solución: pip3 install --user rich
```

## 🏗️ Arquitectura Técnica

```
Terminal App (Rich) → API REST → OpenRouter → Modelo IA
       ↓                    ↓
   Historial Local    Servidor Flask
       ↓                    ↓
   Persistencia       Motor Synapsis
```

## 📊 Rendimiento

- **Inicio**: < 3 segundos
- **Respuesta IA**: 2-10 segundos (depende del modelo)
- **Memoria**: ~50MB para la aplicación
- **CPU**: Mínimo durante espera

## 🎨 Personalización

### Colores
Los colores se pueden personalizar modificando las constantes en `chat_terminal.py`:
- `style="bold green"` - Mensajes de usuario
- `style="bold blue"` - Respuestas de IA
- `border_style="blue"` - Bordes de paneles

### Layout
El layout se puede ajustar modificando los objetos `Panel` y `Table` en el código.

## 🔄 Actualizaciones

Para actualizar la aplicación:
```bash
cd /home/max/Documentos/Darkmax/Synapsis
git pull
./start_chat.sh
```

## 📞 Soporte

Si encuentras problemas:
1. Verifica la conexión a internet
2. Confirma que las API keys sean válidas
3. Revisa los logs del servidor
4. Ejecuta `python3 chat_terminal.py --help`

---

¡Disfruta chateando con IA en una interfaz de terminal profesional! 🚀