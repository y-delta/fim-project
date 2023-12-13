import os
import json

FILE_STATE = {}

SERVER_URL = 'https://localhost:5000/recieve_data'
SERVER_PORT = 5000

HASH_ALGORITHM = 'sha3-256'
MONITOR_INTERVAL = 10 #seconds

MONITORED_PATHS = ['./test_directory/'] # change /path/to/monitor/
TRUSTED_PATHS = ['/path/to/trusted/files'] # change

LOG_FILE = './shared/logs/fim.log'
AUDIT_LOG_PATH = './shared/logs/audit.log'
ALERT_LOG_PATH = './shared/logs/alert.log'
CONFIG_FILE_PATH = './config.json' # change

# Load config from file if available
if os.path.exists(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, 'r') as config_file:
        config_data = json.load(config_file)
        MONITORED_PATHS = config_data.get('monitored_paths', MONITORED_PATHS)
        # Add other configuration parameters as needed