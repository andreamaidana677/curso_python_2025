'''tst de cambiko'''
from flask import Blueprint, request, jsonify 
login = Blueprint('login', _name__) 

@login.route('/login', methods=['POST']) 
def llamarServicioSet(): 
    user = request.json.get('user') 
    password = request.json.get('password') 

    codRes, menRes, accion = inicializarVariables(user, password) 

salida = { 
'codRes': 
    'codRes': codRes, 
    'menRes': menRes, 
    'usuario': user, 
    'accion': accion 
} 
return jsonify(salida)

def inicializarVariables(user, password):
    userLocal = "unida"
    passLocal = "unida123"
    codRes = 'SIN_ERROR'
    mentes = 'ok'

    try:
        prin("verificar login")
        if password == passLocal and user == userLocal:
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'credenciales o usuario incorrectas'


    except Excepcion as e:
        print("Error", str(e))
        codRes = 'Error'
        menRes = 'Msg' +str(e)
        accion = "error interno"

    return codRes, menRes, accion