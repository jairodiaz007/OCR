from fastapi import FastAPI
from PIL import Image
import pytesseract
import numpy as np

from flask import Flask, request

app = Flask(__name__)

@app.route("/ruta_de_tu_api", methods=["POST"])
def recibir_archivo():
    archivo = request.files["archivo"]
    if archivo:
        # Procesa el archivo (por ejemplo, guárdalo en el servidor)
        return "Archivo recibido correctamente."
    else:
        return "No se ha seleccionado ningún archivo."

if __name__ == "__main__":
    app.run(debug=True)