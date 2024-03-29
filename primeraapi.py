import string
from flask import Flask, jsonify, request

app = Flask(__name__)

from videojuegos import videojuegos


@app.route('/')
def hola():
    return "grupo 3-A"


@app.route('/videojuegos', methods=['GET'])
def getProdu():
    return jsonify(videojuegos)


@app.route('/videojuegos/<string:videojuego_name>', methods=['GET'])
def getvideo(videojuego_name):

    catalogo = [video for video in videojuegos if video['name'] == videojuego_name.lower()]
    if len(catalogo) > 0:
        return jsonify({"videojuegos": catalogo[0]})
    return jsonify({"message": "videojuego no encontrado"})


@app.route('/consola/<string:consola_name>', methods=['GET'])
def getvideoconsola(consola_name):
    consola1=[]
    for juego in videojuegos:
        if  juego['consola'] == consola_name.lower():
            juego_aux=juego
            consola1.append(juego_aux)
        else:
            print("no coincide")
    if len(consola1) > 0:
        return jsonify({"Video juegos": consola1})
    return jsonify({"Mensaje": "No existen video juegos para la consola"})

@app.route('/nuevojuego', methods=['POST'])
def addvideo():
    new_juego = {
        "codigo": request.json['codigo'],
        "name": request.json['name'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad'],
        "consola": request.json['consola']
    }
    print (new_juego)
    videojuegos.append(new_juego)
    return jsonify({"message": "videojuego agregado", 'videojuegos': videojuegos})

@app.route('/actualizarjuego/<int:videojuego_codigo>', methods=['PUT'])
def editvideo(videojuego_codigo):
    actual = [video for video in videojuegos if video['codigo'] == videojuego_codigo]
    if len(actual) > 0:
        actual[0]['codigo'] = request.json['codigo'],
        actual[0]['name'] = request.json['name'],
        actual[0]['precio'] = request.json['precio'],
        actual[0]['cantidad'] = request.json['cantidad'],
        actual[0]['consola'] = request.json['consola']
        return jsonify({
            "message": "videojuego actualizado",
            "videojuegos": actual[0]
        })
    return jsonify({"message": "videojuego no encontrado"})

@app.route('/eliminarjuego/<int:videojuego_codigo>', methods=['DELETE'])
def deletevideo(videojuego_codigo):
    eliminarvideo = [video for video in videojuegos if video['codigo'] == videojuego_codigo]
    if len(eliminarvideo) > 0:
        videojuegos.remove(eliminarvideo[0])
        return jsonify({
            'message': 'videojuego eliminado',
            'videots': videojuegos
        })
    return jsonify({"message": "no encontrado"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)