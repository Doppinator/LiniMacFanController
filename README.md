# LiniMacFanController

A small Python project for interacting with Apple SMC fan and sensor data on supported Macs.

## Project structure

- `LiniMacFanController/Explorer/Sensors/` – temperature-sensor models
- `LiniMacFanController/Explorer/Fans/` – fan models
- `LiniMacFanController/Controller/` – fan-speed control policy
- `LiniMacFanController/SMC/` – Apple SMC discovery and low-level access
- `main.py` – application entry point

## Getting started

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Run the application:
   ```bash
   python3 main.py
   ```
