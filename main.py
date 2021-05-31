from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
# configuración key - documentación socketio
app.config['SECRET_KEY'] = 'secret'
# iniciamos el socket
socketio = SocketIO(app)

# endpoint raíz - flask
@app.route('/', methods=['GET'])
def main_path():
    return render_template('index.html')

# evento para recibir información y retornarla
@socketio.on('message')
def get_message(message):
    print('message: {msm}'.format(msm=message))
    send(message, broadcast=True)

# escuchar la aplicación en caso de ser el mismo archivo
if __name__ == '__main__':
    socketio.run(app)

