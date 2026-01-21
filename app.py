from flask import Flask,render_template,url_for,request,redirect
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

@app.route("/addstudent", methods = ["GET","POST"])
def addstudent():
    con= mysql.connection.cursor()
    if  request.method == "POST":
        stu_name = request.form["stu_name"]
        age = request.form["age"]
        address = request.form["address"]
        
        sql = "insert into  student_details (student_name,Age,Address) values (%s,%s,%s)"
        
        con.execute(sql,[stu_name,age,address])
        
        mysql.connection.commit()
        con.close()
        return redirect(url_for("displaystudents"))
    
    return render_template("addstudent.html")

@app.route("/updateStudent/<int:id>", methods = ["GET","POST"])
def updateStudent(id):
    con = mysql.connection.cursor()
    if request.method == "POST":
        stu_name = request.form["stu_name"]
        age = request.form ["age"]
        address = request.form["address"]
        
        sql = "update student_details set student_name = %s, Age = %s, Address = %s where id= %s"
        con.execute(sql,[stu_name,age,address,id])
        mysql.connection.commit()
        return redirect(url_for("displaystudents"))
    
    sql = "SELECT * FROM STUDENT_DETAILS WHERE ID = %s"
    con.execute(sql,[id])
    res = con.fetchone()
    
    return render_template("updatestudent.html",a = res)


@app.route("/deleteStudent/<int:id>")
def deleteStudent(id):
    
    con = mysql.connection.cursor()
    
    sql = "delete from student_details where id = %s"
    
    con.execute(sql,[id])
    mysql.connection.commit()
    return redirect(url_for("displaystudents"))




# if __name__ == "__main__":
#     app.run(debug=True)