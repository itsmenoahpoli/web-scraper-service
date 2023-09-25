import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&sort=relevance'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

product_listings = soup.find_all('div', class_='_2kHMtA')

with open('laptops.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Rating', 'Link'])

    # Loop through each product listing and write its details to the CSV file
    for product in product_listings:
        title = product.find('div', class_='_4rR01T').text.strip()
        price = product.find('div', class_='_30jeq3 _1_WHN1').text.strip()[1:].replace(',', '')
        rating = product.find('div', class_='_3LWZlK')
        rating = rating.text.strip() if rating else ''
        link = 'https://www.flipkart.com' + product.find('a', class_='_1fQZEK')['href']
        writer.writerow([title, price, rating, link])

print('Scraping completed!')