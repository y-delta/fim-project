import os
import json

MONITORED_PATHS = ['/path/to/monitor'] # change
FILE_STATE = {}
MONITOR_INTERVAL = 60 #seconds
SERVER_URL = 'https://localhost:5000/recieve_data'
SERVER_PORT = 5000
CONFIG_FILE_PATH = './config.json' # change
HASH_ALGORITHM - 'sha3-256'

# Load config from file if available
if os.path.exists(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        config_data = json.load(config_file)
        MONITORED_PATHS = config_data.get('monitored_paths', MONITORED_PATHS)
        # Add other configuration parameters as needed