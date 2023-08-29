# devops-plataform-poc

DevOps Platform via Gitlab CI/CD

---
App downloads periodically daily reports from covid set on `poc/poc/settings`:
```
IMPORT_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
START_DATE = '01-22-2020'
```
and compiles the reports by country exposing on `http://localhost:8000/covid_data` which is updated periodically:
- `http://localhost:8000/covid_data/all` - shows a table of the reports of all countries
- `http://localhost:8000/covid_data/{country}` - shows a table of the reports of a given country
    - `http://localhost:8000/covid_data/Nauru` - show a table of all the reports collected from Nauru

---

Uses:
- Docker
- Gitlab CI/CD
- Python 3 
- Django
- Pandas
- MongoDB
---
The dockerized version can be run on the terminal using:
- docker build -t poc Dockerfile .
- docker run -e PYTHONUNBUFFERED=1 -p 8000:8000 poc
