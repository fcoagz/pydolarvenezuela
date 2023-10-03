from datetime import datetime 
from babel.dates import format_date, format_time, get_timezone

class TimeDollar(object):
    def __init__(self) -> None:
        self.locality = get_timezone('America/Caracas')
        self.datetime_obj = datetime.now(self.locality)
    
    def get_time(self, date: str, dateofApi: bool = False):
        if dateofApi:
            datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
        else:
            datetime_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        
        return datetime_obj.strftime("%d/%m/%Y, %I:%M %p")
    
    def get_time_zone(self):
        formatted_date = format_date(self.datetime_obj.date(), format='full', locale='es')
        formatted_time = format_time(self.datetime_obj.time(), format='h:mm:ss a', locale='es')

        return {
            "date": formatted_date,
            "time": formatted_time
        }