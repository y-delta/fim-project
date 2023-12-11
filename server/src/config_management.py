# server/src/config_managment.py
import json
from shared.constants import CONFIG_FILE_PATH

logger = logging.getLogger(__name__)

class ConfigManagement:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(CONFIG_FILE_PATH, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            logger.warning(f"Config file '{CONFIG_FILE_PATH}' not found. Using default config.")
            return {}
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON in '{CONFIG_FILE_PATH}'. Check the file format.")
            return {}

    def process_change(self, change):
        file_path = change.get('file_path')
        action = change.get('action')

        if action == 'modified':
            self.check_sensitive_config(file_path)

    def check_sensitive_config(self, file_path):
        if file_path in self.config.get('sensitive_files', []):
            logger.warning(f"Alert: Sensitive config file '{file_path}' has been modified.")
            # Implement action for a sensitive config file modification, e.g., notify admin
