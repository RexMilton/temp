from prompting import name_prompt,contact_prompt,email_prompt,media_profile_prompt,hobbies_prompt,Technical_skills_prompt,Interpersonal_skills_prompt,Area_of_interest_prompt,Professional_experience_prompt,Project_experience_prompt,Educational_Qualifications_prompt,Certification_prompt,json_format
import google.generativeai as palm

# name extraction
def name_extraction(transcription):
    #print("NAME")
    name_response = palm.generate_text(
        prompt=name_prompt + "\n" + "Paragraph:" + transcription
    )
    name = name_response.candidates[0]['output']
    name=name.strip()
    if name[0]==".":
        name=name[1::]
    name=name.strip()   
    #print(name)
    return name

# contact extraction
def contact_extraction(transcription):
   # print("CONTACT NUMBER")
    contact_response = palm.generate_text(
        prompt=contact_prompt + "\n" + "Paragraph:" + transcription
    )
    contact = contact_response.candidates[0]['output']
    contact=contact.strip()
    if contact[0]==".":
        contact=contact[1::]
    contact=contact.strip()
    #print(contact)
    return contact

# email extraction
def email_extraction(transcription):
    #print("EMAIL")
    email_response = palm.generate_text(
        prompt=email_prompt + "\n" + "Paragraph:" + transcription
    )
    email = email_response.candidates[0]['output']
    email=email.strip()
    if email[0]==".":
        email=email[1::]
    email=email.strip()
    #print(email)
    return email

# social extraction
def social_extraction(transcription):
    #print("SOCIAL MEDIA PROFILE")
    media_response = palm.generate_text(
        prompt=media_profile_prompt + "\n" + "Paragraph:" + transcription
    )
    media = media_response.candidates[0]['output']
    media=media.strip()
    if media[0]==".":
        media=media[1::]
    media=media.strip()
    #print(media)
    return media

# hobbies extraction
def hobbies_extraction(transcription):
    #print("HOBBIES")
    hobbies_response = palm.generate_text(
        prompt=hobbies_prompt + "\n" + "Paragraph:" + transcription
    )
    if hobbies_response.candidates:
        hobbies = hobbies_response.candidates[0]['output']
        hobbies=hobbies.strip()
        if hobbies[0]==".":
            hobbies=hobbies[1::]
        hobbies=hobbies.strip()
    else:
        hobbies = ""
    #print(hobbies)
    return hobbies

# technical skills extraction
def technical_skills_extraction(transcription):
    #print("TECHNICAL SKILLS")
    Technical_skills_response = palm.generate_text(
        prompt=Technical_skills_prompt + "\n" + "Paragraph:" + transcription
    )
    Technical_skills = Technical_skills_response.candidates[0]['output']
    #print(Technical_skills)
    return Technical_skills

# interpersonal skills extraction
def interpersonal_skills_extraction(transcription):
    #print("INTERPERSONAL SKILLS")
    Interpersonal_skills_response = palm.generate_text(
        prompt=Interpersonal_skills_prompt + "\n" + "Paragraph:" + transcription
    )
    Interpersonal_skills = Interpersonal_skills_response.candidates[0]['output']
    #print(Interpersonal_skills)
    return Interpersonal_skills

# area of interest extraction
def area_of_interest_extraction(transcription):
    #print("AREA OF INTEREST")
    area_of_interest_response = palm.generate_text(
        prompt=Area_of_interest_prompt + "\n" + "Paragraph:" + transcription
    )
    area_of_interest = area_of_interest_response.candidates[0]['output']
   # print(area_of_interest)
    return area_of_interest

# professional experience extraction
def professional_experience_extraction(transcription):
    #print("PROFESSIONAL EXPERIENCE")
    Professional_experience_response = palm.generate_text(
        prompt=Professional_experience_prompt + "\n" + "Paragraph:" + transcription
    )
    professional_experience = Professional_experience_response.candidates[0]['output']
    #print(professional_experience)
    return professional_experience

# project experience extraction
def project_experience_extraction(transcription):
   # print("PROJECT EXPERIENCE")
    Project_experience_response = palm.generate_text(
        prompt=Project_experience_prompt + "\n" + "Paragraph:" + transcription
    )
    project_experience = Project_experience_response.candidates[0]['output']
    #print(project_experience)
    return project_experience

# educational qualification extraction
def educational_extraction(transcription):
    #print("Educational Qualification")
    Educational_Qualifications_response = palm.generate_text(
        prompt=Educational_Qualifications_prompt + "\n" + "Paragraph:" + transcription
    )
    Educational_Qualifications = Educational_Qualifications_response.candidates[0]['output']
    #print(Educational_Qualifications)
    return Educational_Qualifications

# certification extraction
def certification_extraction(transcription):
    #print("Certification")
    certification_response = palm.generate_text(
        prompt=Certification_prompt + "\n" + "Paragraph:" + transcription
    )
    certification = certification_response.candidates[0]['output']
    #print(certification)
    return certification

# json extraction
def json_extraction(transcription):
    #print("JSON EXTRACTION")
    json_response = palm.generate_text(
        prompt=json_format + "\n" + "Paragraph:" + transcription
    )
    json_text = json_response.candidates[0]['output']
    #print(json_text)
    return json_text