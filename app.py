from flask import Flask, request, render_template, redirect, url_for
import pdf_reader 
from dotenv import load_dotenv
import os
load_dotenv()
KEY = os.getenv("GROQ_API_KEY")
app = Flask(__name__)
# decorator calls receive() when / is called
@app.route('/',methods=["GET","POST"])
def receive():
    #handle submit button
    message = ""
    if request.method == "POST":
        file = request.files["pdf"]   #receives pdf in bytestream
        content, hasContent=pdf_reader.send(file) #sends pdf to send() in pdf_reader.py. 
        if hasContent:   #if the pdf has content, send content back to html
            from groq import Groq
            client = Groq(
                api_key = KEY
            )
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a resume analyser. You will read a resume, and rate it on a scale of 0 to 100. Here's the resume :{content}",
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            content = chat_completion.choices[0].message.content
            return render_template("index.html", message = content)
        else:
            message = "The pdf sent is empty, please send a pdf with content"
    return render_template("index.html", message = message)
if __name__ == "__main__":
    app.run(debug=True) #test