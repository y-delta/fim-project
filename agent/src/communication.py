# agent/src/communication.py

import requests
from shared.constants import SERVER_URL

class Communication:
    def send_data(self, changes):
        try:
            response = requests.post(SERVER_URL, json=changes, verify=False) #change
            response.raise_for_status()
            print("PRINT!",changes)
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to Server: {e}")