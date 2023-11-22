import requests
from curl_cffi import requests as cffi

def get(url: str, params: dict = None, verify: bool = True):
    response = requests.get(url, params=params, verify=verify, timeout=10.0)
    response.raise_for_status()
    
    return response.content

def curl(url: str, impersonate: str = "chrome110"):
    response = cffi.get(url, impersonate=impersonate, timeout=10.0)
    response.raise_for_status()

    return response.content