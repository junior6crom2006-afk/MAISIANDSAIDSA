# 🧠 Synapsis Chat - Sistema de Chat Conversacional IA

Sistema de chat conversacional que funciona como ChatGPT, integrado en el proyecto Synapsis.

## 🚀 Inicio Rápido

```bash
cd /home/max/Documentos/Darkmax/Synapsis
./start_chat.sh
```

Luego abre en tu navegador: **http://127.0.0.1:8080/**

## 📋 Requisitos

- **Python 3.6+** (ya instalado)
- **Ollama** (ya instalado via snap)
- **Modelo IA**: `phi3:3.8b` (ya descargado)

## 🔧 Configuración Opcional

### Para mejor rendimiento (recomendado si tienes RAM limitada):

```bash
# Opción 1: OpenRouter (recomendado - más modelos disponibles)
export OPENROUTER_KEYS="tu_clave_de_openrouter"
```

Obtén tu clave gratuita en: https://openrouter.ai/keys

```bash
# Opción 2: OpenAI directo
export OPENAI_API_KEY="tu_clave_de_openai"
```

Obtén tu clave en: https://platform.openai.com/api-keys

### Cambiar modelo IA:

```bash
export SYNAPSIS_CHAT_MODEL="otro_modelo"
# Ejemplos: llama2:7b, codellama:7b, etc.
```

## 🌐 Uso

### Interfaz Web
- Abre: `http://127.0.0.1:8080/`
- Escribe mensajes en el cuadro de texto
- Presiona Enter o "Enviar"

### API REST
```bash
curl -X POST http://127.0.0.1:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hola, ¿cómo estás?", "session":"mi_sesion"}'
```

Respuesta:
```json
{
  "session": "mi_sesion",
  "response": "¡Hola! Estoy bien, gracias por preguntar..."
}
```

## 🏗️ Arquitectura

1. **Frontend**: HTML/CSS/JavaScript puro
2. **Backend**: Flask (Python)
3. **IA Engine**:
   - **Primario**: Ollama (modelos locales)
   - **Fallback 1**: OpenRouter API (múltiples modelos)
   - **Fallback 2**: OpenAI API (si está configurada)
4. **Memoria**: Conversaciones por sesión en memoria

## 🔍 Solución de Problemas

### Error: "model requires more system memory"
- Tu RAM (3.4GB) es insuficiente para modelos grandes
- **Solución**: Configura `OPENAI_API_KEY` para usar IA en la nube

### Error: "OPENROUTER_KEYS no configurado"
- No tienes clave de OpenRouter configurada
- Obtén una en: https://openrouter.ai/keys
- Configura: `export OPENROUTER_KEYS="tu_clave"`

### Error: "OPENAI_API_KEY no configurado"
- No tienes clave de OpenAI configurada
- Obtén una en: https://platform.openai.com/api-keys
- Configura: `export OPENAI_API_KEY="tu_clave"`

### Error: "Failed to connect to 127.0.0.1 port 8080"
- El servidor no está ejecutándose
- Ejecuta: `./start_chat.sh`

### Error: "ollama no está instalado"
- Instala: `sudo snap install ollama`

## 📊 Estado del Sistema

Verifica componentes:
```bash
# Ollama
ollama --version
ollama list

# Python
python3 --version
python3 -c "import flask, requests; print('OK')"

# Servidor
curl http://127.0.0.1:8080/health
```

## 🎯 Características

- ✅ Chat conversacional fluido
- ✅ Memoria de conversación por sesión
- ✅ Interfaz web moderna (tipo ChatGPT)
- ✅ API REST para integraciones
- ✅ Fallback automático a OpenAI
- ✅ Manejo robusto de errores
- ✅ Multi-modelo (Ollama + OpenAI)

## 📝 Notas Técnicas

- **Puerto**: 8080 (configurable via `CHAT_SERVER_PORT`)
- **Sesiones**: Persisten en memoria durante la ejecución
- **Modelo default**: `phi3:3.8b` (2.2GB, eficiente)
- **Timeout IA**: 40 segundos
- **Historial**: Máximo 64 mensajes por sesión

---

¡El sistema está listo para usar! 🎉