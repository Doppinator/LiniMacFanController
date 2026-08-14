# LiniMacFanController

A small Python project for interacting with Apple SMC fan and sensor data on supported Macs.

## Project structure

- `LiniMacFanController/explorer/sensors/` – temperature-sensor models
- `LiniMacFanController/explorer/fans/` – fan models
- `LiniMacFanController/controller/` – fan-speed control policy
- `LiniMacFanController/smc/` – Apple SMC discovery and low-level access
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

## Sensor display

The monitor displays a concise set of canonical thermal readings: ambient,
CPU core and heatsink, GPU diode, and power supply.  SMC aliases are used only
when their canonical key is unavailable; unknown, model-specific keys are kept
in the explorer's sensor collection but hidden from the normal console view.

To support another Mac model, add its key and classification to
`explorer/sensors/sensor_registry.py`.
