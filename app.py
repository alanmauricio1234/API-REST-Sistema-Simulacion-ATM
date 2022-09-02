from flask import Flask, jsonify, request
from models import find_card
from datetime import date

app = Flask(__name__)



@app.route('/banco/consulta_tarjeta/<string:n_tarjeta>')
def consulta_tarjeta(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    esta_tarjeta = False
    if (tarjeta):
        esta_tarjeta = True
    
    return jsonify({'Tarjeta': {
            'esta_tarjeta': esta_tarjeta
        }})

@app.route('/banco/verifica_tarjeta/<string:n_tarjeta>')
def verifica_tarjeta(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    esta_tarjeta = False
    es_verificada = False
    if tarjeta:
        esta_tarjeta = True
        es_verificada = tarjeta['es_verificada']
    
    return jsonify(
        {'Tarjeta': {
            'esta_tarjeta': esta_tarjeta,
            'es_verificada': es_verificada
        }})

@app.route('/banco/tarjeta_bloqueada/<string:n_tarjeta>')
def verifica_tarjeta_bloqueada(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    esta_tarjeta = False
    es_bloqueada = False
    if tarjeta:
        esta_tarjeta = True
        es_bloqueada = tarjeta['es_bloqueada']

    return jsonify({
        'Tarjeta': {
                'esta_tarjeta': esta_tarjeta,
                'es_bloqueada': es_bloqueada
            }
    })

@app.route('/banco/verifica_fecha/<string:n_tarjeta>')
def verifica_fecha(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    esta_tarjeta = False
    fecha_verificada = False
    if tarjeta:
        esta_tarjeta = True
        if date.today() < tarjeta['f_vencimiento']:
            fecha_verificada = True
    
    return jsonify({
        'Tarjeta': {
            'esta_tajeta': esta_tarjeta,
            'fecha_verificada': fecha_verificada
        }
    })


@app.route('/banco/verifica_nip/<string:n_tarjeta>/<int:nip>')
def verifica_nip(n_tarjeta, nip):
    tarjeta = find_card(n_tarjeta)
    es_correcto_nip = False
    esta_tarjeta = False
    if tarjeta:
        esta_tarjeta = True
        if nip == tarjeta['nip']:
            es_correcto_nip = True
            tarjeta['intento'] = 0
        else:
            tarjeta['intento'] += 1
        if tarjeta['intento'] >=3:
            tarjeta['es_bloqueada'] = True
    
    return jsonify({
        'Tarjeta': {
            'esta_tarjeta': esta_tarjeta,
            'es_correcto_nip': es_correcto_nip
        }
    })

@app.route('/banco/consulta_intentos/<string:n_tarjeta>')
def consulta_intentos(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    intentos = -1
    esta_tarjeta = False
    if tarjeta:
        intentos = tarjeta['intento']
        esta_tarjeta = True
    return jsonify({
        'Tarjeta': {
            'esta_tarjeta': esta_tarjeta,
            'intentos': intentos
        }
    })

@app.route('/banco/verifica_limite/<string:n_tarjeta>')
def verifica_limite(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    limite = -1
    esta_tarjeta = False
    if tarjeta:
        limite = tarjeta['limite']
        esta_tarjeta = True
    return jsonify({
        'Tarjeta': {
            'esta_tarjeta': esta_tarjeta,
            'limite': limite
        }
    })

@app.route('/banco/consulta_saldo/<string:n_tarjeta>')
def consulta_saldo(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    saldo = 0
    esta_tarjeta = False
    if tarjeta:
        saldo = tarjeta['saldo']
        esta_tarjeta = True
    
    return jsonify({
        'Tarjeta': {
            'esta_tarjeta': esta_tarjeta,
            'saldo': saldo
        }
    })

@app.route('/banco/realiza_pago/<string:n_tarjeta>', methods=['POST'])
def realiza_pago(n_tarjeta):
    tarjeta = find_card(n_tarjeta)
    result = 0.0
    esta_tarjeta = False
    pago = request.json['pago']
    if tarjeta:
        esta_tarjeta = True
        if pago <= tarjeta['limite'] and pago <= tarjeta['saldo']:
            tarjeta['saldo'] -= pago
            result = tarjeta['saldo']
    
    return jsonify({
        'Tarjeta': {
            'esta_tarjeta': esta_tarjeta,
            'pago': result
        }
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)