import requests
import PyPDF2

# Function to convert PDF to text
def pdf_to_text(pdf_url):
    try:
        # Download the PDF file
        response = requests.get(pdf_url)
        with open("temp.pdf", "wb") as pdf_file:
            pdf_file.write(response.content)
        
        # Open the PDF file and extract text
        with open("temp.pdf", "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ""
            for page_num in range(pdf_reader.numPages):
                text += pdf_reader.getPage(page_num).extractText()
        
        return text
    except Exception as e:
        print("Error:", e)
        return None

# URL of the PDF file to convert
pdf_url = "https://mr-umair.000webhostapp.com/new-pdf.pdf"

# Convert PDF to text and display the result
result = pdf_to_text(pdf_url)
if result:
    print("PDF to text conversion result:")
    print(result)
else:
    print("PDF to text conversion failed.")
    
