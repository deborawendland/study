FROM python:3

WORKDIR /usr/src/app

COPY poc/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python poc/manage.py makemigrations covid_data
RUN python poc/manage.py migrate

CMD [ "python", "poc/manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000