from datetime import datetime, timedelta 
from babel.dates import format_date, format_time, get_timezone

class Time(object):
    def __init__(self) -> None:
        locality = get_timezone('America/Caracas')
        self.datetime_obj = datetime.now(locality)
    
    def get_time(self, date: str):
        datetime_f = self.datetime_obj
        listdate = date.split(' ')

        if len(listdate) == 3:
            time = listdate[-1]
            
            if listdate[1] == "un" or listdate[1] == "una":
                hms = 1
            else:
                hms = int(listdate[1])

            time_units = {
                "semana": "weeks", "semanas": "weeks",
                "día": "days", "días": "days",
                "horas": "hours", "hora": "hours",
                "minutos": "minutes", "minuto": "minutes",
                "segundos": "seconds", "segundo": "seconds"
            }
            
            duration = timedelta(**{time_units[time]: hms})
            exact_time = datetime_f - duration

            if time == "día" or time == "días":
                return exact_time.strftime("%d/%m/%Y") 
            
            return exact_time.strftime("%d/%m/%Y, %I:%M %p")
        
        elif len(listdate) == 5:
            duration = timedelta(days=30)

            exact_time = datetime_f - duration
            return exact_time.strftime("%d/%m/%Y")
        
        else:
            return None 

    def get_time_zone(self):
        formatted_date = format_date(self.datetime_obj.date(), format='full', locale='es')
        formatted_time = format_time(self.datetime_obj.time(), format='h:mm:ss a', locale='es')

        return {
            "date": formatted_date,
            "time": formatted_time
        }