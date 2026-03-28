#!/bin/bash
# Diagnóstico completo de CyberChat

echo "🔍 DIAGNÓSTICO COMPLETO DE CYBERCHAT"
echo "===================================="
echo ""

# Cargar configuración
source config_simple.sh

echo "📋 CONFIGURACIÓN ACTUAL:"
echo "OPENROUTER_KEYS: ${OPENROUTER_KEYS:0:25}..."
echo "SYNAPSIS_CHAT_MODEL: $SYNAPSIS_CHAT_MODEL"
echo "HACKER_NAME: $HACKER_NAME"
echo ""

echo "🤖 VERIFICANDO OLLAMA:"
if pgrep -f "ollama" > /dev/null; then
    echo "✅ Ollama está corriendo"
else
    echo "❌ Ollama NO está corriendo"
    echo "   Ejecuta: ollama serve"
    exit 1
fi

echo ""
echo "📦 MODELOS DISPONIBLES:"
ollama list

echo ""
echo "🧪 PROBANDO MODELOS (timeout 15s):"

# Probar phi3 (debería ser más rápido)
echo -n "phi3:3.8b: "
timeout 15 ollama run phi3:3.8b "Responde solo 'OK'" 2>/dev/null | head -1 || echo "❌ LENTO/MUERTO"

# Probar deepseek (puede ser lento)
echo -n "deepseek-coder:6.7b: "
timeout 15 ollama run deepseek-coder:6.7b "Responde solo 'OK'" 2>/dev/null | head -1 || echo "❌ LENTO/MUERTO"

echo ""
echo "🌐 PROBANDO OPENROUTER:"
if [ -n "$OPENROUTER_KEYS" ] && [ "$OPENROUTER_KEYS" != "tu_clave_aqui" ]; then
    response=$(timeout 10 curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: Bearer $OPENROUTER_KEYS" \
        -H "Content-Type: application/json" \
        -H "HTTP-Referer: https://darkmax.bot" \
        -H "X-Title: Synapsis-CyberChat" \
        -X POST https://openrouter.ai/api/v1/chat/completions \
        -d '{"model":"meta-llama/llama-3.2-3b-instruct","messages":[{"role":"user","content":"test"}],"max_tokens":5}')

    if [ "$response" = "200" ]; then
        echo "✅ OpenRouter funciona correctamente"
    else
        echo "❌ OpenRouter error (código: $response)"
    fi
else
    echo "❌ OpenRouter no configurado"
fi

echo ""
echo "🎯 ESTRATEGIA DE CONEXIÓN:"
echo "1. Intentar OpenRouter primero (rápido, sin censura efectiva)"
echo "2. Si falla, usar modelo local como respaldo"
echo "3. Si ambos fallan, mostrar mensaje amigable"

echo ""
echo "🚀 PARA INICIAR:"
echo "./iniciar_cyberchat.sh"
echo ""
echo "💡 Si aún hay problemas:"
echo "- OpenRouter debería funcionar siempre"
echo "- Los modelos locales son respaldo"
echo "- Verifica conexión a internet"