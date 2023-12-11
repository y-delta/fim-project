# agent/src/communication.py

import requests
from shared.constants import SERVER_URL

class Communication:
    def send_data(self, changes):
        try:
            response.post(SERVER_URL, json=changes)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to Server: {e}")