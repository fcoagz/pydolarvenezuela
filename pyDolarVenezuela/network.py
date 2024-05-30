from typing import Literal
import requests
from curl_cffi import requests as cffi

def get(url: str, params: dict = None, verify: bool = True):
    response = requests.get(url, params=params, verify=verify, timeout=10.0)
    response.raise_for_status()
    
    return response.content

def curl(method: Literal['GET', 'POST'], url: str, headers: dict = None, json: dict = None, impersonate: str = "chrome110"):
    response = cffi.request(method=method, url=url, impersonate=impersonate, headers=headers, json=json, timeout=10.0)
    response.raise_for_status()

    return response.content