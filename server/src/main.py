# server/src/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import logging

from flask import Flask, request, jsonify
from config_management import ConfigManagement
from compliance_management import ComplianceManagement
from fim_logs import LoggingModule
from shared.constants import SERVER_PORT

import traceback

app = Flask(__name__)

config_management = ConfigManagement()
compliance_management = ComplianceManagement()
log_module = LoggingModule()

# log_module.basicConfig(
#     level=log_module.INFO,  # Set the desired logging level
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='fim.log'  # Specify the log file
# )

@app.route('/recieve_data', methods=['POST'])
def recieve_data():
    try:
        data = request.get_json()
        process_data(data)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

def process_data(data):
    for change in data:
        try:
            config_management.process_change(change)
            compliance_management.check_compliance(change)
            log_module.log_alert(change)
            log_module.log_change(change)
        except Exception as e:
            log_module.log_server(e)
            logging.error(f"Error processing change: {e}")


def get_ssl_context():
    return (os.path.join('certs', 'cert.pem'), os.path.join('certs', 'key.pem'))

if __name__ == "__main__":
    # Constructing a file path based on the operating system
    os_type = os.name.lower()
    if os_type == 'posix':  # Linux or macOS
        path = os.path.join('/', 'etc', 'server_config.conf')
    elif os_type == 'nt':  # Windows
        path = os.path.join('C:\\', 'ProgramData', 'ServerApp', 'config.ini')
    else:
        raise NotImplementedError(f"Unsupported operating system: {os_type}")

    print(f"Detected OS: {os_type}")
    print(f"File path: {path}")
    
    ssl_context = get_ssl_context()

    app.run(debug=True, host='0.0.0.0', port=SERVER_PORT, ssl_context=ssl_context)