from pyDolarVenezuela.pages import BCV, Italcambio
from pyDolarVenezuela import Monitor, CheckVersion, Redis

CheckVersion.check = False
r = Redis(
  host='redis-16930.c85.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16930,
  password='JHWNV3nRQwWipES10m7g7oFRWinmZKU1')
m = Monitor(Italcambio, db=r)
print(m.get_value_monitors())
