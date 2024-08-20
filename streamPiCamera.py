import socket
import time
import picamera
import os

IP_ADDRESS = "192.168.0.4" # IP del equipo donde se va a visualizar
#RASPICAM_ON = "raspivid -n -w 320 -h 240 -b 4500000 -fps 10 -vf -hf -t 0 -o - | tee video_001.h264 | gst-launch-1.0 -v fdsrc !  h264parse ! rtph264pay config-interval=10 pt=96 ! udpsink host="+IP_ADDRESS+" port=9000&"
RASPICAM_ON = "raspivid -n -w 320 -h 240 -b 4500000 -fps 10 -vf -hf -t 0 -o - | gst-launch-1.0 -e -v fdsrc !  h264parse ! rtph264pay config-interval=10 pt=96 ! udpsink host="+IP_ADDRESS+" port=9000&"

os.system(RASPICAM_ON)
