FROM python:3.8
WORKDIR /smart_home
COPY ./smart_home /smart_home
RUN pip install -r /smart_home/requirements.txt
RUN python manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
