import csv
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.bbc.co.uk/news'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news articles on the page
articles = soup.find_all('div', class_='gs-c-promo')

# Find the site name
site_name = soup.find('meta', property='og:site_name')['content']

# Create a CSV file and write the header
with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Name', 'Description', 'Link'])

    # Iterate over the articles and extract relevant information
    for article in articles:
        # Extract the title
        title = article.find('h3').text.strip()

        # Extract the description (if available)
        description_element = article.find('p')
        description = description_element.text.strip() if description_element else ''

        # Extract the link
        link = url + article.find('a')['href']

        # Write the row to the CSV file
        writer.writerow([title, site_name, description, link])