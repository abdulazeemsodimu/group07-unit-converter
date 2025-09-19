## Group 07 - Python Unit Converter with Tkinter GUI
##  Project Overview

This project is a Unit Converter Application built with Python.
It allows users to convert between different units of measurement such as Length, Mass, and Temperature.
The app also includes a Tkinter GUI for ease of use and stores past conversions in a JSON file.

##  Setup
On bash

### Requirements
- Python 3.10+
- pipenv (for environment & dependencies)

### Installation
Run the following commands in **Git Bash**:

```bash
pip install pipenv
pipenv install --dev
pipenv shell

### Run the app
On bash
pipenv run python src/gui.py

### Run Tests
On bash
pytest tests/

## Features
* Convert between Length, Mass, and Temperature
* Save conversion history into a JSON file
* Display history in GUI
* Clear history button
* Automated tests with pytest

## Team Roles
* Conversion Logic Team – Built converters.py (Length, Mass, Temperature classes)
* History Team – Implemented JSON save/load/clear features (history.py)
* GUI Team – Designed Tkinter interface (gui.py, buttons, dropdowns, history panel)
* Testing Team – Wrote pytest tests for converters and history
* Media Team – Maintains this README, documentation, and presentation materials

Commit history will reflect each member's contributions.

## Testing 
Run the automated tests with: pytest At least 2 passing tests are included (covering conversion logic and history).


## Project structures 
group07-unit-converter/
├── data/              # Stores history.json
├── src/               # Main application code
│   ├── converters.py  # Conversion logic
│   ├── history.py     # Save/load/clear history
│   ├── gui.py         # Tkinter GUI
│   └── __init__.py
├── tests/             # Pytest test files
│   ├── test_converters.py
│   └── test_history.py
├── Pipfile
├── Pipfile.lock
└── README.md


