#import the fask module
from flask import Flask
app = Flask(__name__)
#define the basic route
@app.route("/")
def main():
    return "Welcome!"
if __name__ == "__main__":
    app.run()