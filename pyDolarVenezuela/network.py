import requests

def get(url: str, params: dict = None, verify: bool = True):
    response = requests.get(url, params=params, verify=verify, timeout=10.0)
    response.raise_for_status()
    
    return response.content