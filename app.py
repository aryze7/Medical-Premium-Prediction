import uvicorn 
from fastapi import FastAPI
import numpy as np 
import joblib
import pandas as pd
from PremiumVars import PremiumVars

api = FastAPI()

classifier_rf = joblib.load("D:/JUPYTER/Projects/Medical-Premium-Prediction/rf.sav")
classifier_xg = joblib.load("D:/JUPYTER/Projects/Medical-Premium-Prediction/xgb.sav")


@api.post('/predict')
def predict_premium(data:PremiumVars):
    data = data.dict()
    age = data['Age']
    Diabetes = data['Diabetes']
    BpP = data['BloodPressureProblems']
    AT = data['AnyTransplants']
    ACT = data['AnyChronicDiseases']
    Height = data['Height']
    Weight = data['Weight']
    KA = data['KnownAllergies']
    HOC = data['HistoryOfCancerInFamily']
    NOS = data['NumberOfMajorSurgeries']
    predict_rf = classifier_rf.predict([[age,Diabetes,BpP, AT, ACT, Height, Weight, KA, HOC, NOS]])
    print(predict_rf)
    #predict_xg = classifier_xg.predict([[age,Diabetes,BpP, AT, ACT, Height, Weight, KA, HOC, NOS]])
    return{
        'Prediction using Random Forest(Accuracy Score: 70)': predict_rf
        #'Prediciton using XGBOOST(Accuracy Score: 68.6)': predict_xg              
        }

if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port = 8000)


#uvicorn app:api --reload