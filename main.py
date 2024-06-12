import pandas as pd
from googlesearch import search
import time

def scrape_google_search_results(query):
    # Do the Google search
    search_results = search(query, num_results=10, lang='en')

    # List to store company names
    company_names = []
    
    # Iterate through search results
    for url in search_results:
        try:
            # Pause for a while before making the next request
            time.sleep(2)

            # Extract text from the webpage (for demonstration purposes)
            # You may need to implement actual scraping logic here
            text = extract_text_from_url(url)
            
            # Check if the text contains relevant information about Ayurvedic companies
            if "Ayurvedic" in text or "ayurvedic" in text:
                company_names.append(text)
        except Exception as e:
            print(f"Error occurred while processing {url}: {str(e)}")

    # Create a DataFrame from the list of company names
    df = pd.DataFrame({'Company Name': company_names})

    # Save the DataFrame to an Excel file
    df.to_excel('ayurvedic_companies_after_2019.xlsx')
    print("Company names saved to ayurvedic_companies_after_2019.xlsx")

def extract_text_from_url(url):
    # Dummy function to extract text from the webpage (replace with actual scraping logic)
    # For demonstration purposes, it simply returns a placeholder string
    return "Placeholder text extracted from URL: " + url

if __name__ == "__main__":
    # Define the search query
    query = "Ayurvedic companies in India  after 2019"

    # Scrape Google search results for company names and save them to an Excel file
    scrape_google_search_results(query)
