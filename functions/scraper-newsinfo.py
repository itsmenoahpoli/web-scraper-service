import csv
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://newsinfo.inquirer.net/'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news articles on the page
articles = soup.find_all('div', id='ncg-info')

# Find the site name (if available)
site_name_element = soup.find('meta', property='og:title')
site_name = site_name_element['content'] if site_name_element else ''

# Create a CSV file and write the header
with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Name', 'Description', 'Link'])

    # Iterate over the articles and extract relevant information
    for article in articles:
        # Extract the title
        title_element = article.find('h1').find('a')
        title = title_element.text.strip() if title_element else ''

        # Extract the description (if available)
        description = ''  # No description available in the provided HTML

        # Extract the link
        link = title_element['href'] if title_element else ''

        # Write the row to the CSV file
        writer.writerow([title, site_name, description, link])
