from bs4 import BeautifulSoup
import requests

def extractTextFromURL(target_url):
    """
        Extracts all text within <p> tags from a website and saves it to a text file.

        Parameters:
            url (str): The target URL to extract text from.

        Behavior:
            - Sends a GET request to the provided URL.
            - Parses the HTML content using BeautifulSoup.
            - Searches for all <p> tags and extracts their text.
            - Saves the extracted text to 'website_text.txt'.
            - Handles connection and parsing errors gracefully.
        """
    try:
        response = requests.get(target_url)  # Retrieves the website HTML content

        # Proceed only if the server returned a successful response (status code 200)
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser') #Parse the HTML content

            paragraphs = soup.find_all('p') #Finds all paragraph tags
            if not paragraphs:
                print("No paragraph tags were found on the page.")
                return
            else:
                text = "\n".join(paragraph.get_text() for paragraph in paragraphs) #Join all paragraph texts with line breaks

            # Write the extracted text to a new .txt file
            with open("website_text.txt", "w", encoding="utf-8") as file:
                file.write(text)

            print("Text extracted and saved successfully")
        else:
            print(f"Error: failed to retrieve website content. Status code: {response.status_code}")

    # Catch any errors related to the HTTP request (connection issues, timeout, etc.)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    # Catch any unexpected errors (e.g., issues saving the file, logic errors, etc.)
    except Exception as e:
        print(f"An unexpected Error ocurred: {e}")

#URL
target_url = "https://www.terradomar.com.ar/servicios.php"
extractTextFromURL(target_url)