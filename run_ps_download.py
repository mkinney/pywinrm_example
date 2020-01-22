#!/usr/bin/env python
import winrm

import winrm

ps_script = """
$url = "https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe"
$output = "$home\Downloads\python-3.7.6-amd64.exe"

Invoke-WebRequest -Uri $url -OutFile $output

"""

s = winrm.Session('192.168.2.246:5985', auth=('vagrant', 'vagrant'))
r = s.run_ps(ps_script)

print("status_code:{}".format(r.status_code))

print("output:\n", r.std_out.decode('utf-8'))
