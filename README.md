# 🌙 Sankashti & Purnima API

A public API that calculates **Sankashti Chaturthi** and **Purnima (Full Moon)** dates using astronomical calculations based on the **Hindu lunar calendar (Panchang)**.

This project uses **Sun–Moon angular mathematics (Tithi calculation)** to determine lunar events instead of hardcoding calendar dates.

The API provides endpoints to:

- Check if **today is Sankashti**
- Find the **next Sankashti**
- Get the **full Sankashti calendar for a year**
- Check if **today is Purnima**
- Find the **next Purnima**
- Generate the **full Purnima calendar for a year**

---

# 🔗 Live Links

### 🌐 Web Interface
https://sankashti-api.vercel.app/

### ⚙️ Public API
https://sankashti.onrender.com/

---

# ✨ Features

- 🌙 Accurate Sankashti calculation using **moonrise rule**
- 🌕 Purnima calculation using **sunrise tithi rule**
- 📅 Full year lunar event calendar
- 🔍 Check specific dates
- 🌍 Public REST API
- ⚡ Fast responses
- 📡 Ready for integration with apps, bots, and websites

---

# 🧠 How the Calculation Works

In the Hindu calendar, time is divided into **30 lunar days called Tithis**.

Each Tithi corresponds to **12° difference between Moon and Sun**.

```
Angle = (Moon Longitude − Sun Longitude) % 360
```

```
Tithi = int(angle / 12) + 1
```

---

## 🌙 Sankashti Chaturthi

Sankashti occurs when:

```
Tithi = 19
```

Which corresponds to:

```
Krishna Paksha Chaturthi
```

Unlike most festivals, Sankashti is determined by **Moonrise**.

Rule:

> If Chaturthi tithi is present at **moonrise**, that day is Sankashti.

---

## 🌕 Purnima

Purnima occurs when:

```
Tithi = 15
```

Which corresponds to the **Full Moon**.

Rule:

> If Purnima tithi is present at **sunrise**, that day is Purnima.

---

# 📡 API Endpoints

## Sankashti

### Check Today

```
GET /sankashti/today
```

Example:

```
https://sankashti.onrender.com/sankashti/today
```

Response:

```json
{
 "date": "2026-03-21",
 "is_sankashti": false
}
```

---

### Next Sankashti

```
GET /sankashti/next
```

Example:

```
https://sankashti.onrender.com/sankashti/next
```

Response:

```json
{
 "date": "2026-03-21",
 "days_until": 6
}
```

---

### Sankashti Calendar

```
GET /sankashti/year/{year}
```

Example:

```
https://sankashti.onrender.com/sankashti/year/2026
```

Response:

```json
{
 "year": 2026,
 "total": 12,
 "dates": [
  "2026-01-08",
  "2026-02-07",
  "2026-03-08"
 ]
}
```

---

### Check Specific Date

```
GET /sankashti/check/{date}
```

Example:

```
https://sankashti.onrender.com/sankashti/check/2026-03-21
```

Response:

```json
{
 "date": "2026-03-21",
 "is_sankashti": true
}
```

---

# 🌕 Purnima Endpoints

### Check Today

```
GET /purnima/today
```

Example:

```
https://sankashti.onrender.com/purnima/today
```

---

### Next Purnima

```
GET /purnima/next
```

Example:

```
https://sankashti.onrender.com/purnima/next
```

Response:

```json
{
 "date": "2026-04-02",
 "days_until": 18
}
```

---

### Purnima Calendar

```
GET /purnima/year/{year}
```

Example:

```
https://sankashti.onrender.com/purnima/year/2026
```

---

### Check Specific Date

```
GET /purnima/check/{date}
```

Example:

```
https://sankashti.onrender.com/purnima/check/2026-04-02
```

---

# 🧪 Interactive API Docs

FastAPI automatically generates interactive documentation:

```
https://sankashti.onrender.com/docs
```

You can test all endpoints directly in the browser.

---

# 🛠 Tech Stack

- Python
- FastAPI
- Swiss Ephemeris
- Pytz
- Render (API deployment)
- Vercel (frontend)

---

# 📂 Project Structure

```
moon-events-api
│
├── main.py
├── astronomy.py
├── sankashti.py
├── purnima.py
├── requirements.txt
└── README.md
```

---

# 🚀 Future Improvements

Possible upgrades:

- Ekadashi API integration
- Amavasya calculation
- Full Panchang engine
- Nakshatra calculations
- Multi-location moonrise support
- Hindu festival calendar API

---

# 👨‍💻 Author

Hari Prajwal

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository  
🔗 Share it with others  
🚀 Build something using the API

---

🌙 *Bringing traditional lunar calendars into modern software.*
