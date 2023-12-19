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
                    If not present, don't hallucinate and create new profile links. 
                    Does not include any unnecessary words or sentence.'''

hobbies_prompt ='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with each hobbies that should not be technical stuffs as specified or mentioned in the resume separated by commas.  
                    If not present, don't hallucinate and create your own hobbies. Kindly return empty string if not presents. 
                    Does not include any unnecessary words or sentence.'''

Area_of_interest_prompt ='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with technical skills like python,sap,etc.. where the candidate is technically more strong as specified or mentioned in the resume separated by commas.  
                    Does not include any unnecessary words or sentence.'''

Technical_skills_prompt ='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with each technical skill separated by commas.  
                    Does not include any unnecessary words or sentence.'''

Interpersonal_skills_prompt = '''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. 
                    Give the output as a string with each interpersonal skill separated by commas.  
                    Does not include any unnecessary words or sentence.'''

Professional_experience_prompt='''You are an AI expert in analyzing text extracted from resumes.
                    I will provide the text extracted from candidate's Resume. List out the previous work experience of the 
                    candidate and based on that give me the output in json format as 
                    {"Company":name of the company mentioned by candidate,
                    "Designation":designation of the candidate there,
                    "Duration":duration of experience in that company,
                    "Description":job details}. 
                    Don't hallucinate and create any new detail that is not already mentioned in the resume.
                    If there is no professional experience return empty for all values. 
                    For internship experience, keep the designation as intern'''

Project_experience_prompt = '''You are an AI expert in analyzing text extracted from resumes. 
                        If any project details are mentioned in the resume , then return the output in the json format
                        {"Project Name": The full name of the project as mentioned in the text, 
                        "Duration": The start and end dates of the project, if provided. If not explicitly stated, indicate " " for the duration, 
                        "Description": A brief summary of the project's objectives, scope, and outcomes, extracted from the text. If a detailed description is unavailable, indicate "Description not available" or provide a concise summary based on the available information, 
                        "Client" : The name of the client or organization for which the project was undertaken. If the client's name is not explicitly mentioned, indicate " "}
                        The output should be in json format.The key values pairs are preferred to be in double quotes.'''
Certification_prompt='''You are an AI expert in analyzing text extracted from resumes. 
            If any certifications are mentioned in the resume , then return the output in the json format
            {"Certificate_Name": The full name of the Certification as mentioned in the text, 
            "Issuer" : The name of the issuer or organization who have provided the course. If the issuer's name is not explicitly mentioned, indicate " "}
            The output should be in json format.
            If there are multiple certifications are present, each one will be separated by commas and enclosed in a set brackets to be in proper json format.'''
Educational_Qualifications_prompt='''You are an AI expert in analyzing text extracted from resumes.
                                      I will provide the text extracted from candidate's Resume. 
                                      List out the Educational Qualifications of the candidate and based on that give me the output in json format as 
                                        { "University/School":name of the University/school mentioned by candidate,
                                        "Qualification": name of degree like BE,MCA,ect. or name of Standard like X,XII,
                                        "CGPA/Percentage": CGPA/Percentage secured in qualification if it mentioned. If the grade is not explicitly mentioned, indicate " "}
                                        "Year_of_Completion": Year when the course is completed if it mentioned. If the Year of completion is not explicitly mentioned, indicate " "
                                        }. 
                                        Don't hallucinate and create any new detail that is not already mentioned in the resume.
                                        If there is no educational qualifications of candidate presents return empty for all values.The output should be in json format.
                                        If there are multiple educational qualifications are present, each one will be separated by commas and enclosed in a set brackets to be in proper json format.'''
json_format='''You are an AI expert in correctly formatting the json text. 
                 I will give a json text but it has some syntax errors while using json.loads().
                So, remove those errors and give a correctly formated json so that it will loads to json without any errors.
                The Keys and Values of dictionaries always preferred to be in double quotes.
                Give only the exact output without any unnecessary sentences.'''