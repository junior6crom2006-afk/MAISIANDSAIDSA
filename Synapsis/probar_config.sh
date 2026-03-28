#!/bin/bash
# Script de prueba para verificar que CyberChat funciona

echo "🔧 Probando configuración de CyberChat..."
echo ""

# Cargar configuración
source config_simple.sh

# Verificar variables
echo "📋 Variables configuradas:"
echo "OPENROUTER_KEYS: ${OPENROUTER_KEYS:0:20}..."
echo "SYNAPSIS_CHAT_MODEL: $SYNAPSIS_CHAT_MODEL"
echo "HACKER_NAME: $HACKER_NAME"
echo ""

# Verificar que Ollama esté corriendo
echo "🤖 Verificando Ollama..."
if pgrep -f "ollama" > /dev/null; then
    echo "✅ Ollama está corriendo"
else
    echo "❌ Ollama no está corriendo. Inicia con: ollama serve"
    exit 1
fi

# Verificar modelos disponibles
echo ""
echo "📦 Modelos disponibles:"
ollama list

# Probar conexión a OpenRouter
echo ""
echo "🌐 Probando conexión a OpenRouter..."
if [ -n "$OPENROUTER_KEYS" ] && [ "$OPENROUTER_KEYS" != "tu_clave_aqui" ]; then
    response=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $OPENROUTER_KEYS" -H "Content-Type: application/json" -X POST https://openrouter.ai/api/v1/chat/completions -d '{"model":"meta-llama/llama-3.2-3b-instruct","messages":[{"role":"user","content":"test"}],"max_tokens":5}' --max-time 10)
    if [ "$response" = "200" ]; then
        echo "✅ OpenRouter API funciona correctamente"
    else
        echo "❌ Error en OpenRouter API (código: $response)"
        echo "   Verifica que tu clave sea correcta"
    fi
else
    echo "⚠️  OpenRouter no configurado (usa clave de prueba)"
fi

echo ""
echo "🚀 Si todo está OK, ejecuta:"
echo "   ./iniciar_cyberchat.sh"
echo ""
echo "💡 Dentro de CyberChat puedes usar:"
echo "   - Modelos locales (sin censura)"
echo "   - OpenRouter como respaldo"
echo "   - Comandos: help, scan, exploit, etc."