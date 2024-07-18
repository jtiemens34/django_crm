FROM python:3.5
ENV PYTHONBUFFERED 1
COPY requirements.txt ./
RUN pip install -r requirements.txt
VOLUME /usr/src
COPY . .
EXPOSE 8000
CMD ["python", "django_crm/manage.py", "runserver"]