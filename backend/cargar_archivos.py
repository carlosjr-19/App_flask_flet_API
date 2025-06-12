from flask import Blueprint, request, jsonify
import polars as pl
import os

# Creamos un blueprint para modularizar
upload_bp = Blueprint('upload_bp', __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'storage')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def limpiar_storage():
    for f in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, f)
        os.remove(file_path)
        print("entre en funcion limpiar")
        print(f"Eliminado archivo: {file_path}")

@upload_bp.route('/upload', methods=['POST'])
def upload_files():
    limpiar_storage() 

    if 'archivo_1' not in request.files or 'archivo_2' not in request.files:
        return jsonify({"error": "Faltan archivos"}), 400

    archivo_1 = request.files['archivo_1']
    archivo_2 = request.files['archivo_2']

    path_1 = os.path.join(UPLOAD_FOLDER, archivo_1.filename)
    path_2 = os.path.join(UPLOAD_FOLDER, archivo_2.filename)

    archivo_1.save(path_1)
    archivo_2.save(path_2)

    try:
        # Leer archivos con polars
        df1 = pl.read_csv(path_1)
        df2 = pl.read_excel(path_2)  # Si es Excel, asegúrate de tener openpyxl

        # Aquí podrías hacer cualquier procesamiento con polars
        total_filas_1 = df1.height
        total_filas_2 = df2.height

        # 🚨 Eliminamos los archivos luego de procesarlos
        os.remove(path_1)
        os.remove(path_2)

        return jsonify({
            "message": "Archivos cargados y procesados correctamente",
            "archivo_1_filas": total_filas_1,
            "archivo_2_filas": total_filas_2
        }), 200

    except Exception as e:
        # Si falla algo, igual intentamos limpiar archivos si existen
        if os.path.exists(path_1):
            os.remove(path_1)
        if os.path.exists(path_2):
            os.remove(path_2)

        return jsonify({"error": f"Error al procesar los archivos: {str(e)}"}), 500