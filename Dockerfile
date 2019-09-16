FROM python:3.6-alpine

LABEL maintainer='https://github.com/deanshanahan'

RUN apk update && \ 
    apk add --no-cache portaudio portaudio-dev py3-numpy muslc gcc alsa-utils alsa-utils-doc alsa-lib alsacon

ENV PYTHONPATH=/usr/lib/python3.7/site-packages

COPY . /home

WORKDIR /home

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["start.py"]
