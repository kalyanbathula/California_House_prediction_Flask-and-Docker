import pickle
from flask import Flask,app,jsonify,url_for,render_template,request,Response
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('regmodel.pkl','rb'))
scalar = pickle.load(open('scaling.pkl','rb'))

@app.route('/api/v1')
def home():
    return render_template('home.html')

@app.route('/api/v1/predict',methods = ['POST'])

def predict_api():
    data = request.json['data']
    print("Hello")
    print(data)
    print(data.values())
    return jsonify({
        "message":"Hello"
    })


if __name__=="__main__":
    app.run(debug=True)
