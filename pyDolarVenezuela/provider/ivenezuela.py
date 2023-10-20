from pyDolarVenezuela import network
from bs4 import BeautifulSoup

endpoint = 'venezuela/dolar/precio-dolar-venezuela-{0}-{1}-{2}-{3}-oficial-bcv-paralelo-monitor-dolartoday/'

def _get_price_and_symbol_in_simple(strong_tag: BeautifulSoup):
    price = str(strong_tag.find_next('strong').text).split('Bs.')[-1][:-1].strip()
    symbol = str(strong_tag.find_next('strong').text).split('Bs.')[-1][-1]

    return price, symbol

def _get_values_monitors(url: str):
    response = network.get(url)
    soup = BeautifulSoup(response, "html.parser")

    section_information_dollar = soup.find('div', 'td-post-content')
    monitors_simple = section_information_dollar.find('p', style='font-size:16px')
    image_monitors = section_information_dollar.find_all('div', 'wp-block-image')

    information  = _extract_simple_data(monitors_simple)
    image = _extract_image_data(image_monitors)
    result = {}

    for key, value in information.items():
        result[key] = value
        if key in image:
            result[key]['image'] = image[key]

    return result

def _extract_simple_data(monitors_simple):
    result = {}
    for strong_tag in monitors_simple.find_all('strong'):
        title_map = {
            'Dólar Oficial BCV': 'BCV',
            'Monitor': 'EnParaleloVzla',
            'Dolartoday': 'DolarToday'
        }
        for key, value in title_map.items():
            if key in strong_tag.text:
                price, symbol = _get_price_and_symbol_in_simple(strong_tag)
                result[value.lower()] = {'title': value, 'price': price.replace(',', '.'), 'symbol': symbol}
    return result

def _extract_image_data(image_monitors):
    result = {}
    for image in image_monitors:
        title_map = {
            'Tasa': 'bcv',
            'Monitor': 'enparalelovzla',
            'Dolartoday': 'dolartoday'
        }
        alt_text = str(image.find('img')['alt']).split(' ')[0]
        for key, value in title_map.items():
            if key in alt_text:
                if value not in result:
                    result[value] = [image.find('img')['src']]
                else:
                    result[value].append(image.find('img')['src'])
    return result

class iVenezuela:
    def __init__(self, url: str) -> None:
        self.url = url
        response  = network.get(url + 'precio-dolar-venezuela-dolartoday-monitor-oficial-bcv-hoy-tipo-de-cambio/')
        self.soup = BeautifulSoup(response, "html.parser")
    
    def _load(self):
        section_information_dollar = self.soup.find('div', 'td-post-content')

        for page in section_information_dollar.find_all('p', 'has-text-align-center'):
            if page.find('a'):
                href = page.find('strong').find('a')['href']
                date_text = page.find('a').text.split('hoy  ')[1::]
                
                self.data = _get_values_monitors(href)
                self.data['date'] = ' '.join(date_text)
                        
            elif 'Precio Dólar VENEZUELA' in page.text:
                date_words = str(page.text).split()[-5:]
                date_words.pop(2)

                href = self.url + endpoint.format(*date_words)

                self.data = _get_values_monitors(href)
                self.data['date'] = ' '.join(date_words)
    
    def get_values(self, monitor_code: str = None, name_property: str = None, prettify: bool = False):
        self._load()

        if not monitor_code:
            return self.data
        
        try:
            monitor_data = self.data[monitor_code.lower()]
            if name_property:
                value = monitor_data[name_property]
                return f'Bs. {value}' if prettify and name_property == 'price' else value
            return monitor_data
        except KeyError:
            raise KeyError("Does not match any of the properties that were provided in the dictionary. Most information: https://github.com/fcoagz/pyDolarVenezuela")