import ast
import pandas as pd
from pymongo import MongoClient
def mongo(data):
    data_dict = ast.literal_eval(data)
    updated_personal_df=pd.DataFrame({"Name":data_dict['name'],"Contact_Number":data_dict['contact'],"Email_ID":data_dict['email'],"Social_Media_Profile":data_dict['media'],"Hobbies":data_dict['hobbies']})
    print(updated_personal_df)
    # Replace placeholders with your actual values
    username = "RexMiltonS"
    password = "Rexmilton5*"
    cluster_uri = "cluster0.x57r05g.mongodb.net"
    database_name = "resume"
    collection_name = "personal_details"
    # Construct the connection string
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_uri}/{database_name}?retryWrites=true&w=majority"
    data_to_insert = updated_personal_df.to_dict(orient="records")
    # Connect to the MongoDB Atlas cluster
    client = MongoClient(connection_string)
 
    # Access the specific database and collection
    db = client[database_name]
    collection = db[collection_name]
    # Define other collections
    educational_collection = db["educational_qualification"]
    area_collection = db["Area_of_Interest"]
    technical_collection = db["Technical_Skills"]
    interpersonal_collection = db["Interpersonal_Skills"]
    certification_collection = db["Certifications"]
    project_collection = db["Project_Experience"]
    professional_collection = db["Professional_Experience"]
    # Check if the email id already exists
    email_to_check = data_to_insert[0]['Email_ID']
    existing_record = collection.find_one({'Email_ID': email_to_check})
    if existing_record:
        existing_id=existing_record['_id']
        # Email id already exists, update the existing record
        updated_data = {k: v for k, v in data_to_insert[0].items() if v is not None}
        collection.update_one({'_id': existing_record['_id']}, {'$set': updated_data})
        print(f"Record with email id '{email_to_check}' updated.")
   
        filter_criteria = {'ID': existing_id}
    # Delete records that match the filter
        educational_delete_result = educational_collection.delete_many(filter_criteria)
        area_delete_result = area_collection.delete_many(filter_criteria)
        technical_delete_result = technical_collection.delete_many(filter_criteria)
        interpersonal_delete_result = interpersonal_collection.delete_many(filter_criteria)
        certification_delete_result = certification_collection.delete_many(filter_criteria)
        project_delete_result = project_collection.delete_many(filter_criteria)
        professional_delete_result = professional_collection.delete_many(filter_criteria)
 
        if len(data_dict['education'])!=0:
            updated_education_df=pd.DataFrame(data_dict['education'])
            updated_education_df.columns=['University/School','Qualification','CGPA/Percentage','Year_of_Completion']
            updated_education_df['ID']=existing_id
            education_data_to_insert = updated_education_df.to_dict(orient="records")
            education_result = educational_collection.insert_many(education_data_to_insert)
            print(updated_education_df)
        if len(data_dict['areaofinterest'])!=0:
            updated_area_df=pd.DataFrame(data_dict['areaofinterest'],columns=['Area_of_Interest'])
            updated_area_df['ID']=existing_id
            area_data_to_insert = updated_area_df.to_dict(orient="records")
            area_result = area_collection.insert_many(area_data_to_insert)
            print(updated_area_df)
        if len(data_dict['technicalskills'])!=0:
            updated_technical_df=pd.DataFrame(data_dict['technicalskills'],columns=['Technical_Skills'])
            updated_technical_df['ID']=existing_id
            technical_data_to_insert = updated_technical_df.to_dict(orient="records")
            technical_result = technical_collection.insert_many(technical_data_to_insert)
            print(updated_technical_df)
        if len(data_dict['interpersonalskills'])!=0:
            updated_interpersonal_df=pd.DataFrame(data_dict['interpersonalskills'],columns=['Interpersonal_Skills'])
            updated_interpersonal_df['ID']=existing_id
            interpersonal_data_to_insert = updated_interpersonal_df.to_dict(orient="records")
            interpersonal_result = interpersonal_collection.insert_many(interpersonal_data_to_insert)
            print(updated_interpersonal_df)
        if len(data_dict['certification'])!=0:
            updated_certification_df=pd.DataFrame(data_dict['certification'])
            updated_certification_df.columns=['Certificate_Name','Issuer']
            updated_certification_df['ID']=existing_id
            certification_data_to_insert = updated_certification_df.to_dict(orient="records")
            certification_result = certification_collection.insert_many(certification_data_to_insert)
            print(updated_certification_df)
        if len(data_dict['projects'])!=0:
            updated_project_df=pd.DataFrame(data_dict['projects'])
            updated_project_df.columns=['Project Name','Duration','Description','Client']
            updated_project_df['ID']=existing_id
            project_data_to_insert = updated_project_df.to_dict(orient="records")
            project_result = project_collection.insert_many(project_data_to_insert)
            print(updated_project_df)
        if len(data_dict['experience'])!=0:
            updated_professional_df=pd.DataFrame(data_dict['experience'])
            updated_professional_df.columns=['Company','Designation','Duration','Description']
            updated_professional_df['ID']=existing_id
            professional_data_to_insert = updated_professional_df.to_dict(orient="records")
            professional_result = professional_collection.insert_many(professional_data_to_insert)
            print(updated_professional_df)
    else:
        collection_result = collection.insert_many(data_to_insert)
        inserted_ids = collection_result.inserted_ids
        print(f"New record inserted with ObjectId: {inserted_ids}")
        new_id=inserted_ids[0]
        if len(data_dict['education'])!=0:
            updated_education_df=pd.DataFrame(data_dict['education'])
            updated_education_df.columns=['University/School','Qualification','CGPA/Percentage','Year_of_Completion']
            updated_education_df['ID']=new_id
            education_data_to_insert = updated_education_df.to_dict(orient="records")
            education_result = educational_collection.insert_many(education_data_to_insert)
            print(updated_education_df)
        if len(data_dict['areaofinterest'])!=0:
            updated_area_df=pd.DataFrame(data_dict['areaofinterest'],columns=['Area_of_Interest'])
            updated_area_df['ID']=new_id
            area_data_to_insert = updated_area_df.to_dict(orient="records")
            area_result = area_collection.insert_many(area_data_to_insert)
            print(updated_area_df)
        if len(data_dict['technicalskills'])!=0:
            updated_technical_df=pd.DataFrame(data_dict['technicalskills'],columns=['Technical_Skills'])
            updated_technical_df['ID']=new_id
            technical_data_to_insert = updated_technical_df.to_dict(orient="records")
            technical_result = technical_collection.insert_many(technical_data_to_insert)
            print(updated_technical_df)
        if len(data_dict['interpersonalskills'])!=0:
            updated_interpersonal_df=pd.DataFrame(data_dict['interpersonalskills'],columns=['Interpersonal_Skills'])
            updated_interpersonal_df['ID']=new_id
            interpersonal_data_to_insert = updated_interpersonal_df.to_dict(orient="records")
            interpersonal_result = interpersonal_collection.insert_many(interpersonal_data_to_insert)
            print(updated_interpersonal_df)
        if len(data_dict['certification'])!=0:
            updated_certification_df=pd.DataFrame(data_dict['certification'])
            updated_certification_df.columns=['Certificate_Name','Issuer']
            updated_certification_df['ID']=new_id
            certification_data_to_insert = updated_certification_df.to_dict(orient="records")
            certification_result = certification_collection.insert_many(certification_data_to_insert)
            print(updated_certification_df)
        if len(data_dict['projects'])!=0:
            updated_project_df=pd.DataFrame(data_dict['projects'])
            updated_project_df.columns=['Project Name','Duration','Description','Client']
            updated_project_df['ID']=new_id
            project_data_to_insert = updated_project_df.to_dict(orient="records")
            project_result = project_collection.insert_many(project_data_to_insert)
            print(updated_project_df)
        if len(data_dict['experience'])!=0:
            updated_professional_df=pd.DataFrame(data_dict['experience'])
            updated_professional_df.columns=['Company','Designation','Duration','Description']
            updated_professional_df['ID']=new_id
            professional_data_to_insert = updated_professional_df.to_dict(orient="records")
            professional_result = professional_collection.insert_many(professional_data_to_insert)
            print(updated_professional_df)
    # Close the connection when done
    client.close()