# -*- coding: utf-8 -*-
import urllib.request
import time
status=urllib.request.urlopen("http://10.0.8.127").code
if status == 200:
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),'web server is functional')
