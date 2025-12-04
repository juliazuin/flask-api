FROM python:3.14.0-alpine3.22

EXPOSE 5000

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wsgi.py config.py application ./

CMD ["python", "wsgi.py"]
