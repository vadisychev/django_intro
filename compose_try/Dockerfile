FROM python:3
# RUN apt-get update && apt-get upgrade
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
# RUN python3 manage.py migrate
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
