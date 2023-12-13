import logging
from shared import constants

class LoggingModule:
    def __init__(self):
        self.alert_logger = logging.getLogger('fim_alert_logger')
        self.audit_logger = logging.getLogger('fim_audit_logger')
        self.fim_logger = logging.getLogger('fim_logger')

        # Set levels for each logger
        self.alert_logger.setLevel(logging.WARNING)
        self.audit_logger.setLevel(logging.INFO)
        self.fim_logger.setLevel(logging.INFO)

        # Create and add handlers to each logger with appropriate file paths
        alert_log_handler = logging.FileHandler(constants.ALERT_LOG_PATH)
        audit_log_handler = logging.FileHandler(constants.AUDIT_LOG_PATH)
        fim_log_handler = logging.FileHandler(constants.LOG_FILE)

        # Common format for both loggers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        alert_log_handler.setFormatter(formatter)
        audit_log_handler.setFormatter(formatter)
        fim_log_handler.setFormatter(formatter)

        self.alert_logger.addHandler(alert_log_handler)
        self.audit_logger.addHandler(audit_log_handler)
        self.fim_logger.addHandler(fim_log_handler)

    def log_alert(self, change):
        log_message = f"ALERT: Change detected in {change['file_path']}. Action: {change['action']}"
        # print(f"ALERT: Change detected in {change['file_path']}. Action: {change['action']}")
        self.alert_logger.warning(log_message)
        
    def log_change(self, change):
        log_message = f"Change logged - Path: {change['file_path']}. Action: {change['action']}, Timestamp: {change['timestamp']}"
        # print(f"Change logged - Path: {change['file_path']}. Action: {change['action']}, Timestamp: {change['timestamp']}")
        self.audit_logger.info(log_message)

    def log_server(self, change):
        log_message = f"Server Update - {change}"
        self.fim_logger.alert(log_message)

    # def basicConfig(self, level, format, filename):
    #     # Set up the basic configuration for the logging system
    #     logging.basicConfig(level=level, format=format, filename=filename)
