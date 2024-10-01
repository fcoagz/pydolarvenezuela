from typing import Literal
import requests
from curl_cffi import requests as cffi
import time
from ratelimit import limits, sleep_and_retry

CALLS = 5
RATE_LIMIT = 60

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
}

@sleep_and_retry
@limits(calls=CALLS, period=RATE_LIMIT)
def get(url: str, params: dict = None, verify: bool = True):
    """
    Realiza una solicitud HTTP GET utilizando la biblioteca requests con límite de tasa.
    """
    response = requests.get(url, params=params, verify=verify, timeout=10.0, headers=_headers)
    response.raise_for_status()
    
    return response.content

def curl(method: Literal['GET', 'POST'], url: str, headers: dict = None, data: dict = None, json: dict = None, impersonate: str = "chrome110"):
    """
    Realiza una solicitud HTTP utilizando cffi y permite la opción de impersonar un navegador.

    Args:
        - method (Literal['GET', 'POST']): El método HTTP a utilizar (GET o POST).
        - url (str): La URL a la que se enviará la solicitud.
        - headers (dict, opcional): Encabezados HTTP a incluir en la solicitud. Por defecto es None.
        - json (dict, opcional): Datos JSON a incluir en la solicitud. Por defecto es None.
        - impersonate (str, opcional): El navegador a impersonar. Por defecto es "chrome110".

    Returns:
        bytes: El contenido de la respuesta en formato de bytes.
    """
    if headers is None:
        headers = _headers
        
    response = cffi.request(method=method, url=url, impersonate=impersonate, headers=headers, data=data, json=json, timeout=10.0)
    response.raise_for_status()

    return response.content