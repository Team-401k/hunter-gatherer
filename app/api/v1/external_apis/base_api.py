import requests


class BaseApi:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def make_request(
        self,
        url: str,
        method: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
    ) -> dict:
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        if data is None:
            data = {}

        # Construct the full URL, so this function should only be passed the part of the url that is not base (see pp_api.py)
        full_url = self.base_url + url

        # Make the HTTP request
        response = requests.request(
            method,
            full_url,
            headers=headers,
            params=params,
            json=data,
        )

        # Check the response status and return the JSON data or raise an exception
        if response.status_code in [200, 201]:
            return response.json()
        else:
            response.raise_for_status()
