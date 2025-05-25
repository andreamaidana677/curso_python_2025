# cliente.py

# Simulación de base de datos de clientes
clientes = {
    "4133266": {
        "nombre": "Andrea Montserrat Maidana"
    }
}

def buscar_cliente(ci):
    return clientes.get(ci, None)