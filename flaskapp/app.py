#import the fask module
from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
app = Flask(__name__)

#define the basic route

 #import render template

    #modified the main method to return the renderd template
@app.route("/")
def main():
     return render_template('index.html')
@app.route('/showSignUp')
def showSignUp():
     return render_template('signup.html')
@app.route('/signup', methods=['POST'])

    
@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
    app = Flask(_name_)
    #DB CONFIG
    mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'master12!'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
    #establishing a connection
conn = mysql.connect()
cursor = conn.cursor()
_hashed_password = generate_password_hash(_password)
cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
data = cursor.fetchall()

if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
else:             
                 return json.dumps({'error':str(data[0])})       
else:
                 return json.dumps({'html':'<span>Enter the required fields</span>'})

    
     
			
			