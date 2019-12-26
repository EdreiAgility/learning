FROM python:3.7

EXPOSE 5008

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/config
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
# COPY config/mailconfig.cfg / usr/src/app/config/
# COPY config/dbconfig.cfg / usr/src/app/config/
# #COPY check.js /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]