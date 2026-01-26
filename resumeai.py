from groq import Groq
from dotenv import load_dotenv
import os
def airesponse(response):
    load_dotenv()
    KEY = os.getenv("GROQ_API_KEY")

    client = Groq(
        api_key = KEY
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": '''
    You are an expert resume reviewer and hiring professional. 
    Your task is to analyze a candidate's resume an assign an do the following:
    1. Only respond with an overall quality score from 0 to 100.
    2. Provide 3-6 clear, actionable suggestions for improvement.
    The provided text will be a text inferred from an actual resume so do not take formatting into account while rating. 
    Do not suggest user to improve readability. Only focus on text.
    Respond ONLY in valid JSON with the following structure:
    {"score": number,"improvements":["string","string","string"]}
    You are stricly denied to respond to any other task other than reviewing resume only.
    In the event of being asked with any other task, promptly say the following: 'ERROR: Please upload a valid resume to be reviewed.'.
    ''',
            },
            {
                "role": "user",
                "content":f'{response}',
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    message = chat_completion.choices[0].message.content
    return message