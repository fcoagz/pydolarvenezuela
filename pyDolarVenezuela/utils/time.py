from babel.dates import format_date, format_time
from datetime import datetime, timedelta
from pytz import timezone

from .extras import time_units

standard_time_zone = timezone('America/Caracas')

def get_datestring_to_datetime(date_string: str):
    """
    Formatear string a datetime.
    """
    date_time = date_string.split(' ')
    datetime_obj = datetime.now(standard_time_zone)
    if len(date_time) > 1:
        return datetime_obj.strptime(date_string, '%d/%m/%Y, %I:%M %p')
    else:
        return datetime_obj.strptime(date_string, '%d/%m/%Y')
    
def get_formatted_timestamp(date_timestamp_ms: int):
    """
    Formatear milisegundos a datetime.
    """
    timestamp_s  = date_timestamp_ms / 1000.0
    datetime_obj = datetime.fromtimestamp(timestamp_s, standard_time_zone)
    
    return datetime_obj

def get_formatted_date_bcv(date_string: str):
    """
    Formatear datetime.
    """
    datetime_obj = datetime.now(standard_time_zone).fromisoformat(date_string)
    
    return datetime_obj

def get_formatted_date(date_string: str):
    """
    Formatear datetime.
    """
    datetime_obj = datetime.fromisoformat(date_string).astimezone(standard_time_zone)
    
    return datetime_obj

def get_time(date_string: str):
    """
    Formatear datetime.
    """
    datetime_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    
    return datetime_obj

def get_formatted_time(date_string: str):
    """
    Formatear string a datetime. Solo que esta formateada primeramente como (Hace una Hora).
    """
    datetime_obj = datetime.now(standard_time_zone)
    listdate = date_string.split(' ')

    if len(listdate) == 3:
        time = listdate[-1]

        if listdate[1] == "un" or listdate[1] == "una":
            hms = 1
        else:
            hms = int(listdate[1])
        
        duration = timedelta(**{time_units[time]: hms})
        exact_time = datetime_obj - duration

        if time == "día" or time == "días":
            return exact_time
            
        return exact_time
        
    elif len(listdate) == 5:
        duration = timedelta(days=30)

        exact_time = datetime_obj - duration
        return exact_time
        
    else:
        return None 

def get_time_zone():
    """
    Obtener la hora actual de Venezuela.
    """
    datetime_obj = datetime.now(standard_time_zone)

    formatted_date = format_date(datetime_obj.date(), format='full', locale='es')
    formatted_time = format_time(datetime_obj.time(), format='h:mm:ss a', locale='es')

    return {
        "date": formatted_date,
        "time": formatted_time
    }