FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /nmmotors
COPY requirements.txt /nmmotors/requirements.txt
RUN pip install -r requirements.txt
COPY . /nmmotors
CMD python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000