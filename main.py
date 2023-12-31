from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every
from lib.scraper_lib import exec_newsdata_scrape

app = FastAPI()

"""
  Initialize repeated-task (daily) to
  execute web scraping function
  and generate CSV
"""
@app.on_event('startup')
# @repeat_every(seconds=86400)
@repeat_every(seconds=60)
def get_daily_news():
  try:
    task = exec_newsdata_scrape()

    print (task)

    if task == "FAILED":
      print('FAILED_TO_SCRAPED_DATA')
    else:
      print('SUCCESSFULLY_SCRAPED_DATA')
  except:
    print('SOMETHING_WENT_WRONG')

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
    task = exec_newsdata_scrape()

    if task == 'FAILED':
      return JSONResponse(
        status_code=status.HTTP_200_OK, 
        content={
          "message": "TASK_SUCCEFFSULLY_EXECUTED"
        }
      )
    else:
      return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
          "message": "TASK_SUCCEFFSULLY_EXECUTED"
        }
      )
  except Exception as e:
    return JSONResponse(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      content={
        "message": "INTERNAL_SERVER_ERROR",
        "error": e
      }
    )
