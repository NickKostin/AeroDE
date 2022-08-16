FROM python:3
ADD main.py /.
FROM puckel/docker-airflow:1.10.9
RUN pip install requests
RUN pip install psycopg2-binary
RUN pip install pathlib
RUN pip install python-dotenv




