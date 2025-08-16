from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, content FROM notes ORDER BY id DESC;")
    notes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note = request.form['note']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO notes (content) VALUES (%s);", (note,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_note.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
