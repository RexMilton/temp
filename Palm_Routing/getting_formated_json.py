
import json
def get_correct_formated_json_data(personal_df,education_df,area_df,technical_df,interpersonal_df,certification_df,professional_df,project_df):
    x={}

    #name
    try:
        x['name']=personal_df["Name"].tolist()[0]
    except:
        x['name']=""

    #contact
    try:
        x['contact']=personal_df["Contact_Number"].tolist()[0]
    except:
        x['contact']=""

    #email
    try:
        x['email']=personal_df["Email_ID"].tolist()[0]
    except:
        x['email']=""

    #media
    try: 
        x['media']=personal_df["Social_Media_Profile"].tolist()[0].replace("\n", "").replace("\r", "")
    except:
        x['media']=""

    #hobbies
    try:
        x['hobbies']=personal_df["Hobbies"].tolist()[0]
    except:
        x['hobbies']=""

    try:
        education_df.columns=['university','qualification','cgpa','yearofcompletion']
        x['education'] = json.loads(education_df.to_json(orient='records'))
    except:
        x['education'] =[{'university':"",'qualification':"",'cgpa':"",'yearofcompletion':""}]

    try:
        x['areaofinterest']=area_df['Area_of_Interest'].tolist()
    except:
        x['areaofinterest']=[""]


    try:
        x['technicalskills']=technical_df['Technical_Skills'].tolist()
    except:
        x['technicalskills']=[""]


    try:
        x['interpersonalskills']=interpersonal_df['Interpersonal_Skills'].tolist()
    except:
        x['interpersonalskills']=[""]

    try:
        certification_df.columns=['name','issuer']
        x['certification']=json.loads(certification_df.to_json(orient='records'))
    except:
        x['certification']=[{"name":"","issuer":""}]

    try:
        project_df.columns=['projectname','client','duration','description']
        x['projects']=json.loads(project_df.to_json(orient='records'))
    except:
        x['projects']=[{"projectname":"","client":"","duration":"","description":""}]


    try:
        professional_df.columns=['company','designation','duration','description']
        x['experience']=json.loads(professional_df.to_json(orient='records'))
    except:
        x['experience']=[{"company":"","designation":"","duration":"","description":""}]
    return x
