FROM alang/django
# RUN apt-get update && apt-get upgrade
RUN pip install django-crispy-forms
COPY /forms /usr/django/app/forms
COPY manage.py /usr/django/app
COPY /mysite /usr/django/app/mysite
RUN python3 /usr/django/app/manage.py migrate
CMD ["python3", "app/manage.py", "runserver", "0.0.0.0:8000"]

