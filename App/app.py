from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data_users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 email TEXT NOT NULL,
                 dob DATE NOT NULL)''')
    conn.commit()
    conn.close()


@app.route('/', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')

@app.route('/signup', methods=['POST'])
def register_user():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    dob = request.form['dob']

    if not name or not age or not email or not dob:
        return "All fields are required."

    try:
        age = int(age)
    except ValueError:
        return "Age must be a valid integer."

    try:
        conn = sqlite3.connect('data_users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, age, email, dob) VALUES (?, ?, ?, ?)",
                  (name, age, email, dob))
        conn.commit()
        conn.close()
    except Exception as e:
        return f"An error occurred: {str(e)}"

    return redirect(url_for('display_users'))

@app.route('/users', methods=['GET'])
def display_users():
    conn = sqlite3.connect('data_users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template('user_table.html', users=users)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
