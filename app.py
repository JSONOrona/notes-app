from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

notes = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/notes", methods=["GET", "POST"])
def handle_notes():
    if request.method == "GET":
        return jsonify(notes)
    elif request.method == "POST":
        content = request.json.get("content")
        if content:
            note = {"content": content, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            notes.append(note)
            return jsonify({"message": "Note added successfully"})
        else:
            return jsonify({"error": "Note content is required"}), 400

if __name__ == "__main__":
    app.run(debug=True)
