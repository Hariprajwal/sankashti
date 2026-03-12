from datetime import datetime, timedelta
from astronomy import get_tithi, get_moonrise, jd_to_datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")


def is_sankashti(date):

    moonrise = get_moonrise(date)

    dt = jd_to_datetime(moonrise)

    tithi = get_tithi(dt)

    return tithi == 19


def next_sankashti():

    today = datetime.now(IST).date()

    for i in range(40):

        d = today + timedelta(days=i)

        if is_sankashti(d):

            return {
                "date": d,
                "days_until": (d - today).days,
                "about": "Sankashti Chaturthi is a holy day dedicated to Lord Ganesha, observed on the fourth day after the full moon."
            }

    return None


def sankashti_year(year):

    results = []

    current = datetime(year,1,1).date()
    end = datetime(year,12,31).date()

    while current <= end:

        if is_sankashti(current):

            results.append({
                "date": current,
                "about": "Sankashti Chaturthi"
            })

        current += timedelta(days=1)

    return results