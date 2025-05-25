from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login = Blueprint('login', __name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost', # Cambia esto si tu base de datos está en un contenedor Docker
    'user': 'unida', # Reemplaza con tu usuario de base de datos
    'password': 'unida123', # Reemplaza con tu contraseña de base de datos
    'database': 'jaguarete' # Reemplaza con el nombre de tu base de datos
}


