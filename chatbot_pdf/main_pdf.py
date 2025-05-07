import fitz

def extractTextFromPDF(pdf_file_path):
    """
    Extracts all text content from a PDF file using the PyMuPDF (fitz) library.

    This function opens the specified PDF file, iterates through each page,
    extracts the textual content, and returns it as a single string. It is
    designed to support a chatbot by providing access to the PDF's text data.

    Args:
        pdf_file_path (str): Path to the PDF file.

    Returns:
        str: The extracted text, or an error message if extraction fails.
    """
    try:
        doc = fitz.open(pdf_file_path) #Open the PDF file
        pdf_text = "" #String variable to store the extracted text

        #Iterate through all the pages of the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num) #Load the current page
            pdf_text += page.get_text("text") #Gets all the text from the  page
        doc.close() #Close the document
        return pdf_text
    except Exception as e:
        # Return an error message if something goes wrong during extraction
        return f"Error extracting text from PDF: {e}"

# Path to the input PDF file
pdf_path = "Landon-Hotel.pdf"
# Call the function to extract text from the PDF
extracted_text = extractTextFromPDF(pdf_path)

# Write the extracted text to a new .txt file
with open("pdf-text.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)