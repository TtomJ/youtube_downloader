from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        choice = request.form.get("choice")

        if not url.startswith("http"):
            return "Invalid URL. Please enter a valid YouTube link."

        if choice == "video":
            command = ["yt-dlp", "-f", "best", url]
        elif choice == "audio":
            command = ["yt-dlp", "-f", "bestaudio", "-x", "--audio-format", "mp3", url]
        else:
            return "Invalid choice."

        subprocess.run(command)
        return "Download Started!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
