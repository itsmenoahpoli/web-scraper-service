from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from lib.scraper_lib import exec_newsdata_scrape

app = FastAPI()

@app.get('/')
def index():
  return JSONResponse(
    status_code=status.HTTP_200_OK,
    content={
      "message": "SYSTEM_ONLINE"
    }
  )

@app.get('/api/exec-scrape')
def exec_scrape():
  try:
    exec_newsdata_scrape()

    return JSONResponse(
      status_code=status.HTTP_200_OK,
      content={
        "message": "TASK_SUCCEFFSULLY_EXECUTED"
      }
    )
  except:
    return JSONResponse(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      content={
        "message": "TASK_FAILED_TO_EXECUTE"
      }
    )
