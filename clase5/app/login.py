from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST']) 
def llamarServicioSet(): 
    user = request.json.get('user') 
    password = request.json.get('password') 

    codRes, menRes, accion = inicializarVariables(user, password) 

    salida = { 
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion 
    } 
    return jsonify(salida)

def inicializarVariables(user, password):
    userlocal= "unida"
    password= "unida123"
    codRes = 'SIN_ERROR'
    menRes = 'ok'

    try:
        print= ("verificar login")
       if password == passlocal and user == userlocal:
            print("Usuario y contraseña ok")
            accion = "Success"
        else:
            print("usuario o contraseña incorrecta")
            accion = "usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales o usuario incorrectas'
       

    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"
    
    return codRes, menRes, accion