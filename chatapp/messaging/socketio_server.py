import socketio
import eventlet

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
app = socketio.WSGIApp(sio)
#global socketio
socketio = sio

@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")

@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")

@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    sio.emit('new_message', data)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
    

