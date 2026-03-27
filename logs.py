from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

notes_storage = {}

@app.route('/')
def home():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/log')
def log_page():
    return render_template('log.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        session['username'] = username
        if username not in notes_storage:
            notes_storage[username] = []
        return redirect('/')
    return redirect('/log')

@app.route('/add-notes')
def add_notes():
    username = session.get('username')
    notes = notes_storage.get(username, [])
    return render_template('add-notes.html', username=username, notes=notes)

@app.route('/add-note', methods=['POST'])
def add_note():
    username = session.get('username')
    note = request.form.get('note')
    if username and note:
        if username not in notes_storage:
            notes_storage[username] = []
        notes_storage[username].append(note)
    return redirect('/add-notes')

@app.route('/search-notes')
def search_notes():
    return render_template('search-notes.html')

@app.route('/math-notes')
def math_notes():
    # Mock data for math content
    math_content = {
        "Map Scale Drawing": "Scale drawings show real objects in proportional size...",
        "Equations": "An equation shows two expressions are equal..."
    }
    return render_template('math_notes.html', math_content=math_content)

if __name__ == '__main__':
    app.run(debug=True)