import os
import csv
import requests
from datetime import date
from bs4 import BeautifulSoup

def create_filename(name, path = './scraped_data'):
  if not os.path.exists(path):
    os.makedirs(path)

  return f"{path}/{date.today()}-{name}.csv"

def scrape_bbc_data():
  url = 'https://www.bbc.co.uk/news'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  articles = soup.find_all('div', class_='gs-c-promo')

  site_name = soup.find('meta', property='og:site_name')['content']

  with open(create_filename('bbc_news'), 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Name', 'Description', 'Link'])

    for article in articles:
      title = article.find('h3').text.strip()
      description_element = article.find('p')
      description = description_element.text.strip() if description_element else ''

      link = url + article.find('a')['href']
      writer.writerow([title, site_name, description, link])


def scrape_newsinfo_data():
  url = 'https://newsinfo.inquirer.net/'

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  articles = soup.find_all('div', id='ncg-info')

  site_name_element = soup.find('meta', property='og:title')
  site_name = site_name_element['content'] if site_name_element else ''

  with open(create_filename('newsinfoinq_news'), 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Name', 'Description', 'Link'])

    for article in articles:
      title_element = article.find('h1').find('a')
      title = title_element.text.strip() if title_element else ''
      description = ''  

      link = title_element['href'] if title_element else ''
      writer.writerow([title, site_name, description, link])


def exec_newsdata_scrape():
  scrape_bbc_data()
  scrape_newsinfo_data()

  # Get scraped data from csv files
  bbc_news_data = []
  newsinfo_data = []

  # Loop bbc_news data csv file
  with open(f"./scraped_data/{date.today()}-bbc_news.csv") as bbcnewsCsv:
    csv_reader = csv.reader(bbcnewsCsv, delimiter=',')
    line_count = 0

    bbc_cols = None
    newsinfo_cols = None

    for row in csv_reader:
      if line_count == 0:
        line_count += 1
        bbc_cols = row

      else:
        line_count += 1
        bbc_news_data.append(dict({
          bbc_cols[0].lower(): row[0],
          bbc_cols[1].lower(): row[1],
          bbc_cols[2].lower(): row[2],
          bbc_cols[3].lower(): row[3]
        }))

  # Loop bbc_news data csv file
  with open(f"./scraped_data/{date.today()}-newsinfoinq_news.csv") as newsinfoCsv:
    csv_reader = csv.reader(newsinfoCsv, delimiter=',')
    line_count = 0

    bbc_cols = None

    for row in csv_reader:
      if line_count == 0:
        line_count += 1
        newsinfo_cols = row

      else:
        line_count += 1
        newsinfo_data.append(dict({
          newsinfo_cols[0].lower(): row[0],
          newsinfo_cols[1].lower(): row[1],
          newsinfo_cols[2].lower(): row[2],
          newsinfo_cols[3].lower(): row[3]
        }))

  # Prepare http request for news dashboard API
  data = {
    "bbc_news": bbc_news_data,
    "newsinfo_news": newsinfo_data
  }

  headers = {'Content-Type': 'application/json'}
  
  response = requests.post('http://127.0.0.1:8000/api/v1/news/insert', json=data, headers=headers)

  print(response)
  if response.status_code == "200":
    return 'SUCCESS'
  else:
    return 'FAILED'


