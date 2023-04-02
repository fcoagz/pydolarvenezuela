import requests
from bs4 import BeautifulSoup

def price():
  webSite = "https://monitordolarvenezuela.com/"
  
  webResult = requests.get(webSite)
  dataWeb = BeautifulSoup(webResult.content, 'html.parser')
  divElements = dataWeb.find_all('div', 'col-12 col-sm-4 col-md-2 col-lg-2')
  
  priceResult = []

  for divElement in divElements:
    text = divElement.find('p')
    priceResult.append(text.text.split(' ')[-1].replace(',', '.'))

  return {
    '$bcv' : f'Bs. {priceResult[0]}',
    '$enparalelovzla' : f'Bs. {priceResult[1]}',
    '$dolartoday' : f'Bs. {priceResult[2]}',
    '$monitordolarweb' : f'Bs. {priceResult[3]}',
    '$enparalelovzlavip' : f'Bs. {priceResult[4]}',
    '$binancep2p' : f'Bs. {priceResult[5]}'
  }
    