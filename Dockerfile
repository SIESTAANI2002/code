FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get install wget -y -f
RUN apt install -y ffmpeg

copy . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
