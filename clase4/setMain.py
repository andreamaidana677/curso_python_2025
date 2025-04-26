#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Línea shebang: permite ejecutar este script directamente en sistemas Unix/Linux
# Codificación UTF-8 para permitir caracteres especiales

from flask import Flask, jsonify, request
# Importamos Flask para crear la app web, jsonify para devolver respuestas en JSON
# y request para manejar datos entrantes (por ejemplo, de formularios o JSON)

app = Flask(__name__)
# Creamos la instancia de la aplicación Flask

@app.route('/', methods=['GET'])
def hello():
    # Definimos una ruta para el endpoint raíz "/" que responde a solicitudes GET
    return 'Hello World!'
    # Al acceder a la raíz del sitio, se devuelve este mensaje

if __name__ == "__main__":
    # Este bloque se ejecuta solo si el script se ejecuta directamente (no importado como módulo)
    # Ejecuta la app en el host 0.0.0.0 para que sea accesible desde otras máquinas
    # Modo debug activado para ver errores detallados
    app.run(host='0.0.0.0', port=5000, debug=True)

