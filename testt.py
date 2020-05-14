from bs4 import BeautifulSoup as soup
from selenium import webdriver

url = 'https://www.flipkart.com/search?q=oneplus%207t&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

driver = webdriver.Firefox()
driver.get(url)

html = driver.page_source
page = soup(html)

jobs = page.find_all('div',{"class":"_3BTv9X"})

for job in jobs:
    
    product_img = job.find('img',{'class':'_1Nyybr _30XEf0'})


    print('\nproduct image {}'.\
      format(product_img))
    print('\n')