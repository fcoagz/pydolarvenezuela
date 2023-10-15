from babel.dates import format_date, format_time
from datetime import datetime, timedelta
from pytz import timezone

standard_time_zone = timezone('America/Caracas')

def get_time(date_string: str):
    """
    Formatear datetime a string.
    """
    datetime_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    
    return datetime_obj.strftime('%d/%m/%Y, %I:%M %p')

def get_time_standard(date_string: str):
    """
    Formatear datetime a string. Restando las horas que tuvo la ultima actualizacion del monitor \
    por la zona horaria universal.
    """
    rested_hours = timedelta(hours=4)
    time_zone_utc = datetime.fromisoformat(date_string[:-1])
    datetime_obj = time_zone_utc - rested_hours

    return datetime_obj.strftime('%d/%m/%Y, %I:%M %p')

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