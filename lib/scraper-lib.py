import csv
import requests
from bs4 import BeautifulSoup

def scrape_bbc_data(self):
  # URL of the website to scrape
  url = 'https://www.bbc.co.uk/news'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  articles = soup.find_all('div', class_='gs-c-promo')

  site_name = soup.find('meta', property='og:site_name')['content']

  with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['Title', 'Name', 'Description', 'Link'])

      for article in articles:
          title = article.find('h3').text.strip()
          description_element = article.find('p')
          description = description_element.text.strip() if description_element else ''

          link = url + article.find('a')['href']
          writer.writerow([title, site_name, description, link])


def scrape_newsinfo_data(self):
  url = 'https://newsinfo.inquirer.net/'

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  articles = soup.find_all('div', id='ncg-info')

  site_name_element = soup.find('meta', property='og:title')
  site_name = site_name_element['content'] if site_name_element else ''

  with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['Title', 'Name', 'Description', 'Link'])

      for article in articles:
          title_element = article.find('h1').find('a')
          title = title_element.text.strip() if title_element else ''
          description = ''  

          link = title_element['href'] if title_element else ''
          writer.writerow([title, site_name, description, link])