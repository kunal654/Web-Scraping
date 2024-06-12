

# Ayurvedic Companies Scraper

This repository contains a Python script designed to scrape and collect information about Ayurvedic companies in India established after 2019 using Google search results, and to save the data into an Excel file.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Google Search Integration**: Utilizes the `googlesearch-python` library to perform Google searches programmatically.
- **Web Scraping**: Extracts text from the search result webpages to identify company names (with placeholder function for demonstration).
- **Data Storage**: Uses `pandas` to store the collected company names in an Excel file for easy access and analysis.

## Installation

### Clone the Repository

First, clone the repository to your local machine:
```bash
git clone https://github.com/kunal654/ayurvedic-companies-scraper.git
cd ayurvedic-companies-scraper
```

### Install Dependencies

Install the necessary Python libraries using pip:
```bash
pip install pandas googlesearch-python
```

## Usage

### Define Your Search Query

Open `scraper.py` and define your search query:
```python
query = "Ayurvedic companies in India after 2019"
```

### Run the Script

Execute the script to start the scraping process:
```bash
python scraper.py
```

### Output

The script will create an Excel file named `ayurvedic_companies_after_2019.xlsx` in the current directory, containing the names of the Ayurvedic companies.

## Script Overview

### `scrape_google_search_results(query)`

This function performs the following tasks:
1. Conducts a Google search for the specified query.
2. Iterates through the search results, extracting relevant text to identify Ayurvedic companies.
3. Stores the extracted company names in a pandas DataFrame.
4. Saves the DataFrame to an Excel file.

### `extract_text_from_url(url)`

A placeholder function designed to simulate extracting text from a webpage. In a real-world scenario, you would replace this with actual web scraping logic using libraries such as BeautifulSoup or Scrapy.

```python
def extract_text_from_url(url):
    # Dummy function to extract text from the webpage (replace with actual scraping logic)
    # For demonstration purposes, it simply returns a placeholder string
    return "Placeholder text extracted from URL: " + url
```

## Customization

### Web Scraping Logic

Replace the `extract_text_from_url(url)` function with actual scraping logic. For instance, using BeautifulSoup to parse HTML and extract relevant information:

```python
from bs4 import BeautifulSoup
import requests

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant information based on the HTML structure of the webpage
    text = soup.get_text()
    return text
```

### Modify Search Parameters

Adjust the parameters of the `googlesearch` function to change the number of search results or language:
```python
search_results = search(query, num_results=20, lang='en')
```

## Dependencies

- `pandas`: For data manipulation and storage.
- `googlesearch-python`: For performing Google searches programmatically.
- `BeautifulSoup` and `requests` (if replacing the placeholder scraping function with actual logic).

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contact
For any questions or issues, please open an issue on GitHub or contact me directly at kunalgautam489@gmail.com.



