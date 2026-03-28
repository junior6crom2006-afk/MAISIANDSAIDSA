#!/usr/bin/env bash
# Demo script para probar CyberChat con diferentes configuraciones

echo "💀 CYBERCHAT CONFIGURATION DEMO"
echo "==============================="
echo ""

# Configuración 1: Modo Pentesting
echo "🔧 Configuración 1: MODO PENTESTING"
export SYNAPSIS_CHAT_MODEL="codellama:13b"
export HACKER_NAME="PENTESTER"
export TARGET_SYSTEM="CORPORATE_NETWORK"
echo "SYNAPSIS_CHAT_MODEL=$SYNAPSIS_CHAT_MODEL"
echo "HACKER_NAME=$HACKER_NAME"
echo "TARGET_SYSTEM=$TARGET_SYSTEM"
echo ""

# Configuración 2: Modo Malware Development
echo "🔧 Configuración 2: MODO MALWARE DEV"
export SYNAPSIS_CHAT_MODEL="deepseek-coder:6.7b"
export HACKER_NAME="MALWARE_DEV"
export TARGET_SYSTEM="SANDBOX_ENV"
echo "SYNAPSIS_CHAT_MODEL=$SYNAPSIS_CHAT_MODEL"
echo "HACKER_NAME=$HACKER_NAME"
echo "TARGET_SYSTEM=$TARGET_SYSTEM"
echo ""

# Configuración 3: Modo Forense
echo "🔧 Configuración 3: MODO FORENSE"
export SYNAPSIS_CHAT_MODEL="llama3.1:8b"
export HACKER_NAME="FORENSIC_ANALYST"
export TARGET_SYSTEM="COMPROMISED_SYSTEM"
echo "SYNAPSIS_CHAT_MODEL=$SYNAPSIS_CHAT_MODEL"
echo "HACKER_NAME=$HACKER_NAME"
echo "TARGET_SYSTEM=$TARGET_SYSTEM"
echo ""

echo "💡 Para usar una configuración específica:"
echo "source cyberchat_config.sh  # Carga configuraciones predefinidas"
echo "./start_chat.sh            # Inicia CyberChat"
echo ""

echo "⚠️  RECUERDA: Configura tus APIs si quieres usar modelos premium"
echo "export OPENROUTER_KEYS='tu_clave_openrouter'"
echo "export OPENAI_API_KEY='tu_clave_openai'"