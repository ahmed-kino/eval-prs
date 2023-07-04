FROM python:3.9.16

RUN apt update
RUN apt install make

WORKDIR /app

ADD  . .
RUN pip install -r requirements.txt
CMD ["make", "run"]