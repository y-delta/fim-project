import os
import time
from file_monitor import FileMonitor
from communication import Communication
from shared import constants

def main():
    file_monitor = FileMonitor()
    communication = Communication()

    while True:
        changes = file_monitor.monitor_files()
        if changes:
            communication.send_data(changes)

        time.sleep(constants.MONITOR_INTERVAL)

if __name__ == "__main__":
    main()