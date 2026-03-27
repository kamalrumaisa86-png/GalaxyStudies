from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Temporary in-memory user storage (Reset on server restart)
users = {"admin": "password123"}
# Personal notes storage: { username: [list_of_notes] }
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

@app.route('/search-notes')
def search_notes():
    return render_template('search-notes.html')

@app.route('/english')
def english_page():
    return render_template('english.html')

@app.route('/grammar')
def grammar_page():
    return render_template('grammer.html')

@app.route('/reading')
def reading_page():
    query = request.args.get('q', '').lower()
    return render_template('reading.html', query=query)

