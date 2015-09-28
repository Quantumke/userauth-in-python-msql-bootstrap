#import the fask module
from flask import Flask
app = Flask(__name__)
#define the basic route
 #import render template
from flask import Flask, render_template, json, request
    #modified the main method to return the renderd template
@app.route("/")
def main():
     return render_template('index.html')
@app.route('/showSignUp')
def showSignUp():
     return render_template('signup.html')
@app.route('/signup' methods=['POST'])
def signup():
    #read the posted values
    _name = request.form['inputName']
    _email -request.from['inputEmail']
    _password =request.form['inputPassword']
    #Validae the recieved values:
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
if __name__ == "__main__":
    app.run()
    
    