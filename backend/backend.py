from flask import Flask, jsonify
import env

app = Flask(__name__)

mvnos = env.MVNOS

@app.route("/obtener_datos")
def obtener_datos():
    # Puedes conectar a base de datos o lógica aquí
    return jsonify({"nombre": "Carlos Jr.", "mensaje": "¡Hola desde el servidor!"})

@app.route("/colores")
def colores():
    return jsonify({
        "themes": {
            "bgcolor": "#F9F8FA",
            "dark_white": "#E7E6E9",
            "grey_color": "#A9ACb6",
            "dark_page": "#320E5B",
            "yellow_color": "#ECE5D5"
            },
        "menu": {
            "width": 1500,
            "height": 40,
            "bgcolor": "#a9acb6",
            "buttons": [
                    {"text": "Inicio", "icon": "home"},
                    {"text": "Reportes", "icon": "report"},
                    {"text": "Configuración", "icon": "settings"},
                    {"text": "Ayuda", "icon": "help"}
                ]
            }
        })

@app.route("/formulario")
def formulario():
    return jsonify({
        "container": {
            "width": 400,
            "height": 700,
            "margin": 5,
            "bgcolor": "#ECE5D5",
            "border_radius": 10
        },
        "title": {
            "text": "Gestor de Comisiones",
            "size": 20,
            "weight": "bold",
            "color": "#320E5B"
        },
        "image": {
            "src": "https://solecybernetic.pythonanywhere.com/static/images/saturno.png",
            "width": 80,
            "height": 80
        },
        "labels": {
            "archivo_finanzas": "Selecciona el reporte de finanzas de la marca",
            "archivo_general": "Selecciona el reporte de general ACT/REC"
        },
        "dropdowns": {
            "marca": mvnos,
            "sales": ["SI", "NO"],
            "proceso": ["Activación", "Recarga"],
            "comision": ["20%", "15%"]
        },
        "fecha_default": "31-12-2025",
        "procesar_button": {
            "text": "Procesar",
            "bgcolor": "#2cc736",
            "width": 200,
            "color": "#E7E6E9",
            "icon": "play_arrow"
        },
        "loader_visible": False
    })

@app.route("/info-proceso")
def info_proceso():
    return jsonify({
        "info_proceso": {
            "mensaje": "Aquí se mostrará la información procesada.\nPuedes copiar este texto.\nResultado total: 150 líneas procesadas.\nTiempo de procesamiento: 2.5 segundos.\n\n¡Gracias por usar el gestor de comisiones!\n\nRecuerda que puedes volver a cargar los archivos y procesar nuevamente.",
            "icono": "hourglass_empty",
            "color": "#320E5B"
        }
    })

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})

"""if __name__ == '__main__':
    app.run(debug=True)"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)