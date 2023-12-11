# agent/src/communication.py

import requests
from shared import constants

class Communication:
    def send_data(self, changes):
        try:
            response.post(constants.SERVER_URL, json=changes)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to Server: {e}")