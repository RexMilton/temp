import logging

from requests import Response

from flask_pymongo import pymongo
from flask import jsonify, request
import pandas as pd
import json
# from simple_app.ml import process

l=[{"test":"res-fine"}]


con_string = "mongodb+srv://RexMiltonS:Rexmilton5*@cluster0.3ekp5xp.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)

db = client.get_database('login')

user_collection = pymongo.collection.Collection(db, 'login')
print("MongoDB connected Successfully")

def project_api_routes(endpoints):
    @endpoints.route('/file_upload',methods=['POST'])
    def file_upload():
        resp = {}
        try:
            req = request.form
            file = request.files.get('file')
            # df = pd.read_csv(file)
            # print(df.head)
            # print(df.columns)
            global l
            # l=process(df)
            # print(l)
            status = {
                "statusCode":"200",
                "statusMessage":"File uploaded Successfully.",
                "res": "hello"
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] = status
        return resp

    @endpoints.route('/get_data',methods=['GET'])
    def get_data():
        x={
            "name":'rex',
            "email": 'rexmilton@gmail.com',
            "contact": '2331241432',
            "media" : ['insta','github'],
            "hobbies": ['reading','writing'],
            "technicalskills" : ['angular','python'],
            "interpersonalskills" : ['leadership','timemanagement'],
            "areaofinterest" : ['coding'],
            "experience" : [
                {
                    "company" : 'kaar',
                    "designation" : 'intern',
                    "duration" : '1 year',
                    "description" : 'Data Analyst'
                }
            ],
            "projects" : [
                {
                    "projectname" : 'frs',
                    "client" : 'kaar',
                    "duration" : '1 month',
                    "description" : 'sales forecasting'
                }
            ],
            "education" : [
                {
                    "university" : 'rmk',
                    "qualification" : 'B.E',
                    "cgpa" : '9.2',
                    "yearofcompletion" : "2023"
                },
                {
                    "university" : 'rmk',
                    "qualification" : 'B.E',
                    "cgpa" : '9.2',
                    "yearofcompletion" : "2023"
                },

            ],
            "certification" :[
                {
                    "name" : 'google cloud',
                    "issuer" : 'google'
                }
            ]       
        }
        return x
    
    @endpoints.route('/submit_data',methods=['POST'])
    def submit_data():
        response = jsonify({'status': 'success'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        resp = {}
        try:
            resp = request.json
            print(resp)
            status = {
                "statusCode":"200",
                "statusMessage":"File uploaded Successfully.",
                "res": "hello"
            }
        except Exception as e:
            print("ERROR",e)
        return resp
    
    return endpoints
