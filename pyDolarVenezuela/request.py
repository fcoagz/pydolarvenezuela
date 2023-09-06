from requests import Response
import requests

def _ensure_200_and_return_content(response: Response) -> bytes:
    if response.status_code != requests.codes.ok:
        raise ValueError("")
    return response.content

def content(url: str) -> bytes:
    response = requests.get(url, timeout=10.0)
    return _ensure_200_and_return_content(response)