# utils/request_handler.py

import requests
from config.settings import Config

class RequestHandler:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.default_headers = {
            "Content-Type": "application/json"
        }
        if Config.AUTH_TOKEN:
            self.default_headers["Authorization"] = f"Bearer {Config.AUTH_TOKEN}"

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self._merge_headers(headers)
        response = requests.get(url, headers=final_headers, params=params, timeout=Config.TIMEOUT)
        return response

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self._merge_headers(headers)
        response = requests.post(url, headers=final_headers, json=data, timeout=Config.TIMEOUT)
        return response

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self._merge_headers(headers)
        response = requests.put(url, headers=final_headers, json=data, timeout=Config.TIMEOUT)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self._merge_headers(headers)
        response = requests.delete(url, headers=final_headers, timeout=Config.TIMEOUT)
        return response

    def _merge_headers(self, custom_headers):
        """
        Merge default headers with any custom headers provided.
        """
        if custom_headers:
            merged = self.default_headers.copy()
            merged.update(custom_headers)
            return merged
        return self.default_headers
