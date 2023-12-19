import google.generativeai as palm

palm.configure(api_key="AIzaSyA1HwkfN_9cH2hF1KJc54OBNm_m321ImN4")

generation_config = {
    'model': 'models/gemini-pro',
    'temperature': 0,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024
}
