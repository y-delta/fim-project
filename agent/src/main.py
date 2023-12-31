import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import time
from file_monitor import FileMonitor
from communication import Communication
from shared.constants import MONITOR_INTERVAL, SERVER_URL

def main():
    file_monitor = FileMonitor()
    communication = Communication()

    while True:
        try:
            changes = file_monitor.monitor_files()
            if changes:
                communication.send_data(changes)
        except Exception as e:
            print(f"Error in monitoring or communication: {e}")
        time.sleep(MONITOR_INTERVAL)

if __name__ == "__main__":
    # Constructing a file path based on the operating system
    os_type = os.name.lower()
    if os_type == 'posix':  # Linux or macOS
        path = os.path.join('/', 'etc', 'my_config.conf')
    elif os_type == 'nt':  # Windows
        path = os.path.join('C:\\', 'ProgramData', 'MyApp', 'config.ini')
    else:
        raise NotImplementedError(f"Unsupported operating system: {os_type}")

    print(f"Detected OS: {os_type}")
    print(f"File path: {path}")

    main()