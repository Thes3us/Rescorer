import pymupdf
import re
def send(file):
    """sends pdf file from Flask app to be processed
    Args:
        file (bytestream): The pdf in bytestream
    Returns:
        string: response 
    """
    MaxChars=16000
    TotalChars=0
    if not file:
        return("empty") # if file is empty
    if file.filename.endswith('.pdf') == False:
        return("invalid format")  # if file is not pdf
    byte_form=file.read()        #reads the file in byte form from the object
    try:
        doc = pymupdf.open(stream=byte_form,filetype="pdf")     #opens the file from the byte form
    except Exception:
        return("unable to open")
    content = []
    for page in doc:
        text=page.get_text()   #converts byte to human readable stuff
        text=re.sub(r'\s+',' ',text)  #removes all kind of whitespaces
        TotalChars+=len(text)
        if TotalChars>MaxChars:
            return("too large")
        content.append(text)   #append each page into text
    # print(content)    #debug purpose
    return(content) # return content and hascontent