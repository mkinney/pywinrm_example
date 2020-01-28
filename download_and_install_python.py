#!/usr/bin/env python
import sys
import winrm

# Powershell to download a file
python_version = "3.7.6"
download_script = """
$url = "https://www.python.org/ftp/python/{0}/python-{0}-amd64.exe"
$output = "$home\Downloads\python-{0}-amd64.exe"

Invoke-WebRequest -Uri $url -OutFile $output
""".format(python_version)

install_script = """
Start-Process -FilePath $home\Downloads\python-{0}-amd64.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -NoNewWindow -Wait
""".format(python_version)

def arg_check():
    if len(sys.argv) < 2:
        print('Warning: Need to provide ip for windows instance.')
        sys.exit(1)

if __name__ == '__main__':
    arg_check()
    print("Going to download, install, and verify python version:{}".format(python_version))
    s = winrm.Session('{}:5985'.format(sys.argv[1]), auth=('vagrant', 'vagrant'))
    r = s.run_ps(download_script)
    #print("status_code:{}".format(r.status_code))
    #print("output:\n", r.std_out.decode('utf-8'))
    #print("stderr:\n", r.std_err.decode('utf-8'))

    if r.status_code == 0:
        print("Downloaded successfully.")

    # see if we can silently install it 
    r = s.run_ps(install_script)
    #print("status_code:{}".format(r.status_code))
    #print("output:\n", r.std_out.decode('utf-8'))
    #print("err:\n", r.std_err.decode('utf-8'))
    if r.status_code == 0:
        print("Install successfully.")

    r = s.run_ps("python --version")
    if r.status_code == 0:
        print("Ran python successfully.")
        print("output:\n", r.std_out.decode('utf-8'))

