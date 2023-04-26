FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN apt-get update
RUN pip install --upgrade pip
RUN apt-get install wget -y -f
RUN apt-get install git -y
RUN add-apt-repository ppa:savoury1/ffmpeg4 -y
RUN apt full-upgrade

copy . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
