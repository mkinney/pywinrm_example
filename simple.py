#!/usr/bin/env python
import sys
import winrm

def arg_check():
    if len(sys.argv) < 2:
        print('Warning: Need to provide ip for windows instance.')
        sys.exit(1)

if __name__ == '__main__':
    arg_check()
    s = winrm.Session('{}:5985'.format(sys.argv[1]), auth=('vagrant', 'vagrant'))
    r = s.run_cmd('ipconfig', ['/all'])

    print("status_code:{}".format(r.status_code))

    print("output:\n", r.std_out.decode('utf-8'))
