#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

# Función para mostrar el menú cyberpunk
show_menu() {
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║           💀 CYBERCHAT TERMINAL v2.0 - MENU              ║"
    echo "║              [ROOT ACCESS GRANTED]                       ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    echo "Selecciona una opción:"
    echo "1) 🌐 Interfaz Web (Navegador) - http://127.0.0.1:8080/"
    echo "2) 💻 Interfaz Terminal Cyberpunk (Aplicación dedicada)"
    echo "3) 🔧 Solo servidor (para APIs o testing)"
    echo "4) ❌ Salir"
    echo ""
    read -p "Opción (1-4): " choice
    echo ""
}

# Función para mostrar información de configuración
show_config_info() {
    echo ""
    echo "╔══════════════════════ CONFIGURACIÓN ══════════════════════╗"
    echo "║                                                                ║"
    echo "║  [VARIABLES DE ENTORNO PARA PERSONALIZACIÓN]                  ║"
    echo "║                                                                ║"
    echo "║  SYNAPSIS_CHAT_MODEL  → Modelo IA (por defecto: llama3.1:8b)   ║"
    echo "║  HACKER_NAME          → Tu nombre de hacker (por defecto: ANONYMOUS) ║"
    echo "║  OPENROUTER_KEYS      → API Key de OpenRouter (opcional)       ║"
    echo "║  OPENAI_API_KEY       → API Key de OpenAI (opcional)           ║"
    echo "║                                                                ║"
    echo "║  EJEMPLOS:                                                     ║"
    echo "║  export SYNAPSIS_CHAT_MODEL='codellama:13b'                    ║"
    echo "║  export HACKER_NAME='NEO'                                      ║"
    echo "║  export OPENROUTER_KEYS='sk-or-v1-...tu_clave...'              ║"
    echo "║                                                                ║"
    echo "╚══════════════════════════════════════════════════════════════════╝"
    echo ""
}

# Función para verificar dependencias
check_dependencies() {
    if ! command -v ollama &> /dev/null; then
        echo "[ERROR] ollama no está instalado. Instala con: sudo snap install ollama"
        exit 1
    fi

    # Modelo por defecto más técnico pero más ligero para pruebas
    MODEL="${SYNAPSIS_CHAT_MODEL:-phi3:3.8b}"
    if ! ollama list | grep -q "^$MODEL"; then
        echo "🔄 Descargando modelo $MODEL (este proceso puede tardar)..."
        ollama pull "$MODEL"
    fi

    python3 --version >/dev/null 2>&1 || { echo "Python3 no encontrado"; exit 1; }

    # Instalar dependencias Python
    python3 -m pip install --user flask requests rich 2>/dev/null || true
}

# Función para iniciar servidor
start_server() {
    echo "Iniciando servidor de chat..."
    python3 chat_server.py &
    SERVER_PID=$!
    echo "Servidor iniciado (PID: $SERVER_PID)"

    # Esperar a que el servidor esté listo
    for i in {1..10}; do
        if curl -s http://127.0.0.1:8080/health >/dev/null 2>&1; then
            echo "✅ Servidor listo en http://127.0.0.1:8080/"
            return 0
        fi
        sleep 1
    done

    echo "❌ Error: Servidor no pudo iniciarse"
    return 1
}

# Función para interfaz web
web_interface() {
    echo "🌐 Abriendo interfaz web..."
    echo "Accede a: http://127.0.0.1:8080/"
    echo ""
    echo "💡 Presiona Ctrl+C para detener el servidor"
    echo ""

    # Intentar abrir navegador automáticamente
    if command -v xdg-open &> /dev/null; then
        xdg-open http://127.0.0.1:8080/ 2>/dev/null &
    elif command -v open &> /dev/null; then
        open http://127.0.0.1:8080/ 2>/dev/null &
    fi

    # Mantener servidor corriendo
    wait $SERVER_PID
}

# Función para interfaz terminal
terminal_interface() {
    echo "💻 Iniciando interfaz de terminal CYBERPUNK..."
    echo ""

    # Verificar que rich esté instalado
    if ! python3 -c "import rich" 2>/dev/null; then
        echo "🔧 Instalando dependencias de terminal..."
        python3 -m pip install --user rich
    fi

    # Mostrar información de configuración
    show_config_info

    # Ejecutar aplicación de terminal cyberpunk
    python3 chat_terminal.py

    # Cuando termine, detener servidor
    echo "🔒 Deteniendo servidor..."
    kill $SERVER_PID 2>/dev/null || true
}

# Función para modo servidor solo
server_only() {
    echo "🔧 Modo servidor - API disponible en http://127.0.0.1:8080/"
    echo ""
    echo "💡 Presiona Ctrl+C para detener"
    echo ""
    echo "Endpoints disponibles:"
    echo "• GET  /          - Página principal"
    echo "• GET  /chat      - Interfaz web"
    echo "• POST /api/chat  - API de chat"
    echo "• GET  /health    - Estado del servidor"
    echo ""

    wait $SERVER_PID
}

# Verificar dependencias
check_dependencies

# Mostrar menú
show_menu

case $choice in
    1)
        echo "Opción seleccionada: 🌐 Interfaz Web [BROWSER MODE]"
        start_server && web_interface
        ;;
    2)
        echo "Opción seleccionada: 💻 Interfaz Terminal Cyberpunk [HACKER MODE]"
        start_server && terminal_interface
        ;;
    3)
        echo "Opción seleccionada: 🔧 Solo Servidor [API MODE]"
        start_server && server_only
        ;;
    4)
        echo "💀 DESCONECTANDO DEL SISTEMA..."
        exit 0
        ;;
    *)
        echo "❌ ACCESO DENEGADO - Opción inválida"
        exit 1
        ;;
esac
