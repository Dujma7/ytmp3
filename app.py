from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import yt_dlp
import os   
app = Flask(__name__)
CORS(app, resources={r"/download": {"origins": "*"}})

folder = "C:\\Users\\zvonk\\OneDrive\\Dokumente\\YTMP3"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods=["POST"])
def downloadYouTubeVideo():
    link = request.json.get("link")
    ydl_opts = {
        "format":"bestaudio/best",
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'ffmpeg_location': "C:\\ffmpeg"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    return jsonify({"status":"success", "message":"Download completed"})

if __name__ == '__main__':
    app.run(debug=True)