import re
from bs4 import BeautifulSoup

from ..network import get
from ..utils import time
from ..utils.extras import list_monitors_images
from ..pages import EnParaleloVzla as EnParaleloVzlaPage
from ._base import Base

pattern = r"🗓 (\d{2}/\d{2}/\d{4})🕒 (\d{1,2}:\d{2} [AP]M)💵 (Bs\. \d{2},\d{2})(🔺|🔻|🟰) (\d{1,2},\d{2}%) Bs (\d{1,2},\d{2})"
url_image = 'https://res.cloudinary.com/dcpyfqx87/image/upload/v1721329079/enparalelovzla/jmdvqvnopoobzmdszno3.png'

class EnParaleloVzla(Base):
    PAGE = EnParaleloVzlaPage

    @classmethod
    def _load(cls, **kwargs):
        html = get(cls.PAGE.provider)
        soup = BeautifulSoup(html, 'html.parser')
        
        widget_messages = soup.find_all('div', 'tgme_widget_message_wrap js-widget_message_wrap')
        last_occurrences = []

        for widget in widget_messages:
            message = widget.find('div', 'tgme_widget_message text_not_supported_wrap js-widget_message')
            if message is not None:
                data_message = message.find('div', 'tgme_widget_message_bubble')
                text_message = data_message.find('div', 'tgme_widget_message_text js-message_text')
                
                if text_message is not None:
                    result = re.search(pattern, text_message.text.strip())
                    if result:
                        price = float(result.group(3).replace('Bs. ', '').replace(',', '.'))
                        percent = result.group(5).replace(',', '.').replace('%', '')    
                        change = result.group(6).replace(',', '.')
                        symbol = "▼" if result.group(4) == '🔻' else "▲" if result.group(4) == '🔺' else ""
                        color  = "red" if symbol == '▼' else "green" if symbol == '▲' else "neutral"
                        # url_message = data_message.find('a', 'tgme_widget_message_photo_wrap').get('href')
                        date_message = data_message.find('div', 'tgme_widget_message_info short js-message_info').\
                            find('time').get('datetime')
                        last_update = time.get_formatted_date(date_message)

                        data = {
                            'key': 'enparalelovzla',
                            'title': 'EnParaleloVzla',
                            'price': price,
                            'last_update': last_update,
                            'image': url_image,
                            'percent': percent,
                            'change': change,
                            'color': color,
                            'symbol': symbol
                        }
                        last_occurrences.append(data)
        if last_occurrences:
            return [last_occurrences[-1]]
        return None