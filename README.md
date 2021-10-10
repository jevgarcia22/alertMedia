# Take home assignment
Script created with Selenium and Python to follow a given set of instructions.

### General Info
This project runs a simple script to:
- Navigate to Google
- Search for term (stackoverflow)
- Select the appropriate Google result
- Open Stackoverflow.com menu and select Tags
- Filter Tags for Python-3.6
- Find and select the question with the highest number of votes
- Print the author of the answer to the above question with the highest number of votes

### Technologies
Project created with:
- Python 3.6
- Selenium
- Chromedriver 94.0.4606.61
  - see https://chromedriver.chromium.org/getting-started for more info on Chromedriver

### Setup
First, clone the repo:
```
git clone https://github.com/jevgarcia22/alertMedia.git
```
Navigate to the project root
Create a virtual environment
```
python3 -m venv env
```
Activate the virtual environment
```
source venv/bin/activate
```
Install dependencies into the virtual environment
```
pip install -r requirements.txt
```
### Running Script
To execute from the command line:
```
python3 script.py
```
