# /server/src/compliance_managment.py

import hashlib
import os
import logging
from datetime import datetime
from shared.constants import HASH_ALGORITHM, FILE_STATE, TRUSTED_PATHS, LOG_FILE

logger = logging.getLogger(__name__)

class ComplianceManagement:
    def __init__(self):
        self.allowed_hash_algorithms = ['sha256', 'sha1', 'md5', 'sha3-256']  # Add more if needed
        self.log_file = LOG_FILE

    def check_compliance(self, change):
        file_path = change.get('file_path')
        action = change.get('action')

        if action == 'modified':
            self.check_file_integrity(file_path)

    def check_file_integrity(self, file_path):
        if file_path not in FILE_STATE:
            logging.warning(f"File path {file_path} not found in FILE_STATE.")
        return
        
        if HASH_ALGORITHM not in self.allowed_hash_algorithms:
            logger.error(f"Error: Unsupported hash algorithm '{HASH_ALGORITHM}'.")
            return

        current_hash = self.calculate_file_hash(file_path)

        if file_path not in TRUSTED_PATHS:
            if current_hash != FILE_STATE[file_path]:
                self.handle_integrity_violation(file_path, current_hash)

    def calculate_file_hash(self, file_path):
        hasher = hashlib.new(HASH_ALGORITHM)

        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hasher.update(chunk)

        return hasher.hexdigest()

    def handle_integrity_violation(self, file_path, current_hash):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as log:
            log.write(f"{timestamp} - File integrity violation: '{file_path}' modified. New hash: {current_hash}\n")
        logger.error(f"Alert: File integrity violation - '{file_path}' has been modified.")
        # Implement action for file integrity violation, like, notify admin