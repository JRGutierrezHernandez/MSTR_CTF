from flask import Flask, jsonify, send_from_directory
import psutil
import threading
import time

# Le decimos a Flask que todo está en la misma carpeta
app = Flask(__name__, static_folder=".", static_url_path="")

datos = {"cpu": 0, "ram": 0}

def monitor():
    while True:
        datos["cpu"] = psutil.cpu_percent(interval=1)
        datos["ram"] = psutil.virtual_memory().percent

threading.Thread(target=monitor, daemon=True).start()

# Servir el HTML principal
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# API de datos
@app.route("/datos")
def datos_api():
    return jsonify(datos)

# Servir archivos estáticos (CSS, etc.)
@app.route("/<path:archivo>")
def static_files(archivo):
    return send_from_directory(".", archivo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)