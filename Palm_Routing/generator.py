
import zipfile
from extraction import name_extraction,contact_extraction,email_extraction,social_extraction,hobbies_extraction,area_of_interest_extraction,technical_skills_extraction,interpersonal_skills_extraction,professional_experience_extraction,project_experience_extraction,certification_extraction,educational_extraction
from preprocessing import crop_text,json_preprocessing,list_preprocessing
from reading_text import read_text_from_file
from getting_formated_json import get_correct_formated_json_data
import pandas as pd
import json
# v=r"C:\Users\Snekalatha\Downloads\Palm Routing\uploads\resume.pdf"
import os

def list_files_with_paths(folder_path):
    files_with_paths = []

    # Check if the provided path is a zip file
    if folder_path.endswith('.zip') and os.path.isfile(folder_path):
        with zipfile.ZipFile(folder_path, 'r') as zip_ref:
            # Extract all contents of the zip file to a temporary folder
            temp_folder = r"E:\kaar\text extraction\Palm_Routing\uploads\temp"
            zip_ref.extractall(temp_folder)

            # Get the list of files in the temporary folder with full paths
            files_with_paths = [os.path.join(temp_folder, f) for f in os.listdir(temp_folder) if os.path.isfile(os.path.join(temp_folder, f))]

    else:
        # Get the list of files in the specified folder with full paths
        files_with_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    return files_with_paths

# Example Usage:
folder_path = r"E:\kaar\text extraction\Palm_Routing\uploads\resume.zip"
y={}
count=1
file_list_with_paths = list_files_with_paths(folder_path)
print("List of files with full paths:")
for file_path in file_list_with_paths:
    print(file_path)
    transcription=read_text_from_file(file_path)
    name_extract = name_extraction(transcription)
    contact_extract = contact_extraction(transcription)
    email_extract = email_extraction(transcription)
    social_extract = social_extraction(transcription)
    hobbies_extract = hobbies_extraction(transcription)
    area_of_interest_extract=area_of_interest_extraction(transcription)
    technical_skills_extract=technical_skills_extraction(transcription)
    interpersonal_skills_extract=interpersonal_skills_extraction(transcription)
    professional_experience_extract=professional_experience_extraction(transcription)
    professional_experience_extract=crop_text(professional_experience_extract)
    project_experience_extract=project_experience_extraction(transcription)
    project_experience_extract=crop_text(project_experience_extract)
    certification_extract=certification_extraction(transcription)
    certification_extract=crop_text(certification_extract)
    educational_extract=educational_extraction(transcription)
    educational_extract=crop_text(educational_extract)

    column_names = ['Name', 'Contact_Number', 'Email_ID', 'Social_Media_Profile', 'Hobbies']
    personal_df=pd.DataFrame(columns=column_names)
    new_record = [name_extract,contact_extract,email_extract,social_extract,hobbies_extract]
    personal_df.loc[len(personal_df)] = new_record
    professional_df=json_preprocessing(professional_experience_extract,"professional_experience")
    project_df=json_preprocessing(project_experience_extract,"project_experience")
    certification_df=json_preprocessing(certification_extract,"certifications")
    education_df=json_preprocessing(educational_extract,"educational_qualifications")
    area_df=list_preprocessing(area_of_interest_extract,"Area_of_Interest")
    technical_df=list_preprocessing(technical_skills_extract,"Technical_Skills")
    interpersonal_df=list_preprocessing(interpersonal_skills_extract,"Interpersonal_Skills")
    print("PERSONAL")
    print(personal_df)
    print("education_df")
    print(education_df)
    print("area_df")
    print(area_df)
    print("technical_df")
    print(technical_df)
    print("interpersonal_df")
    print(interpersonal_df)
    print("certification_df")
    print(certification_df)
    print("project_df")
    print(project_df)
    print("professional_df")
    print(professional_df)
    x=get_correct_formated_json_data(personal_df,education_df,area_df,technical_df,interpersonal_df,certification_df,professional_df,project_df)
    y[count]=x
    count=count+1
# Convert dictionary to JSON format
json_data = json.dumps(y)

# Print the JSON-formatted string
print(json_data)
def out_get():
    return(json_data)
