from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
def index():
  return {
    "system-healthcheck": "Running"
  }
