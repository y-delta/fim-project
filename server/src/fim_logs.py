import logging
from shared import constants

class LoggingModule:
    def __init__(self):
        alert_log_handler = logging.FileHandler('alert_logs.log')
        audit_log_handler = logging.FileHandler('audit_logs.log')

        alert_log_handler.setLevel(logging.WARNING)
        audit_log_handler.setLevel(logging.INFO)

        self.logger = logging.getLogger('fim_logs')

        self.logger.addHandler(alert_log_handler)
        self.logger.addHandler(audit_log_handler)

    def log_alert(self, change):
        log_message = f"ALERT: Change detected in {change['file_path']}. Action: {change['action']}"
        self.logger.warning(log_message)
        
    def log_change(self, change):
        log_message = f"Change logged - Path: {change['file_path']}. Action: {change['action']}, Timestamp: {change['timestamp']}"
        self.logger.info(log_message)