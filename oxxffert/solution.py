#!/usr/bin/python3


# from distutils.log import debug
from crypt import methods
from unittest import result
import flask
from flask import Flask , render_template
from flask import request
import sys 
import math

from numpy import char 


app = Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")



@app.route('/clubsters', methods=["POST"])
def clubsters():
    if request.method == "POST":
        charger = request.form["value_1"]
        #evaluator = str(request.form['result'])
        def buildman(operation):
            
            mmmaker =  eval(operation)
            # print(mmmaker)
            # if str(operation):
            # buildman(eval("operation"))

                # print(f'result --> {make}')
        # buildman(charger)
        # operr = buildman--(charger)
        if str(charger):
            make = eval(charger)
            print(float(make))
            return render_template("index.html", result=float(make))
        # return render_template("index.html", )
    # pass
@app.route('/strangerman', methods=["POST"])
def strangerman():
    if request.method == "POST":
        kwork = int(request.form["sq_raiz"])
        if int(kwork):
            pth = math.sqrt(kwork)          
            return render_template('index.html', ravengold=pth)


app.run(debug=True)
if __name__ == "__main__":
    clubsters()
    strangerman()
    main()
    # pass