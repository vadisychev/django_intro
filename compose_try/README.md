To run application for the first time on your server please do:

1) run application by "docker-compose up" command;
2) execute "python3 manage.py migrate" on web-service (container) to create tables in Postgres DB.
3) DB will be stored on your server as named volume "postgres-test-db". So, you don't require any futher actions in the next app run. 
