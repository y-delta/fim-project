# agent/src/file_monitor.py

import os 
import hashlib
from shared import constants

class FileMonitor:
    def __init__(self):
        self.monitored_paths = constants.MONITORED_PATHS

    def monitor_files(self):
        changes = []
        for path in self.monitored_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    last_modified = os.path.getmtime(file_path)

                    if file_path not in constants.FILE_STATE:
                        constants.FILE_STATE[file_path] = last_modified

                    if last_modified != constants.FILE_STATE[file_path]:
                        changes.append({
                            'file_path': file_path,
                            'action': 'modified',
                            'timestamp': time.time()
                        })
                        constants.FILE_STATE[file_path] = last_modified

        return changes
