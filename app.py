from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(username, email) VALUES (%s, %s)", (username, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/users')
def users():
    cur =mysql.connection.cursor("SELECT * FROM users")

    if users > 0:
        usersDetails = cur.fetchall()

        return render_template('users.html',usersDetails=usersDetails)

if __name__ == '__main__':
    app.run(host ="0.0.0.0",port=80)      