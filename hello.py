# from flask import Flask

# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)

from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download-audio', methods=['GET'])
def download_audio():
    # Replace 'path_to_audio_file' with the actual path to your audio file
    audio_file_path = 'audio/demo.mp3'
    
    return send_file(audio_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)