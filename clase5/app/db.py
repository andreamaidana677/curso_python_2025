import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",               # o el usuario que usás
        password="unida123",  # ← reemplazá esto
        database="jaguarete"
    )
