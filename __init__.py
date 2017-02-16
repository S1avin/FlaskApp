
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql=MySQL(app)


"""
app.config['MYSQL_DATABASE_USER'] = 'Slavin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'World202web'
app.config['MYSQL_DATABASE_DB'] = 'Slavin$Inventory'
app.config['MYSQL_DATABASE_HOST'] = 'Slavin.mysql.pythonanywhere-services.com'
mysql.init_app(app)

db = mysql.connect(host="Slavin.mysql.pythonanywhere-services.com", user="Slavin", passwd="Google103", db="Slavin$Inventory")
cur = db.cursor()

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/view/', methods=["POST", "GET"])
def view():
    if request.method == 'POST':
        invid = request.form['invid']
        return render_template("view.html", invid = invid)

@app.route('/enter/', methods=["GET", "POST"])
def enter():
    return render_template("enter.html")

@app.route("/test/")
def student():
   return render_template("student.html")

@app.route('/result/', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

"""
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view", methods=['GET', 'POST'])
def view():
    return render_template("view.html")

@app.route("/enter", methods=['GET', 'POST'])
def enter():
    try:
        con = mysql.connect("Slavin.mysql.pythonanywhere-services.com","Slavin","Google103","Slavin$Inventory" )
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
        con = mysql.connect("Slavin.mysql.pythonanywhere-services.com","Slavin","Google103","Slavin$Inventory" )
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
@app.route("/echo", methods=['POST'])
def echo():
    text=request.form['text']
    cur.execute("SELECT * FROM Item WHERE invid = text")
    data = cur.fetchall()
    db.close
    return render_template('echo.html', text = data)
"""
if __name__ == '__main__':
    app.debug = True
    app.run()
