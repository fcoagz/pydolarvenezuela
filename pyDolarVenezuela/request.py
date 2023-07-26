import requests
from requests import Response

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def ensure_200_and_return_content(response: Response) -> bytes:
    if not response.status_code == requests.codes.ok:
        raise ValueError("Error de comunicación Alcambio. Codigo: {0}".format(response.status_code))
    return response.content

def get_content_page(url: str) -> bytes:
    return ensure_200_and_return_content(
        requests.get(url=url)
    )