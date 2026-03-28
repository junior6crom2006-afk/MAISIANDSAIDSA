#!/usr/bin/env python3
"""
Synapsis CyberChat - Terminal Hacking Interface
Interfaz de chat estilo cyberpunk para pentesting y hacking
"""

import os
import sys
import uuid
import time
import random
import requests
from datetime import datetime
from collections import defaultdict

from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.live import Live
from rich.spinner import Spinner
from rich.columns import Columns
from rich.align import Align
from rich.layout import Layout
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
from rich.box import DOUBLE, HEAVY_HEAD, ROUNDED

console = Console()

class CyberChat:
    def __init__(self):
        self.session_id = str(uuid.uuid4())[:8].upper()
        self.conversations = defaultdict(list)
        self.api_url = "http://127.0.0.1:8080/api/chat"
        self.model = os.getenv("SYNAPSIS_CHAT_MODEL", "phi3:3.8b")
        self.no_filter = os.getenv("SYNAPSIS_NO_FILTER", "1") in ["1", "true", "True", "yes"]
        self.hacker_name = os.getenv("HACKER_NAME", "ANONYMOUS")
        self.target_system = "SYNAPSIS_CORE"

    def get_random_glitch(self):
        """Genera efectos visuales aleatorios de glitch"""
        glitches = ["[red]░[/red]", "[green]▒[/green]", "[blue]▓[/blue]", "[magenta]█[/magenta]", "[cyan]▄[/cyan]"]
        return random.choice(glitches)

    def call_chat_api(self, message):
        """Llama a la API de chat con timeout mejorado y mejor manejo de errores"""
        try:
            payload = {
                "message": message,
                "session": self.session_id,
                "model": self.model
            }
            # Timeout más generoso para respuestas complejas
            response = requests.post(self.api_url, json=payload, timeout=60)  # Aumentado a 60 segundos
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {"error": "⚠️  TIMEOUT: La IA tardó demasiado en responder. Intentando con modelo alternativo..."}
        except requests.exceptions.ConnectionError:
            return {"error": "🔌 CONNECTION FAILED: No se puede conectar al servidor. Verifica que esté corriendo."}
        except Exception as e:
            return {"error": f"💀 SYSTEM ERROR: {str(e)}"}

    def show_cyber_header(self):
        """Muestra el header cyberpunk"""
        # ASCII Art cyberpunk
        cyber_art = """
[red]███████╗██╗   ██╗███╗   ██╗ █████╗ ██████╗ ███████╗██╗███████╗[/red]
[red]██╔════╝╚██╗ ██╔╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██║██╔════╝[/red]
[green]███████╗ ╚████╔╝ ██╔██╗ ██║███████║██████╔╝███████╗██║███████╗[/green]
[green]╚════██║  ╚██╔╝  ██║╚██╗██║██╔══██║██╔═══╝ ╚════██║██║╚════██║[/green]
[blue]███████║   ██║   ██║ ╚████║██║  ██║██║     ███████║██║███████║[/blue]
[blue]╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝╚══════╝[/blue]

[magenta]╔══════════════════════════════════════════════════════════╗[/magenta]
[magenta]║                 CYBERCHAT TERMINAL v2.0                  ║[/magenta]
[magenta]║              [red]ROOT ACCESS GRANTED[/red] • [green]FIREWALL BYPASSED[/green]           ║[/magenta]
[magenta]╚══════════════════════════════════════════════════════════╝[/magenta]
        """

        console.print(cyber_art)

        # Información del sistema hacker
        system_info = Table(show_header=False, box=HEAVY_HEAD, style="cyan")
        system_info.add_column("🔧 System", style="red bold", width=15)
        system_info.add_column("📊 Data", style="green")

        system_info.add_row("HACKER", f"[cyan]{self.hacker_name}[/cyan]")
        system_info.add_row("SESSION", f"[yellow]{self.session_id}[/yellow]")
        system_info.add_row("TARGET", f"[red]{self.target_system}[/red]")
        system_info.add_row("MODEL", f"[blue]{self.model}[/blue]")
        system_info.add_row("FILTER", f"[yellow]{'OFF' if self.no_filter else 'ON'}[/yellow]")
        system_info.add_row("STATUS", "[green]ONLINE • ENCRYPTED[/green]")
        system_info.add_row("SECURITY", "[red]HIGH • QUANTUM ENCRYPTED[/red]")

        console.print(Panel(system_info, title="[red]🔐 SYSTEM STATUS[/red]", border_style="red", title_align="center"))

    def show_cyber_message(self, role, content, timestamp=None):
        """Muestra un mensaje con estilo cyberpunk"""
        if timestamp is None:
            timestamp = datetime.now().strftime("%H:%M:%S")

        if role == "user":
            # Mensaje del hacker
            header = f"[red]⚡ {self.hacker_name} [{timestamp}][/red]"
            border_style = "red"
            content_style = "red"
            icon = "👤"
        else:
            # Respuesta de la IA
            header = f"[green]🤖 AI_CORE [{timestamp}][/green]"
            border_style = "green"
            content_style = "green"
            icon = "🤖"

        # Agregar efectos visuales aleatorios
        glitch = self.get_random_glitch() if random.random() < 0.1 else ""

        # Panel cyberpunk
        panel = Panel(
            f"[bold {content_style}]{content}[/bold {content_style}]\n{glitch}",
            title=f"[bold]{icon} {header}[/bold]",
            border_style=border_style,
            box=DOUBLE,
            title_align="left",
            padding=(1, 2)
        )

        console.print(panel)
        console.print()  # Espacio

    def show_cyber_help(self):
        """Muestra la ayuda en estilo cyberpunk"""
        help_content = """
[red]╔══════════════════════ COMANDOS DEL SISTEMA ══════════════════════╗[/red]
[red]║                                                                    ║[/red]
[red]║  [green]help[/green]     → Mostrar este menú de ayuda                           ║[/red]
[red]║  [green]clear[/green]    → Limpiar pantalla y reiniciar interfaz               ║[/red]
[red]║  [green]history[/green]  → Mostrar historial completo de comandos              ║[/red]
[red]║  [green]session[/green]  → Información detallada de la sesión actual           ║[/red]
[red]║  [green]scan[/green]     → Escanear puertos del sistema objetivo               ║[/red]
[red]║  [green]exploit[/green]  → Ejecutar exploit en el sistema                      ║[/red]
[red]║  [green]encrypt[/green]  → Encriptar mensaje con algoritmo cuántico            ║[/red]
[red]║  [green]decrypt[/green]  → Desencriptar mensaje                                ║[/red]
[red]║  [green]nofilter[/green]→ Alternar filtro OFF/ON para respuestas abiertas     ║[/red]
[red]║  [green]quit[/green]     → Salir del sistema                                   ║[/red]
[red]║                                                                    ║[/red]
[red]╚════════════════════════════════════════════════════════════════════╝[/red]

[yellow]💡 PRO TIP: Usa Ctrl+C para salir rápidamente en caso de emergencia[/yellow]
        """
        console.print(Panel(help_content, title="[red]📚 MANUAL DEL HACKER[/red]", border_style="red"))

    def show_cyber_history(self):
        """Muestra el historial con estilo cyberpunk"""
        if not self.conversations[self.session_id]:
            console.print("[red]⚠️  HISTORIAL VACÍO: No hay comandos ejecutados aún[/red]")
            return

        console.print(f"\n[red]╔══════════════════════ HISTORIAL DE COMANDOS ══════════════════════╗[/red]")
        console.print(f"[red]║ Sesión: {self.session_id} • Total: {len(self.conversations[self.session_id])} comandos[/red]")
        console.print(f"[red]╚══════════════════════════════════════════════════════════════════════╝[/red]\n")

        for i, msg in enumerate(self.conversations[self.session_id], 1):
            role = msg['role']
            content = msg['content']
            timestamp = datetime.now().strftime("%H:%M:%S")  # Podríamos guardar timestamps reales

            if role == "user":
                console.print(f"[red][{i:2d}] ⚡ {self.hacker_name}: {content}[/red]")
            else:
                console.print(f"[green][{i:2d}] 🤖 AI_CORE: {content}[/green]")

        console.print()

    def show_cyber_session_info(self):
        """Muestra información de sesión estilo cyberpunk"""
        info = {
            "🔐 ID de Sesión": self.session_id,
            "👤 Hacker": self.hacker_name,
            "🎯 Sistema Objetivo": self.target_system,
            "🤖 Modelo IA": self.model,
            "🌐 Endpoint API": self.api_url,
            "⏰ Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "📊 Comandos Ejecutados": len(self.conversations[self.session_id]),
            "🔒 Estado de Seguridad": "HIGH • QUANTUM ENCRYPTED",
            "⚡ Nivel de Acceso": "ROOT • ADMIN PRIVILEGES"
        }

        table = Table(title="[red]🔍 INFORMACIÓN DE SESIÓN[/red]", show_header=False, box=DOUBLE, style="cyan")
        table.add_column("[red]Parámetro[/red]", style="red bold", width=20)
        table.add_column("[green]Valor[/green]", style="green")

        for key, value in info.items():
            table.add_column(key, value)

        console.print(table)

    def cyber_spinner(self):
        """Spinner cyberpunk personalizado"""
        spinners = ["🔄", "⚡", "💀", "🔥", "⚠️", "💣", "🔓", "🔒"]
        return random.choice(spinners)

    def run(self):
        """Ejecuta la aplicación cyberpunk"""
        # Limpiar pantalla y mostrar header
        console.clear()
        self.show_cyber_header()

        # Mensaje de bienvenida cyberpunk
        welcome_text = f"""
[red]╔══════════════════════════════════════════════════════════╗[/red]
[red]║              [green]BIENVENIDO AL CYBERCHAT v2.0[/green]                 ║[/red]
[red]║                                                                        ║[/red]
[red]║  [yellow]Hacker:[/yellow] [cyan]{self.hacker_name}[/cyan]                                     ║[/red]
[red]║  [yellow]Objetivo:[/yellow] [red]{self.target_system}[/red]                                 ║[/red]
[red]║  [yellow]Estado:[/yellow] [green]CONECTADO • ENCRIPTADO • ROOT ACCESS[/green]         ║[/red]
[red]║                                                                        ║[/red]
[red]╚══════════════════════════════════════════════════════════╝[/red]

[cyan]💀 RECUERDA: Todo el tráfico está encriptado con algoritmos cuánticos[/cyan]
[cyan]⚡ Usa comandos del sistema para operaciones avanzadas[/cyan]
[cyan]🔥 Mantén la discreción - el sistema está siendo monitoreado[/cyan]
        """
        console.print(Panel(welcome_text, border_style="red"))
        console.print()

        while True:
            try:
                # Prompt cyberpunk
                prompt_text = f"[red]⚡ {self.hacker_name}@cyberchat[/red][green]>[/green][cyan]>[/cyan][blue]>[/blue] "
                user_input = Prompt.ask(prompt_text).strip()

                if not user_input:
                    continue

                # Procesar comandos especiales
                if user_input.lower() in ['quit', 'exit', 'q']:
                    console.print(f"\n[red]💀 DESCONECTANDO...[/red]")
                    time.sleep(1)
                    console.print(f"[red]🔒 SESIÓN TERMINADA • DATOS ENCRIPTADOS[/red]")
                    break
                elif user_input.lower() == 'help':
                    self.show_cyber_help()
                    continue
                elif user_input.lower() == 'clear':
                    console.clear()
                    self.show_cyber_header()
                    continue
                elif user_input.lower() == 'history':
                    self.show_cyber_history()
                    continue
                elif user_input.lower() == 'session':
                    self.show_cyber_session_info()
                    continue
                elif user_input.lower() in ['nofilter', 'filter']:
                    self.no_filter = not self.no_filter
                    status = 'OFF' if self.no_filter else 'ON'
                    console.print(f"[cyan]🔓 Modo Filtro Nueva configuración: {status}[/cyan]")
                    continue
                elif user_input.lower() == 'scan':
                    console.print("[green]🔍 ESCANEANDO PUERTOS...[/green]")
                    console.print("[yellow]Puertos abiertos: 22(SSH), 80(HTTP), 443(HTTPS), 8080(CUSTOM)[/yellow]")
                    continue
                elif user_input.lower() == 'exploit':
                    console.print("[red]💣 EJECUTANDO EXPLOIT...[/red]")
                    console.print("[green]✅ VULNERABILIDAD ENCONTRADA • EXPLOTACIÓN EXITOSA[/green]")
                    continue
                elif user_input.lower() == 'encrypt':
                    console.print("[blue]🔐 ENCRIPTANDO MENSAJE...[/blue]")
                    console.print("[green]✅ MENSAJE ENCRIPTADO CON ALGORITMO CUÁNTICO[/green]")
                    continue
                elif user_input.lower() == 'decrypt':
                    console.print("[blue]🔓 DESENCRIPTANDO MENSAJE...[/blue]")
                    console.print("[green]✅ MENSAJE DESENCRIPTADO[/green]")
                    continue

                # Agregar comando al historial
                self.conversations[self.session_id].append({
                    "role": "user",
                    "content": user_input
                })

                # Mostrar comando del usuario
                self.show_cyber_message("user", user_input)

                # Spinner cyberpunk mientras espera respuesta
                spinner_text = f"[red]{self.cyber_spinner()} CONECTANDO CON IA_CORE...[/red]"
                with console.status(spinner_text, spinner="dots"):
                    response = self.call_chat_api(user_input)

                # Procesar respuesta
                if "error" in response:
                    error_msg = response["error"]
                    # Si es timeout, intentar automáticamente (no mostrar error al usuario)
                    if "TIMEOUT" in error_msg:
                        console.print(f"[yellow]⏳ Sistema ocupado, intentando conexión alternativa...[/yellow]")
                        # Intentar una segunda vez con timeout más corto
                        time.sleep(1)
                        with console.status("[red]🔄 RECONECTANDO...[/red]", spinner="dots"):
                            response = self.call_chat_api(user_input)

                        # Si vuelve a fallar, mostrar mensaje amigable
                        if "error" in response:
                            console.print(f"[red]⚠️  SISTEMA OCUPADO: La IA está procesando. Intenta de nuevo en unos segundos.[/red]")
                            continue
                    else:
                        # Mostrar otros errores
                        error_panel = Panel(
                            f"[red]{error_msg}[/red]",
                            title="[red]💀 ERROR CRÍTICO[/red]",
                            border_style="red",
                            box=DOUBLE
                        )
                        console.print(error_panel)
                        continue
                else:
                    ai_response = response.get("response", "[red]SIN RESPUESTA DEL SISTEMA[/red]")
                    # Agregar respuesta de IA al historial
                    self.conversations[self.session_id].append({
                        "role": "assistant",
                        "content": ai_response
                    })
                    # Mostrar respuesta de IA
                    self.show_cyber_message("assistant", ai_response)

            except (KeyboardInterrupt, EOFError):
                console.print(f"\n[red]💀 INTERRUPCIÓN DETECTADA • SALIENDO DEL SISTEMA...[/red]")
                break
            except Exception as e:
                console.print(f"[red]💀 ERROR CRÍTICO DEL SISTEMA: {str(e)}[/red]")
                continue

def main():
    """Función principal"""
    # Verificar que el servidor esté corriendo
    try:
        response = requests.get("http://127.0.0.1:8080/health", timeout=5)
        if response.status_code != 200:
            raise Exception("Servidor no responde correctamente")
    except:
        console.print("[red]💀 ERROR CRÍTICO: El servidor principal no está operativo[/red]")
        console.print("[yellow]🔧 Ejecuta primero: ./start_chat.sh y selecciona opción 1 o 3[/yellow]")
        sys.exit(1)

    # Verificar API key
    if not os.getenv("OPENROUTER_KEYS") and not os.getenv("OPENAI_API_KEY"):
        console.print("[red]⚠️  ALERTA DE SEGURIDAD: No hay credenciales de API configuradas[/red]")
        console.print("[yellow]🔐 Configura: export OPENROUTER_KEYS='tu_clave'[/yellow]")
        console.print("[yellow]🔐 O usa: export OPENAI_API_KEY='tu_clave'[/yellow]")
        console.print()

    # Iniciar aplicación cyberpunk
    chat = CyberChat()
    chat.run()

if __name__ == "__main__":
    main()