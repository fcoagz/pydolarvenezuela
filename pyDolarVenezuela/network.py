import httpx

def get(url: str, params: dict = None, verify: bool = True):
    response = httpx.get(url, verify=verify, timeout=10.0) if not params else httpx.get(url, params=params, timeout=10.0)

    if response.status_code == httpx.codes.OK:
        return response.content
    raise ValueError(f"We could not connect to the page {url}. Status Code: {response.status_code}")