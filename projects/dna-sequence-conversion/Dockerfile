FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m pytest tests
RUN python app.py 

ENTRYPOINT [ "bash" ]