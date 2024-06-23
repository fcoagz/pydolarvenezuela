from typing import Literal
import requests
from curl_cffi import requests as cffi

_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
}

def get(url: str, params: dict = None, verify: bool = True):
    """
    Realiza una solicitud HTTP GET utilizando la biblioteca requests.

    Args:
        - url (str): La URL a la que se enviará la solicitud GET.
        - params (dict, opcional): Parámetros que se incluirán en la solicitud. Por defecto es None.
        - verify (bool, opcional): Si se debe verificar el certificado SSL. Por defecto es True.

    Returns:
        bytes: El contenido de la respuesta en formato de bytes.
    """
    response = requests.get(url, params=params, verify=verify, timeout=10.0, headers=_headers)
    response.raise_for_status()
    
    return response.content

def curl(method: Literal['GET', 'POST'], url: str, headers: dict = None, json: dict = None, impersonate: str = "chrome110"):
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
        
    response = cffi.request(method=method, url=url, impersonate=impersonate, headers=headers, json=json, timeout=10.0)
    response.raise_for_status()

    return response.content