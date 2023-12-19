from prompting import name_prompt,contact_prompt,email_prompt,media_profile_prompt,hobbies_prompt,Technical_skills_prompt,Interpersonal_skills_prompt,Area_of_interest_prompt,Professional_experience_prompt,Project_experience_prompt,Educational_Qualifications_prompt,Certification_prompt,json_format
from extraction import json_extraction
import json
import pandas as pd
import ast
# crop text
def crop_text(text):
    start_index = text.find('{')
    end_index = text.rfind('}')
    if start_index != -1 and end_index != -1:
        cropped_text = text[start_index:end_index+1].strip()
        return cropped_text
    else:
        return ("")
    
# replace last occurence
def replace_last_occurrence(text, find, replacement):
    last_occurrence_index = text.rfind(find)
    if last_occurrence_index != -1:
        replaced_text = text[:last_occurrence_index] + replacement + text[last_occurrence_index + len(find):]
        return replaced_text
    else:
        return text
    
# replace except last
def replace_except_last(text, find, replacement):
    parts = text.replace(find,replacement)
    formatted_text=replace_last_occurrence(parts, '},', '}')
    return formatted_text
    
# json preprocessing
def json_preprocessing(text,findings):
    text = text.replace("\n", "")
    if findings=="professional_experience":
        fixed=[{"Company":"","Designation":"","Duration":"","Description":""}]
        fixed_df=pd.DataFrame(fixed)
    elif findings=="project_experience":
        fixed=[{"Project Name":"","Duration":"","Description":"","Client":""}]
        fixed_df=pd.DataFrame(fixed)
    elif findings=="certifications":
        fixed=[{"Certificate_Name":"","Issuer":""}]
        fixed_df=pd.DataFrame(fixed)
    elif findings=="educational_qualifications":
        fixed=[{"University/School":"","Qualification":"","CGPA/Percentage":"","Year_of_Completion":""}]
        fixed_df=pd.DataFrame(fixed)
    try:
        #print("1")
        try:
            #print("2")
            k=text.split("},")
            if len(k)==0:
                try:
                    #print("3")
                    json_text = json.loads(text)
                    df = pd.DataFrame(json_text)
                    return df
                except:
                    #print("4")
                    my_dict = ast.literal_eval(text)
                    df = pd.DataFrame([my_dict])
                    return df
            else:
                print(1/0)
        except:
            #print("5")
            try:
                #print("6")
                # Try to load the text as a JSON object
                if text[0] != '[':
                    bracket_text = '[' + text + ']'
                else:
                    bracket_text = text
                json_text = json.loads(bracket_text)
                df = pd.DataFrame(json_text)
                return df
            except:
                #print("7")
                try:
                    #print("8")
                    replacement_text = replace_except_last(bracket_text, '}', '},') 
                    json_text = json.loads(replacement_text)
                    df = pd.DataFrame(json_text)
                    return df
                except:
                    #print("9")
                    try:
                        #print("10")
                        # If parsing fails, attempt another method (json_extraction)
                        json_out = json_extraction(text)
                        json_out=crop_text(json_out)
                        try:
                            #print("11")
                            k=json_out.split("},")
                            if len(k)==0:
                                try:
                                    #print("12")
                                    json_text = json.loads(json_out)
                                    df = pd.DataFrame(json_text)
                                    return df
                                except:
                                    #print("13")
                                    my_dict = ast.literal_eval(json_out)
                                    df = pd.DataFrame([my_dict])
                                    return df
                            else:
                                print(1/0)
                        except:
                            #print("14")
                            try:
                                #print("15")
                                # Try to load the text as a JSON object
                                if json_out[0] != '[':
                                    bracket_text = '[' + json_out + ']'
                                else:
                                    bracket_text = json_out
                                json_text = json.loads(bracket_text)
                                df = pd.DataFrame(json_text)
                                return df
                            except:
                                #print("16")
                                try:
                                    #print("17")
                                    replacement_text = replace_except_last(bracket_text, '}', '},') 
                                    #print("Replacement Text")
                                    #print(replacement_text)
                                    json_text = json.loads(replacement_text)
                                    df = pd.DataFrame(json_text)
                                    return df
                                except:
                                    try:
                                        #print("18")
                                        df=pd.DataFrame(replacement_text)
                                        return df
                                    except:
                                        return fixed_df
                    except:
                        return fixed_df    
    except:
            return fixed_df
    
# list preprocessing
def list_preprocessing(text,col_name):
    list_df=text.split(",")
    strip_list=[]
    for i in list_df:
        strip_list.append(i.strip())
    df=pd.DataFrame(strip_list,columns=[col_name])
    return df