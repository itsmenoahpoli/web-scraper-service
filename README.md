## Web Scraper Service
Build using Python, FastAPI & Uvicorn


### Prerequisites
Python 3.10+ installed

#### Installation Guide (Terminal/CMD commands in sequence)
```bash

git clone https://github.com/itsmenoahpoli/web-scraper-service.git

cd web-scraper-service

python -m venv .venv


# If using venv (https://docs.python.org/3/library/venv.html)
# For MacOS
source .venv/bin/activate
# For Windows
./venv/Scripts/activate


# If using pipenv (https://pipenv.pypa.io/en/latest/)
pipenv shell

pipenv install -r requirements.txt


# Run the server
uvicorn main:app --reload

# Open a web browser with url of `http://localhost:8000`
```