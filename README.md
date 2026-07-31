# iMacFanController

A small Python project for interacting with Apple SMC fan and sensor data on supported Macs.

## Project structure

- `main.py` – entry point for the application
- `smc.py` – Apple SMC discovery and low-level file access helpers
- `fan.py` – fan control logic
- `sensor.py` – sensor reading logic
- `requirements.txt` – Python dependencies

## Getting started

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Run the application:
   ```bash
   python main.py
   ```
