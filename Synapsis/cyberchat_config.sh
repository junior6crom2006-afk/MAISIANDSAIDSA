# CyberChat Configuration Examples
# Configuración de ejemplo para CyberChat Terminal v2.0

# ==========================================
# MODELOS DE IA RECOMENDADOS PARA PENTESTING
# ==========================================

# Modelo técnico avanzado (recomendado para pentesting)
export SYNAPSIS_CHAT_MODEL="codellama:13b"

# Modelo general con conocimientos técnicos
export SYNAPSIS_CHAT_MODEL="llama3.1:8b"

# Modelo ligero para sistemas con recursos limitados
export SYNAPSIS_CHAT_MODEL="phi3:3.8b"

# Modelo especializado en código y seguridad
export SYNAPSIS_CHAT_MODEL="deepseek-coder:6.7b"

# ==========================================
# CONFIGURACIÓN PERSONAL
# ==========================================

# Tu nombre de hacker (aparece en la interfaz)
export HACKER_NAME="NEO"

# Sistema objetivo (solo visual)
export TARGET_SYSTEM="CORPORATE_NETWORK"

# ==========================================
# APIs EXTERNAS (OPCIONALES)
# ==========================================

# OpenRouter API (para modelos premium)
export OPENROUTER_KEYS="sk-or-v1-tu_clave_aqui"

# OpenAI API (como fallback)
export OPENAI_API_KEY="sk-tu_clave_aqui"

# ==========================================
# EJEMPLOS DE USO
# ==========================================

# Configuración básica para pentesting
export SYNAPSIS_CHAT_MODEL="codellama:13b"
export HACKER_NAME="CYBERPUNK"
export TARGET_SYSTEM="ENTERPRISE_SERVER"

# Configuración para desarrollo malware
export SYNAPSIS_CHAT_MODEL="deepseek-coder:6.7b"
export HACKER_NAME="MALWARE_DEV"
export TARGET_SYSTEM="SANDBOX_ENV"

# Configuración para análisis forense
export SYNAPSIS_CHAT_MODEL="llama3.1:8b"
export HACKER_NAME="FORENSIC_ANALYST"
export TARGET_SYSTEM="COMPROMISED_SYSTEM"