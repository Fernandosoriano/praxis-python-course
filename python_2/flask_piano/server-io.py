from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from note_manager import Note_Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

sound_strem = Note_Manager()
key_note={
    "z":"C",
    "x":"D",
    "c":"E",
    "v":"F",
    "b":"G",
    "n":"A",
    "m":"B",
    ",":"C",
}

###
### MAIN PAGE SERVER
###
@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('key')
def key_press(data):
    if(data["key"]==','):
        sound_strem.run(key_note[data['key']],5,"N")
    else:
        sound_strem.run(key_note[data['key']],4,"N")

    # print(data['key'])

###
### MAIN FUNCTION
### 
if __name__ == '__main__':
    sound_strem.init_stream()
    socketio.run(app,port=5400)


