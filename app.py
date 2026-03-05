from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# This event listens for drawing coordinates from any client
@socketio.on('draw')
def handle_draw(data):
    # Broadcast the data to everyone else connected
    emit('draw_received', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)