FROM python:3.6

EXPOSE 5000

WORKDIR /server

COPY requirements.txt /server
COPY templates/* /server/templates/
COPY server.py /server
COPY models.py /server

RUN pip install -r requirements.txt

CMD python server.py
