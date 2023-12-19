import ast
import os
import pandas as pd
from flask import Flask, request,jsonify
from flask_cors import CORS
from pathlib import Path
import google.generativeai as palm
import PyPDF2
import json
import os
from bson import json_util
from  mongodb import mongo 
class DataStore():
    pdfText=None

class_data = DataStore()

app = Flask(__name__)
CORS(app,resources={r"/api/*": {"origins": "http://localhost:4200"}})

# Configure the client library by providing your API key.
palm.configure(api_key="AIzaSyA1HwkfN_9cH2hF1KJc54OBNm_m321ImN4")

name_prompt = '''You are an AI expert in analyzing text extracted from resumes.
                With the text extracted from resume as your input, give the output as the name of the candidate [For example: SINEGALATHA B],
                Does not include any unnecessary words or sentence.'''

contact_prompt = '''You are an AI expert in analyzing text extracted from resumes.
                 With the text extracted from resume as your input, give the output as contact number of the candidate.
                 If not present, don't hallucinate and create new contact number. 
                 Does not include any unnecessary words or sentence.'''

email_prompt = '''You are an AI expert in analyzing text extracted from resumes.
                With the text extracted from resume as your input, give the output as email ID of the candidate.
                If not present, don't hallucinate and create new email ID. 
                Does not include any unnecessary words or sentence.'''

media_profile_prompt = '''You are an AI expert in analyzing text extracted from resumes.
                    With the text extracted from resume as your input, give the output as Social media profile (like linkedin, instagram, github or any portfolio) of the candidate as it is mentioned in the resume.
                    if there are multiple social media links in resume give them in a list as strings
                    If not present, don't hallucinate and create new profile links. 
                    Does not include any unnecessary words or sentence.'''
education_details_prompt='''You are an AI expert in analyzing text extracted from resumes.
                                      I will provide the text extracted from candidate's Resume. 
                                      List out the Educational Qualifications of the candidate and based on that give me the output in json format as 
                                        {university:name of the University/school mentioned by candidate,
                                        qualification: name of degree like BE,MCA,ect. or name of Standard like X,XII,
                                        cgpa: CGPA/Percentage secured in qualification if it mentioned. If the grade is not explicitly mentioned, indicate " "}
                                        yearofcompletion: Year when the course is completed if it mentioned. If the Year of completion is not explicitly mentioned, indicate " "
                                        }. If there are multiple educational details split them with comma start with " and end with "
                                        Don't hallucinate and create any new detail that is not already mentioned in the resume.
                                        If there is no educational qualifications of candidate presents return empty for all values.The output should be in json format.'''
hobbies_prompt ='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with each hobbies that should not be technical stuffs as specified or mentioned in the resume separated by commas.  
                    If not present, don't hallucinate and create your own hobbies. Kindly return empty string like "" if not present. 
                    Does not include any unnecessary words or sentence.'''

Professional_experience_prompt='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. List out the previous work experience of the 
                    candidate and based on that give me the output in json format as 
                    {company:name of the company mentioned by candidate,
                    designation:designation of the candidate there,
                    duration:duration of experience in that company,
                    description:job details}. Also give whole json format in single line dont give \n anywhere , If there are multiple experiences split them with comma start with " and end with "
                    Don't hallucinate and create any new detail that is not already mentioned in the resume.
                    If there is no professional experience return empty for all values. 
                    For internship experience, keep the designation as intern'''
Certification_prompt='''You are an AI expert in analyzing text extracted from resumes. 
            If any certifications are mentioned in the resume , then return the output in the json format
            {"name": The full name of the Certification as mentioned in the text, 
            "issuer" : The name of the issuer or organization who have provided the course. If the issuer's name is not explicitly mentioned, indicate " "}
            The output should be in json format.
            If there are multiple certifications are present, each one will be separated by commas and enclosed in a set brackets to be in proper json format.'''
Area_of_interest_prompt ='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with technical skills like python,sap,etc.. where the candidate is technically more strong as specified or mentioned in the resume separated by commas.  
                    If there are none area of intereset return and empty string as output like this '' Does not include any unnecessary words or sentence.'''

Technical_skills_prompt ='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with each technical skill separated by commas.Give everything in a single line without uneccesary spaces and '\n'.  
                    Does not include any unnecessary words or sentence.'''

Interpersonal_skills_prompt = '''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with each interpersonal skill separated by commas.  Give everything in a single line without uneccesary spaces and '\n'
                    Does not include any unnecessary words or sentence.'''
