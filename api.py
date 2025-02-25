from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas


# Cargar el archivo Excel al iniciar la API
EXCEL_PATH = "contraseñas_estudiantes.xlsx"
df = pd.read_excel("contrasena.xlsx")

# Convertir a un diccionario para acceso rápido
data_dict = {str(row["Carnet"]): row["Contrasena"] for _, row in df.iterrows()}

@app.route("/get-password", methods=["GET"])
def get_password():
    carnet = request.args.get("carnet")
    
    if not carnet:
        return jsonify({"error": "Debes proporcionar un carnet"}), 400
    
    password = data_dict.get(carnet)
    
    if password:
        return jsonify({"carnet": carnet, "contrasena": password})
    else:
        return jsonify({"error": "Carnet no encontrado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
