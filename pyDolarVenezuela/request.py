import requests

def _get_response_content(response: requests.Response):
    if not response.status_code == requests.codes.ok:
        raise ValueError("Connection error on the page")
    return response.content