Project_details_prompt = '''You are an AI expert in analyzing text extracted from resumes. 
                        If any project details are mentioned in the resume , then return the output in the json format
                        {"projectname": The full name of the project as mentioned in the text, 
                        "duration": The start and end dates of the project, if provided. If not explicitly stated, indicate " " for the duration, 
                        "description": A brief summary of the project's objectives, scope, and outcomes, extracted from the text. If a detailed description is unavailable, indicate "Description not available" or provide a concise summary based on the available information, 
                        "client" : The name of the client or organization for which the project was undertaken. If the client's name is not explicitly mentioned, indicate " "}
                        The output should be in json format.The key values pairs are preferred to be in double quotes.Dont hallucinate own project details please provide only if they are available in text'''


#Defining Configuration
model = 'models/text-bison-001'
temperature = 0
candidate_count = 1
top_k = 40
top_p = 0.95
max_output_tokens = 1024
stop_sequences: []
safety_settings: [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}]
defaults = {
'model': model,
'temperature': temperature,
'candidate_count': candidate_count,
'top_k': top_k,
'top_p': top_p,
'max_output_tokens': max_output_tokens,
# 'safety_settings':safety_settings,
}

def extraction(transcription,s):
    # Your existing extraction function
    response = palm.generate_text(
        **defaults,
        prompt=s + "\n" + "Paragraph:" + transcription
    )
    try:
        final = response.candidates[0]['output']
    except Exception as e:
        # Handle any error by setting final to an empty string
        final = ""
    final=(final.lstrip('\n')).strip()
    return final


def process_json(text):
     if(text[0]!='[' and text[0]!='{'):
        while(text[0]!='{'):
            text=text[1:]
        while(text[-1]!='}'):
            text=text[:-1]
     if(text[0]!="["):
          text = f"[{text.strip()}]"
     if("'" in text):
          text = text.replace("'", "\"")
     final_text=json.loads(text)
     return final_text
     

          
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as resume_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(resume_file)
            # Initialize a variable to store the extracted text
            transcription = ''
            # Iterate through all pages and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                transcription += page.extract_text()
    return transcription


def find(extracted_text):
    global name
    global contact
    global email
    global media_profile
    global hobbies
    global education_details
    global professional_experience
    global certification_details
    global technical_skills
    global interpersonal_skills
    global area_of_interest
    global skills
    global project_details
    name=extraction(extracted_text,name_prompt)
    contact=extraction(extracted_text,contact_prompt)
    email=extraction(extracted_text,email_prompt)
    media_profile=[(extraction(extracted_text,media_profile_prompt))]
    hobbies=extraction(extracted_text,hobbies_prompt)
    hobbies=(hobbies.lstrip('\n')).strip()
    hobbies=[hobbies]
    education_details=process_json(extraction(extracted_text,education_details_prompt))
    professional_experience=(extraction(extracted_text,Professional_experience_prompt))
    if(professional_experience[-1].isalpha()):
        professional_experience=professional_experience+"'}]"
    professional_experience=professional_experience.lstrip('\n')
    professional_experience=process_json(professional_experience)
    certification_details=process_json(extraction(extracted_text,Certification_prompt))
    technical_skills=extraction(extracted_text,Technical_skills_prompt)
    technical_skills=list((technical_skills.lstrip('\n')).strip().split(','))
    interpersonal_skills=extraction(extracted_text,Interpersonal_skills_prompt)
    interpersonal_skills=list((interpersonal_skills.lstrip('\n')).strip().split(','))
    area_of_interest=extraction(extracted_text,Area_of_interest_prompt)
    area_of_interest=list((area_of_interest.lstrip('\n')).strip().split(','))
    project_details=process_json(extraction(extracted_text,Project_details_prompt))
    

# #File Upload Code
@app.route('/api/file_upload', methods=['POST'])
def file_upload():
    global pdfText
    resp = {}
    try:
        file = request.files.get('file')
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        find(text)  
            
        status = {
            "statusCode": "200",
            "statusMessage": "File uploaded Successfully."
        }
    except Exception as e:
        print(e)
        status = {
            "statusCode": "400",
            "statusMessage": str(e)
        }
    resp["status"] = status
    return resp

