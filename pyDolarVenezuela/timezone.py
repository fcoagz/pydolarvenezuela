import json
from datetime import datetime
from babel.dates import format_date, format_time 

from pyDolarVenezuela.request import get_content_page
from pyDolarVenezuela.util import ZONA_HORARIA_VENEZUELA

def get_time_zone():
    response = get_content_page(ZONA_HORARIA_VENEZUELA)
    datetime_str = json.loads(response)["datetime"]
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")

    formatted_date = format_date(datetime_obj.date(), format='full', locale='es')
    formatted_time = format_time(datetime_obj.time(), format='h:mm:ss a', locale='es')

    return {
        "date": formatted_date,
        "time": formatted_time
    }