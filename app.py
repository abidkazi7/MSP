# -*- coding: utf-8 -*-
"""
Created on Wed July  12 23:10:16 2023

@author: Sanket Khedkar
"""

from flask import Flask,render_template,redirect,url_for,request
from Aj_new_function import read_dataset
import numpy as np
app= Flask(__name__)

crops_path = {1: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Rice.csv',
            2: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Maize.csv',
            3: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Groundnut.csv',
            4: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Moong.csv',
            5: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Urad.csv',
            6: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Soyabean.csv',
            7: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Jowar.csv',
            8: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Tur.csv',
            9: 'DataSet/Data_Main6_with_CostP_Imp_InP_Single_Cotton.csv'
            }

@app.route('/')
def Home():
    return render_template('layout.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')
@app.route('/about')
def about():
    return render_template('')

@app.route('/predict',methods=['GET','POST'])
def predict():
    
    crop=int(request.args.get('Crops'))
    
    yr=int(request.args.get('year'))
    
    print(crop,yr)
       
    data=read_dataset(crops_path[crop],crop,yr,yr,yr,yr)
    
    return render_template('crop-result.html',prediction = data)


if __name__ == "__main__":
    app.run()
    
    