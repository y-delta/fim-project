# Project Overview
This repository contains a Python-based project for monitoring file changes and managing configurations. This repository hosts two integral components:
- **Agent**: Regularly monitors file changes and relays this information.
- **Server**: Processes received data, logs activities for audit compliance, and handles configuration management.
## Prerequisites
- Python 3.x
- Flask, Werkzeug, requests, watchdog (see `requirements.txt`)

## Installation
1. Clone the repository: `git clone https://github.com/y-delta/fim-project.git`
2. Install dependencies: `pip install -r requirements.txt`

## Running the Application
### Agent
1. Navigate to the agent directory: `cd agent/src/`
2. Run the agent script: `python agent.py`

### Server
1. Navigate to the server directory: `cd server/src/`
2. Run the server script: `python server.py`

## Docker
The `docker-compose.yml` sets up the Agent and Server. It includes configurations for building Docker images, container naming, restart policies, and port mappings for the Server.

To build using docker-compose, run the following command:

`docker-compose up --build`


To build Docker images for both the agent and server, use the following commands:
1. Agent: `docker build -t agent-image . -f Dockerfile.agent`
2. Server: `docker build -t server-image . -f Dockerfile.server`

## Configuration
Agent and Server configurations are adjustable in their respective config files. Modify 'constants.py' for environment-specific settings like intervals and URLs. SSL/TLS configurations are crucial for secure communications in Flask. `constants.py` contains key configuration settings for the FIM Project. Adjustments to these settings will affect how the application monitors files and communicates with the server. Following are the parameters that can be configured to suit your environment: 

#### `SERVER_URL` and `SERVER_PORT`
- `SERVER_URL`: The URL where the server listens for data. Change to match your server's address.
- `SERVER_PORT`: The port number for the Flask server. Modify if using a different port.

#### `HASH_ALGORITHM`
- Defines the hashing algorithm for file integrity checks. Change as needed for different security levels or performance requirements.

#### `MONITOR_INTERVAL`
- Sets how often (in seconds) the system checks for file changes. Decrease for more frequent checks, increase for less frequent checks.

#### `MONITORED_PATHS` and `TRUSTED_PATHS`
- `MONITORED_PATHS`: Directories to be monitored. Replace './test_directory/' with actual paths to monitor.
- `TRUSTED_PATHS`: Directories considered safe. Change to reflect your trusted file locations.

#### `LOG_FILE`, `AUDIT_LOG_PATH`, and `ALERT_LOG_PATH`
- Specify paths for different log files (`fim.log`, `audit.log`, `alert.log`). Adjust paths as needed.

#### `CONFIG_FILE_PATH`
- Path to an external JSON configuration file. Alter if your config file is located elsewhere.

#### Dynamic Configuration Loading
If a configuration file exists at `CONFIG_FILE_PATH`, the system will override `MONITORED_PATHS` and potentially other settings with values from this file. Add additional parameters as required.


## Tests
The `tests` directory contains test scripts ensuring code functionality and reliability. Run the following commands from the root of the project directory to test application logic:

`python3 -m unittest tests.test_agent`

`python3 -m unittest tests.test_server`

## Log Files
The application generates log files for both the Agent and the Server. These logs contain information about file changes, alerts, and errors. Log files are stored in `shared/logs`, providing valuable information for monitoring and debugging.

1. `alert.log` - Creation, deletion and other alerts.
2. `audit.log` -Records file modifications and accesses.
3. `fim.log` - General application logs, includes errors, warnings and flask server logs. 

## Contributing
Contributions are welcome! Please get in touch with me on how to contribute to the project.


