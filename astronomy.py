import swisseph as swe
from datetime import datetime, timedelta
import pytz

IST = pytz.timezone("Asia/Kolkata")

LAT = 12.9716
LON = 77.5946


def jd_to_datetime(jd):
    """Convert Julian Day to IST datetime."""
    utc_dt = datetime(1970, 1, 1, tzinfo=pytz.UTC) + timedelta(seconds=(jd - 2440587.5) * 86400)
    return utc_dt.astimezone(IST)


def get_tithi(dt):

    utc = dt.astimezone(pytz.UTC)

    jd = swe.julday(
        utc.year,
        utc.month,
        utc.day,
        utc.hour + utc.minute / 60
    )

    sun = swe.calc_ut(jd, swe.SUN)[0][0]
    moon = swe.calc_ut(jd, swe.MOON)[0][0]

    angle = (moon - sun) % 360

    return int(angle / 12) + 1


def get_sunrise(date):

    jd = swe.julday(date.year, date.month, date.day, 0)

    rs = swe.rise_trans(
        jd,
        swe.SUN,
        rsmi=swe.CALC_RISE,
        geopos=(LON, LAT, 0.0)
    )

    return rs[1][0]


def get_moonrise(date):

    jd = swe.julday(date.year, date.month, date.day, 0)

    rs = swe.rise_trans(
        jd,
        swe.MOON,
        rsmi=swe.CALC_RISE,
        geopos=(LON, LAT, 0.0)
    )

    return rs[1][0]