from flask import Flask,render_template,request
import requests
import os

app=Flask(__name__)


@app.route("/")
def index():
    x=os.listdir('static/')
    return render_template("index.htm",tech=x)
    


if __name__=="__main__":
    app.run(debug=True)

