from fastapi import FastAPI
import requests 
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


KEY_API_WEATHER = "7fc41fc637a8312deb794c4ffd5a28e9"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/postalzip/{zip_code}")
def read_item(zip_code: str):
    METEO_API_URL = "http://api.openweathermap.org/data/2.5/weather?zip=" +zip_code+ ",fr&appid=" +KEY_API_WEATHER

    r = requests.get(METEO_API_URL)
    if r.status_code != 200 :
        return{ "CodeError" : r.status_code }
    else :
        return {"Result": r.json()} 
    
    # uvicorn main:app --relod...
    #  uvicorn main:app  --reload --host 0.0.0.0 --port 8000