from datetime import datetime, timedelta
from astronomy import get_tithi, get_sunrise, jd_to_datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")


def is_purnima(date):

    sunrise = get_sunrise(date)

    dt = jd_to_datetime(sunrise)

    tithi = get_tithi(dt)

    return tithi == 15


def next_purnima():

    today = datetime.now(IST).date()

    for i in range(40):

        d = today + timedelta(days=i)

        if is_purnima(d):

            return {
                "date": d,
                "days_until": (d - today).days,
                "about": "The Full Moon day, a time of peak energy and spiritual fruition."
            }

    return None


def purnima_year(year):

    results = []

    current = datetime(year, 1, 1).date()
    end = datetime(year, 12, 31).date()

    while current <= end:

        if is_purnima(current):

            results.append({
                "date": current,
                "about": "Purnima"
            })

        current += timedelta(days=1)

    return results