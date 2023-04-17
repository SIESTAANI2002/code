#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=15681388, cast=int)
    API_HASH = config("API_HASH", default="446b56944f74f6b7688175d48cdfa881")
    BOT_TOKEN = "6249960795:AAHBC233MxzMDnrtTiBP8FcmfltympbBpiE"
    DEV = 5074446156
    OWNER = config("OWNER", default="5074446156")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -map 0:v? -map 0:a? -map 0:s? -c:v libx265 -pix_fmt yuv420p10le -preset slow -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -vf scale=1280:720,"drawtext=fontfile=/content/drive/MyDrive/Font/A.ttf:text=Encoded By @Ani_Animesh:x=1040:y=650:fontsize=10:fontcolor=white:enable=between(t\,200\,440)" -x265-params me=3:rd=4:subme=3:aq-mode=3:aq-strength=1:deblock=1,1:psy-rd=1.20:psy-rdoq=1:merange=57:bframes=4:b-adapt=2:frame-threads=3:no-info=1 -crf 23 -c:a aac -b:a 112k -c:s copy -metadata title="Presented By Ani Animesh | Anime Sakura" -metadata author="AnimeSakura.co" -metadata copyright="Copyright 2023 Me" -metadata encoded_by="Lolikiller #Sakura_Gang" -metadata:s:0 title="Episode Unknown xD" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="AnimeSakura.co" -metadata:s:s:0 title="AnimeSakura.co" -metadata:s:s:1 title="@Ani_Animesh" "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/a615291ef3f9f361e9b12.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
