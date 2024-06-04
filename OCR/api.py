from flask import Flask, jsonify
from PIL import Image
import pytesseract
import numpy as np

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    ruta = 'E:/Personal/fotoDatosFactura CLARO.png'
    img = np.array(Image.open(ruta))
    pytesseract.pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"
    # Realiza el OCR en la imagen
    text = pytesseract.image_to_string(img)    
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)