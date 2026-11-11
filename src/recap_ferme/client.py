import requests

BASE_URL = "https://api.openf1.org/v1"

session = requests.Session()

def _request(path: str, params: dict = {}):
    full_path = BASE_URL + path
    if params:
        full_path += "?"
        for key, val in params.items():
            full_path += str(key) + "=" + str(val) + "&"
        full_path = full_path[:-1]
    response = session.get(full_path, timeout=5)
    response.raise_for_status()
    return response.json()

