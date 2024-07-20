from flask import Flask ,render_template,request,redirect
# from flask_pymongo import PyMongo
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['medicalAI']
collection = db['userdata']


app = Flask(__name__)



@app.route("/", methods =['POST','GET'])
def home():
    return render_template("index.html")


@app.route("/signup", methods =['POST','GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        #inserting into datbase
        info ={"username":username,"email":email,"password":password}
        collection.insert_one(info)

        return redirect("/")

        

    return render_template("signup.html")


@app.route("/login", methods =['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = collection.find_one({'username':username},{"password":password})
        if user :
            return redirect("/")
        else :
            flag =1
            return render_template("login.html",flag =flag)    
        # results = collection.find({username: {'$exists': True},password: {'$exists': True}})


    
    return render_template("login.html")



if __name__ =='__main__':
    app.run(debug=True)