import os, httpApp, app
from threading import Thread

def sslContext():
        privKey = r'/home/dion-frankes/Downloads/slimme-rattenval-IOT/flask-iot-webserver/ssl/kickinganimal.nl/privatekey.pem'
        cert = r'/home/dion-frankes/Downloads/slimme-rattenval-IOT/flask-iot-webserver/ssl/kickinganimal.nl/cert.pem'
        return (cert, privKey)

def httpsServer():
    app.app.run(debug=False, host='0.0.0.0',port=5000, ssl_context=sslContext(), use_reloader=False)

def httpServer(): 
    app.app.run(debug=False, host='0.0.0.0',port=4000, use_reloader=False)

Thread(target = httpServer).start()
Thread(target = httpsServer).start()
