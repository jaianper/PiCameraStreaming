import socket
import time
import picamera
import os

from datetime import datetime, date

DATE="{:%Y-%m-%d}".format(datetime.now())
FILENAME = "Raspvid_"+DATE+".h264"
RASPICAM_ON = "raspivid -n -w 640 -h 360 -b 4500000 -fps 24 -md 5 -vf -hf -t 3600000 -o "+FILENAME

os.system(RASPICAM_ON)
