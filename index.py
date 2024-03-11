import requests
import PyPDF2
from http.server import BaseHTTPRequestHandler

# Function to convert PDF to text
def pdf_to_text(pdf_url):
    try:
        # Download the PDF file
        response = requests.get(pdf_url)
        pdf_data = response.content
        
        # Open the PDF file and extract text
        pdf_reader = PyPDF2.PdfFileReader(pdf_data)
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        
        return text
    except Exception as e:
        print("Error:", e)
        return None

def handler(request, context):
    # Ignore requests for favicon
    if request["path"] == "/favicon.ico":
        return {"statusCode": 404}
    
    # URL of the PDF file to convert
    pdf_url = "https://mr-umair.000webhostapp.com/new-pdf.pdf"

    # Convert PDF to text and return the result
    result = pdf_to_text(pdf_url)
    if result:
        return {
            "statusCode": 200,
            "body": result
        }
    else:
        return {
            "statusCode": 500,
            "body": "PDF to text conversion failed."
        }
