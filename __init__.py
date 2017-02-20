
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
#
#
app = Flask(__name__)
#mysql=MySQL(app)



@app.route("/")
def index():
    return render_template('index.html')

"""
@app.route("/view", methods=['GET', 'POST'])
def view():
    return render_template("view.html")

@app.route("/enter", methods=['GET', 'POST'])
def enter():
    try:
        con = mysql.connect("xxxx","xxx","xxxx","xxxx" )
        things = []
        with con:
            cur = con.cursor()
            invid = request.form['invid']
            Location = request.form["Location"]
            things = [invid, Location]
            cur.executemany("INSERT INTO Item(invid,Location) VALUES(?,?)", things)
            con.commit()
            return render_template("enter.html")
    except Exception as e:
        return(str(e))

@app.route("/add", methods=['GET', 'POST'])
def adding():
    try:
        con = mysql.connect("xxxx","xxx","xxxx","xxxx" )
        things = []
        with con:
            cur = con.cursor()
            invid = request.form['invid']
            Location = request.form["Location"]
            Title = request.form["Title"]
            things = [invid, Location, Title]
            cur.executemany("INSERT INTO Item(invid,Location,Title) VALUES(?,?,?)", things)
            con.commit()
            return render_template("enter.html")
    except Exception as e:
        return(str(e))

"""

if __name__ == '__main__':
    app.debug = True
    app.run()
