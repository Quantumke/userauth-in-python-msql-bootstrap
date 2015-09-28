#import the fask module
from flask import Flask
app = Flask(__name__)
#define the basic route
 #import render template
from flask import Flask, render_template
    #modified the main method to return the renderd template
@app.route("/")
def main():
        return render_template('index.html')
if __name__ == "__main__":
    app.run()
    
   
    