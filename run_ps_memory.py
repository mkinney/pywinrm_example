#!/usr/bin/env python
import winrm

ps_script = """$strComputer = $Host
Clear
$RAM = WmiObject Win32_ComputerSystem
$MB = 1048576

"Installed Memory: " + [int]($RAM.TotalPhysicalMemory /$MB) + " MB" """

s = winrm.Session('192.168.2.246:5985', auth=('vagrant', 'vagrant'))
r = s.run_ps(ps_script)

print("status_code:{}".format(r.status_code))

print("output:\n", r.std_out.decode('utf-8'))
