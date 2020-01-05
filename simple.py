#!/usr/bin/env python
import winrm

s = winrm.Session('192.168.2.246:5985', auth=('vagrant', 'vagrant'))
r = s.run_cmd('ipconfig', ['/all'])

print("status_code:{}".format(r.status_code))

print("output:\n", r.std_out.decode('utf-8'))
