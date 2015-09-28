#import the fask module
from flask import Flask
app = Flask(__name__)
#define the basic route
@app.route("/")
def main():
    return "Welcome!"
if __name__ == "__main__":
    app.run()
    
    #import render template
    from flask import Flask, render_template
    #modified the main methodto return the renderd template
    def main():
        return render_template('index.html')