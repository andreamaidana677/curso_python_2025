from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])

def llamarservicioSet():
    ci = request.json.get('ci')
    

    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': ci,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(ci):
    ciLocal = '4133266'
    codRes='SIN_ERROR'
    menRes= 'ok'

    try:
        
        if ci == ciLocal:
            print("usuario ok")
            accion = "Success"
        else:
            accion = "Usuario o contraseña incorrecta"
            codRes ='ERROR'
            menRes ="Error cliente"
            ci ='4133266'

    except Exception as e:
        print("ERROR", str(e))
        codRES = "Error interno"

    return codRes , menRes , accion