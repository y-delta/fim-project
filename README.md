# Project Overview
This repository contains a Python-based project for monitoring file changes and managing configurations. This repository hosts two integral components:
- **Agent**: Diligently monitors file changes and relays this information.
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
Agent and Server configurations are adjustable in their respective config files. Modify 'constants.py' for environment-specific settings like intervals and URLs. SSL/TLS configurations are crucial for secure communications in Flask.

## Tests
The `tests` directory contains test scripts ensuring code functionality and reliability. Run the following commands from the root of the project directory to test application logic:

`python3 -m unittest tests.test_agent`
`python3 -m unittest tests.test_server`

## Log Files
The application generates log files for both the Agent and the Server. These logs contain information about file changes, alerts, and errors. Log files are stored in `shared/logs`, providing valuable information for monitoring and debugging.

1. alert.log - Creation, deletion and other alerts.
2. audit.log -Records file modifications and accesses.
3. fim.log - General application logs, includes errors, warnings and flask server logs. 

## Contributing
Contributions are welcome! Please get in touch with me on how to contribute to the project.


