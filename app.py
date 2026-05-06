from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database and users table
def init_db():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            role TEXT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Home route
@app.route('/')
#def home():
    #return redirect('/register')


# Register page
@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            return "Login Successful!"
        else:
            return "Invalid Username or Password"

    return render_template("login.html")


# Handle registration form
@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    phone = request.form['phone']
    role = request.form['role']
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO users 
            (firstname, lastname, email, phone, role, username, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (firstname, lastname, email, phone, role, username, password))

        conn.commit()

    except sqlite3.IntegrityError:
        return "Username or Email already exists!"

    finally:
        conn.close()

    return redirect('/login')

@app.route('/admin')
def admin():
    conn = sqlite3.connect("hospital.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            id,
            firstname,
            lastname,
            email,
            phone,
            role,
            username
        FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    return render_template("admin.html", users=users)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)




    
