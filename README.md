# Automatic Asset Creation

This project allows you to automatically create assets in UiPath Orchestrator using data from an Excel file. It is built in Python and leverages the `requests` and `pandas` libraries.

## Project Structure

- **.env**  
  Environment variables required for the project.

- **pyproject.toml**  
  Configuration for linting and formatting using Ruff.

- **src/auth.py**  
  Contains the [`authenticate_uipath_orchestrator`](src/auth.py) function responsible for authenticating with UiPath Orchestrator.

- **src/create_assets.py**  
  Reads an Excel file, extracts asset data, and sends API requests to create assets in UiPath Orchestrator using the [`create_uipath_orchestrator_assets`](src/create_assets.py) function.

- **assets.xlsx**  
  Excel file that contains the asset data. The file must have a sheet named "Sheet1" with columns **Asset Name** and **Asset Value**.

## Prerequisites

- Python 3.8+  
- Required libraries: `pandas`, `requests`, `simplejson`

Install them via pip:

```sh
pip install pandas requests simplejson