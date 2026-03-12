from datetime import datetime, timedelta
from astronomy import get_tithi, get_sunrise, jd_to_datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")


def is_amavasya(date):
    """
    Amavasya is the 30th Tithi.
    We check the Tithi at sunrise.
    """
    sunrise = get_sunrise(date)
    dt = jd_to_datetime(sunrise)
    tithi = get_tithi(dt)
    return tithi == 30


def next_amavasya():
    today = datetime.now(IST).date()
    for i in range(40):
        d = today + timedelta(days=i)
        if is_amavasya(d):
            return {
                "date": d,
                "days_until": (d - today).days,
                "about": "The New Moon day, sacred for Pitru Tarpan and spiritual practices."
            }
    return None


def amavasya_year(year):
    results = []
    current = datetime(year, 1, 1).date()
    end = datetime(year, 12, 31).date()
    while current <= end:
        if is_amavasya(current):
            results.append({
                "date": current,
                "about": "Amavasya"
            })
        current += timedelta(days=1)
    return results
