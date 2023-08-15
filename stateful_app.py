from flask import Flask, request, jsonify, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Initialize the database
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/notes", methods=["GET", "POST"])
def handle_notes():
    if request.method == "GET":
        conn = sqlite3.connect('notes.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, content, timestamp FROM notes ORDER BY timestamp DESC')
        notes = [{'id': id, 'content': content, 'timestamp': timestamp} for id, content, timestamp in cursor.fetchall()]
        conn.close()
        return jsonify(notes)
    elif request.method == "POST":
        content = request.json.get("content")
        if content:
            conn = sqlite3.connect('notes.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO notes (content) VALUES (?)', (content,))
            conn.commit()
            conn.close()
            return jsonify({"message": "Note added successfully"})
        else:
            return jsonify({"error": "Note content is required"}), 400

if __name__ == "__main__":
    app.run(debug=True)
