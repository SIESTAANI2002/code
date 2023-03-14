FROM python:3.9.7-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev
RUN wget https://codeload.github.com/FFmpeg/FFmpeg/tar.gz/refs/tags/n6.0 -O ffmpeg.tar.gz \
    && tar -zxvf ffmpeg.tar.gz \
    && mv FFmpeg-n6.0 ffmpeg \
    && rm ffmpeg.tar.gz
RUN apt -qq install -y mediainfo
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
