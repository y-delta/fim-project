# agent/src/file_monitor.py

import os 
import hashlib
import time
from shared.constants import MONITORED_PATHS, FILE_STATE

class FileMonitor:
    def __init__(self):
        self.monitored_paths = ['/home/kali/Projects/fim-project/test_directory/']

    def monitor_files(self):
        changes = []
        for path in self.monitored_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    print(file)
                    file_path = os.path.join(root, file)
                    last_modified = os.path.getmtime(file_path)

                    if file_path not in FILE_STATE:
                        FILE_STATE[file_path] = last_modified

                    if last_modified != FILE_STATE[file_path]:
                        changes.append({
                            'file_path': file_path,
                            'action': 'modified',
                            'timestamp': time.time()
                        })
                        FILE_STATE[file_path] = last_modified
            print(changes)
        return changes
