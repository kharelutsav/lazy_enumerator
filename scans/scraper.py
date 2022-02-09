from bs4 import BeautifulSoup
import requests as req

def scrap():
    resp = req.get("https://hackerone.com").text
    
    soup = BeautifulSoup(resp, 'lxml')
  
    for link in soup.find_all('a'):
        print(link.get('href'))
        

scrap()

