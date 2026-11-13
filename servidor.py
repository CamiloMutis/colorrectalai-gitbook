"""Vista previa local del GitBook de ColorrectalAI.

Uso:
    python servidor.py          (Windows)
    python3 servidor.py         (Linux / macOS)
    python3 servidor.py 8801    (para usar otro puerto)

Siempre sirve la carpeta raíz del repositorio, sin importar desde dónde se ejecute.
"""

import functools
import http.server
import os
import socketserver
import sys
import webbrowser

PUERTO = int(sys.argv[1]) if len(sys.argv) > 1 else 8800
RAIZ = os.path.dirname(os.path.abspath(__file__))
URL = f"http://localhost:{PUERTO}/vista-previa/"


class Manejador(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # La raíz redirige a la vista previa
        if self.path in ("/", "/index.html"):
            self.send_response(302)
            self.send_header("Location", "/vista-previa/")
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, formato, *args):
        pass  # sin registro de cada petición, para que el enlace quede visible


def main():
    sys.stdout.reconfigure(line_buffering=True)
    manejador = functools.partial(Manejador, directory=RAIZ)
    socketserver.TCPServer.allow_reuse_address = True
    try:
        servidor = socketserver.ThreadingTCPServer(("127.0.0.1", PUERTO), manejador)
    except OSError:
        print(f"\n  El puerto {PUERTO} ya está en uso.")
        print(f"  Apaga el otro servidor o usa otro puerto:  python3 servidor.py {PUERTO + 1}\n")
        sys.exit(1)

    linea = "=" * 60
    print(f"\n{linea}")
    print("  Vista previa del GitBook de ColorrectalAI")
    print(linea)
    print(f"\n  Abre en el navegador:  {URL}\n")
    print("  Para apagar el servidor presiona Ctrl + C")
    print(f"{linea}\n")

    try:
        webbrowser.open(URL)
    except Exception:
        pass

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor apagado.\n")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
