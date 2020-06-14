#!/bin/sh
#spawn-fcgi -d /home/develop/python/weather -f /home/develop/python/weather/main.py -a 127.0.0.1 -p 9002
#uwsgi -s 127.0.0.1:9002 -w main.py
uwsgi -s:9002 -w index -p 2 -d uws.error &