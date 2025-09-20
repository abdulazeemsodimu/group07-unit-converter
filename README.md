# **Group 07 - Unit Converter with History**
A Python Unit Converter app built with Tkinter GUI.
The app lets you convert between Length, Mass, and Temperature units.
It also saves past conversions into a history file so users can view them later.

##  📖 Project Summary
This project is a Unit Converter Application built with Python.
The app provides a user-friendly interface for performing unit conversions and keeping a history of results

### Features
* Convert between Length, Mass, and Temperature
* Save conversion history into a JSON file
* Display history in GUI
* Clear history button
* Automated tests with pytest

### Requirements
- Python 3.10+
- pipenv (for environment & dependencies)

##  ⚙️ Setup Instructions
Run the following commands in **Git Bash**:

```bash
git clone https://github.com/abdulazeemsodimu/group07-unit-converter
cd group07-unit-converter
```

### Installation
Run the following commands in **Git Bash**:

```bash
### Set up environment
pip install pipenv
pipenv install --dev
pipenv shell

### Run the app
pipenv run python -m src.gui

### Run Tests
pipenv run pytest
```

## 👥 Team Roles
* Conversion Logic Team – Built converters.py (Length, Mass, Temperature classes)
* History Team – Implemented JSON save/load/clear features (history.py)
* GUI Team – Designed Tkinter interface (gui.py, buttons, dropdowns, history panel)
* Testing Team – Wrote pytest tests for converters and history
* Media Team – Maintains this README, documentation, and presentation materials

### Reflection
The commit history on GitHub clearly shows contributions from all members. 
Each feature branch was created, worked on, and merged, making the project’s development transparent and collaborative.

## 📂 Project Structure 
```
group07-unit-converter/
├── data/
│ └── history.json
├── src/
│ ├── __init__.py
│ ├── gui.py
│ ├── converters.py
│ └── history.py
├── tests/
│ ├── __init__.py
│ ├── test_converters.py
│ └── test_history.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── .gitignore
```

## 🎥 Demo Video
[Watch the demo](https://link-to-your-video.com)

## 📸 Screenshots
![App Screenshot](path/to/screenshot.png)
