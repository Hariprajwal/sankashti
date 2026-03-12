from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz
from sankashti import is_sankashti, next_sankashti, sankashti_year
from purnima import is_purnima, next_purnima, purnima_year
from amavasya import is_amavasya, next_amavasya, amavasya_year

IST = pytz.timezone("Asia/Kolkata")

app = FastAPI(title="Moon Events API")

# Enable CORS correctly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Moon Events API running"}

# Sankashti Routes
@app.get("/sankashti/today")
def sank_today():
    today = datetime.now(IST).date()
    return {
        "date": today,
        "is_sankashti": is_sankashti(today)
    }

@app.get("/sankashti/next")
def sank_next():
    return next_sankashti()

@app.get("/sankashti/year/{year}")
def sank_year_route(year: int):
    dates = sankashti_year(year)
    return {
        "year": year,
        "total": len(dates),
        "dates": dates
    }

# Purnima Routes
@app.get("/purnima/today")
def pur_today():
    today = datetime.now(IST).date()
    return {
        "date": today,
        "is_purnima": is_purnima(today)
    }

@app.get("/purnima/next")
def pur_next():
    return next_purnima()

@app.get("/purnima/year/{year}")
def pur_year_route(year: int):
    dates = purnima_year(year)
    return {
        "year": year,
        "total": len(dates),
        "dates": dates
    }

# Amavasya Routes
@app.get("/amavasya/today")
def am_today():
    today = datetime.now(IST).date()
    return {
        "date": today,
        "is_amavasya": is_amavasya(today)
    }

@app.get("/amavasya/next")
def am_next():
    return next_amavasya()

@app.get("/amavasya/year/{year}")
def am_year_route(year: int):
    dates = amavasya_year(year)
    return {
        "year": year,
        "total": len(dates),
        "dates": dates
    }