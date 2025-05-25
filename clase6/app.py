from flask import flask, render_template

app = Flak(____name__)

@login.route('/') 
def dashboart():
    datos = {
        'usuarios':120,
        'ms': menRes,
        'usuario': user,
        'accion': accion 





    }
    user = request.json.get('user') 
    password = request.json.get('password') 

    codRes, menRes, accion = inicializarVariables(user, password) 

    salida = { 
        'codRes': codRes,
        'menRes': menRes,
        'usuario': user,
        'accion': accion 
    } 