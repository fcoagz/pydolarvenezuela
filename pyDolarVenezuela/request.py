from httpx import Response
import httpx

def _ensure_200_and_return_content(response: Response) -> bytes:
    if response.status_code != httpx.codes.OK:
        raise ValueError(f"I can't communicate with the Exchange Monitor page {response.status_code}")
    return response.content

def content(url: str) -> bytes:
    response = httpx.get(url, timeout=10.0)
    return _ensure_200_and_return_content(response)