from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


def connect():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root1234',
        db='project_db',
        port=3306,
    )
    return connection


@app.route('/')
def hello_world():
    return render_template("admin/index.html")


@app.route('/viewUser')
def viewUser():
    return render_template("admin/viewUser.html")


@app.route('/addArea')
def addArea():
    return render_template("admin/addArea.html")


@app.route('/viewArea')
def viewArea():
    return render_template("admin/viewArea.html")


@app.route('/viewBranch')
def viewBranch():
    return render_template("admin/viewBranch.html")


@app.route('/viewVideos')
def viewVideos():
    return render_template("admin/viewVideos.html")


@app.route('/viewComplaints')
def viewComplaints():
    return render_template("admin/viewComplaints.html")


@app.route('/complaintReply')
def complaintReply():
    return render_template("admin/complaintReply.html")


@app.route('/viewFeedbacks')
def viewFeedbacks():
    return render_template("admin/viewFeedbacks.html")


@app.route('/Login')
def Login():
    return render_template("admin/login.html")


@app.route('/register')
def Register():
    return render_template("admin/register.html")


@app.route('/userinfo', methods=['POST'])
def userinfo():
    if request.method == 'POST':
        fname = request.form.get('fname')
        email = request.form.get('email')
        country = request.form.get('country')
        password = request.form.get('password')
    connection = connect()
    cursor1 = connection.cursor()

    cursor1.execute(
        "insert into register_db (FirstName, Email, Country, Password)"
        " values ('{}','{}','{}','{}')".format(fname, email, country, password))

    connection.commit()
    return render_template('admin/index.html')


if __name__ == '__main__':
    app.run(debug=True)
