from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db= SQLAlchemy(app)


class Employee(db.Model):
    
    id = db.Column(db.Integer,primary_key = True,auto_increment = True)
    name = db.Column(db.String,nullable = False)
    email = db.Column(db.String,nullable = False)
    
with app.app_context():
    db.create_all()
    
@app.route("/employee", methods = ["POST"])   
def createemp():
    emp = request.get_json()
    
    res = Employee(name = emp["name"], email = emp["email"])
    
    db.session.add(res)
    db.session.commit()
    
    return jsonify({"message" : "your data added successfully"})
    
def hello():
    return "new change"




if __name__ == "__main__":
    app.run(debug= True)