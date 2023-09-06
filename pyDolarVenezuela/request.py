from httpx import Response
import httpx

def _ensure_200_and_return_content(response: Response) -> bytes:
    if response.status_code != httpx.codes.OK:
        raise ValueError("")
    return response.content

# def ask(url: str, params: dict):
#     response = httpx.get(url, params=params, timeout=10.0)
#     return _ensure_200_and_return_content(response)

def content(url: str) -> bytes:
    response = httpx.get(url, timeout=10.0)
    return _ensure_200_and_return_content(response)