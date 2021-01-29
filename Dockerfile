FROM python:3.7-alpine

WORKDIR /app
COPY backend .
RUN pip install -r requirements.txt
#EXPOSE 8000
#CMD gunicorn -b :8000 django.wsgi

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]