#Retriving Data from Resume
@app.route('/api/get_data',methods=['GET'])
def get_data():
    # print(name)
    x={"1": {"name": "ANUVA GOYAL",
 "contact": "+91 9520349542", 
"email": "anuvagoyal111@gmail.com", 
"media": ["LinkedIn: https://www.linkedin.com/in/anuva-goyal-8889b61b2/"], 
"hobbies": ["Reading novels", "Volunteering and social service"], 
"education": [{"university": "Dayalbagh Educational Institute", "qualification": "B.Tech.", "cgpa": "CGPA 9.35", "yearofcompletion": "2023"}, {"university": "St. Clare's Senior Secondary School", "qualification": "XII", "cgpa": "94%", "yearofcompletion": "2019"}, {"university": "St. Clare's Senior Secondary School", "qualification": "X", "cgpa": "CGPA 10", "yearofcompletion": "2017"}], 
"areaofinterest": ["python", "java", "html", "javascript", "c++", "c", "sql", "pycharm", "jupyter notebook", "google colab", "code blocks", "matlab", "turbo c++", "ms office", "scikit-learn", "tensorflow", "opencv", "numpy", "pytesseract", "keras"], 
"technicalskills": ["C++", "Python", "JAVA", "HTML", "CSS", "JavaScript", "Data Structures", "SQL", "PyCharm", "Jupyter Notebook", "Google Colab", "Code Blocks", "MATLAB", "Turbo C++", "MS Office", "Scikit-Learn", "TensorFlow", "OpenCV", "NumPy", "Pytesseract", "Keras"], 
"interpersonalskills": ["teamwork", "communication", "leadership", "problem-solving"], 
"certification": [{"name": "Data Science", "issuer": "Coursera"}], 
"projects": [{"projectname": "Mental Healthcare Chatbot", "client": "Ongoing", "duration": "A model to provide mental health counselling to users using conversational AI techniques", "description": ""}], 
"experience": [{"company": "Geniusup India Pvt. Ltd.", "designation": "Intern", "duration": "1 month", "description": "Worked on proxy rotation and utilization. Learnt Web Scraping using bs4 and performed LDA Topic Modeling on \"The Hindu\" news articles."}, {"company": "VUGS Technologies", "designation": "Intern", "duration": "1 month", "description": "Built an OCR using Pytesseract and NER Text Classification Model to categorize detected text into Name, E-mail Address, Phone number and Date."}]
}, 
"2": {"name": "ASWIN S", 
"contact": "+91 97872220470", 
"email": "aswinjak2002@gmail.com", 
"media": ["https://www.linkedin.com/in/aswin-s-506520202"],
"hobbies": ["music"],
"education": [{"university": "BHARANIPARK MATRIC HR. SEC. SCHOOL", "qualification": "Higher Secondary Education", "cgpa": "82.0%", "yearofcompletion": "2019-2020"}, {"university": "BHARANIPARK MATRIC HR. SEC. SCHOOL", "qualification": "Secondary Education", "cgpa": "90.2%", "yearofcompletion": "2017-2018"}, {"university": "M. KUMARASAMY COLLEGE OF ENGINEERING", "qualification": "B.E. COMPUTER SCIENCE", "cgpa": "9.232", "yearofcompletion": "2023-2024"}], "areaofinterest": ["java", "angular", "mysql", "html", "css"], 
"technicalskills": ["java", "mysql", "angular", "html", "css"], 
"interpersonalskills": ["teamwork", "time management", "adaptability"], 
"certification": [{"name": "Japanese Language Proficiency Test (N5)", "issuer": "The Japan Foundation"}], 
"projects": [{"projectname": "Student Sentiment Analysis Using Feedback", "client": "11th April 2022 - 25th April 2022", "duration": "A web application that connects the people and the medical store. The customers, medical stores and warehouse have different login id to know the status of the medicines.", "description": "MKCS Digital Tech Solutions"}], 
"experience": [{"company": "KAAR TECHNOLOGIES", "designation": "Software Engineer Intern", "duration": "Dec 2022 - July 2023", "description": "Developed a web application that connects people and medical stores. The customers, medical stores and warehouse have different login id to know the status of the medicines."}]}
}
    # x={}
    # x["name"]=name
    # x["email"]=email
    # x["contact"]=contact
    # x["media"]=media_profile
    # x["education"]=education_details
    # x["experience"]=professional_experience
    # x["certification"]=certification_details
    # x["projects"]=project_details
    # x["technicalskills"]=technical_skills
    # x["interpersonalskills"]=interpersonal_skills
    # x["areaofinterest"]=area_of_interest
    # x["hobbies"]=hobbies
    return x

@app.route('/api/submit_data',methods=['POST'])
def submit_data():
    response = jsonify({'status': 'success'})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    resp = {}
    # mongo("hello")
    try:
        resp = request.get_json(force = True)
        data_with_str_object_id = json.loads(json_util.dumps(resp))
        temp = mongo(data_with_str_object_id)
        # print("hello")
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
