FROM python:3.10.4

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "python", "main.py" ]