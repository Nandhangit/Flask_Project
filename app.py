from flask import Flask,render_template,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] ="Nandhan@2005"
app.config["MYSQL_DB"] = "flask_database"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


# @app.route("/home/<name>/<int:age>")
# def homepage(name,age):
#     return f"<h1>Welcome to {name} and your age is {age}</h1>"


@app.route("/home")
def homepage():
    
    name = "ram"
    
    subject = ["Tamil","english","Maths","science","social"]
    
    # background = color
    
    
    return render_template("home.html",a= name, b= subject)

@app.route("/projects")
def projectpage():
    
    return render_template("projects.html")


@app.route("/contact")
def contactpage():
    
    return render_template("contact.html")
    
@app.route("/about")
def aboutpage():
    
    return render_template("about.html")
    
@app.route("/skills")
def skillspage():
    return render_template("skills.html")

@app.route("/display")
def displaystudents():
    con = mysql.connection.cursor()
    sql = "Select * from student_details"
    con.execute(sql)
    res =con.fetchall()
    
    
    
    return render_template("studisplay.html",a =res)



if __name__ == "__main__":
    app.run(debug=True)