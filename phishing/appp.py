# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:37:43 2020

@author: Gokul
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:19:52 2020

@author: Gokul
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load

app = Flask(__name__)
model = pickle.load(open('decisonp.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    name=[x for x in request.form.values()]
    print(name)
    x_test = [[float(x) for x in name]]
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==-1):
        pred='There are high probability of it being a phising website'
    else:
        pred="There are less probability of it being a phising website"
    return render_template('main.html', prediction_text='{}'.format(pred))

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
