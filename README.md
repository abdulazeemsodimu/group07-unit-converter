## Group 07 - Python Unit Converter with Tkinter GUI
## 📌 Project Overview

This project is a Unit Converter Application built with Python.
It allows users to convert between different units of measurement such as Length, Mass, and Temperature.
The app also includes a Tkinter GUI for ease of use and stores past conversions in a JSON file.

## 🚀 Features
•	- Convert between units within categories (Length, Mass, Temperature).
•	- Simple and interactive Tkinter GUI.
•	- Save and view conversion history.
•	- Clear history when needed.
•	- Persistent storage using JSON.
•	- Tested with pytest.

## 🛠️ Project Structure

group07-unit-converter/
│
├── src/                  # Source code
│   ├── __init__.py
│   ├── converters.py     # Conversion logic
│   ├── gui.py            # Tkinter GUI
│   └── history.py        # Save & load history
│
├── tests/                # Unit tests
│   ├── __init__.py
│   ├── test_converters.py
│   └── test_history.py
│
├── data/
│   └── history.json      # Stores conversion history
│
├── Pipfile               # Pipenv dependencies
├── Pipfile.lock
└── README.md             # Project documentation

## ⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/abdulazeemsodimu/group07-unit-converter.git
cd group07-unit-converter
2. Setup Virtual Environment (Pipenv)
pipenv install --dev
pipenv shell
3. Run the Application
python src/gui.py
4. Run Tests
pytest

