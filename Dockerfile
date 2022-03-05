FROM python:3.8

ENV PYTHONUNBUFFERED 1
# RUN apt update -y && apt install -y cron

COPY  ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./ /app

# RUN useradd -m rpzuser 

# RUN mkdir -p /var/log/rupyz
# RUN chown rpzuser /var/log/rupyz

# RUN touch /var/log/rupyz/info.log
# RUN chown rpzuser /var/log/rupyz/info.log

# USER rpzuser
