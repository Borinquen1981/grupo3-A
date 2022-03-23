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
    if (len(catalogo) > 0):
        return jsonify({"videojuegos": catalogo[0]})
    return jsonify({"message": "videojuego no encontrado"})

@app.route('/consola/<string:consola_name>', methods=['GET'])
def getvideoconsola(consola_name):
    catalogo = [video for video in videojuegos if video['consola'] == consola_name.lower()]
    if (len(catalogo) > 0):
        return jsonify({"videojuegos": catalogo[0]})
    return jsonify({"message": "videojuego no encontrado"})


@app.route('/videojuegos', methods=['POST'])
def addvideo():
    #print(request.json)
    new_juego = {
        "name": request.json['name'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad']
    }
    videojuegos.append(new_juego)
    #return 'recibido'
    return jsonify({"message": "videojuego agregado", 'videojuegos': videojuegos})
#actualizar dato

@app.route('/videojuegos/<string:videojuego_name>', methods=['PUT'])
def editvideo(videojuego_name):
    actual = [video for video in videojuegos if video['codigo'] == videojuego_name]
    if (len(actual) > 0):
        actual[0]['codigo'] = request.json['codigo'],
        actual[0]['name'] = request.json['name'],
        actual[0]['precio'] = request.json['precio'],
        actual[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "message": "videojuego actualizado",
            "videojuegos": actual[0]
        })
    return jsonify({"message": "videojuego no encontrado"})
#metodo delete

@app.route('/videojuegos/<string:videojuego_name>', methods=['DELETE'])
def deletevideo(videojuego_name):
    eliminarvideo = [video for video in videojuegos if video['name'] == videojuego_name]
    if len(eliminarvideo) > 0:
        videojuegos.remove(eliminarvideo[0])
        return jsonify({
            'message': 'videojuego eliminado',
            'videots': videojuegos
        })
    return jsonify({"message": "no encontrado"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
