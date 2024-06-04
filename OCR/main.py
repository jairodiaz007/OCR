from flask import Flask, jsonify
from PIL import Image
import pytesseract
import numpy as np

app = Flask(__name__)
#@app.route('/api/data2', methods=['GET'])
#def get_data2():
#    filename = 'E:/Personal/fotoDatosFactura CLARO.png'
#    img = np.array(Image.open(filename))
#   pytesseract.pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"
#  text = pytesseract.image_to_string(img)    
#    api_string = "Este es el string de la API2"    
#    return jsonify({'string': text})    
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hola desde la API en Python",
        "status": "success"
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')