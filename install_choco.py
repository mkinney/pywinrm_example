#!/usr/bin/env python
import sys
import winrm

def arg_check():
    if len(sys.argv) < 2:
        print('Warning: Need to provide ip for windows instance.')
        sys.exit(1)

install_choco = """
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
"""

def run_ps(ps, message):
    r = s.run_ps(ps)
    if r.status_code == 0:
        print('{} was a success'.format(message))


if __name__ == '__main__':
    arg_check()
    print("Going to install Chocolatey...")
    s = winrm.Session('{}:5985'.format(sys.argv[1]), auth=('vagrant', 'vagrant'))
    run_ps(install_choco, 'Install')

    # Note: If you connect to the instance using RDP/VNC, be sure to start powershell as admin
    # otherwise the 'choco' command is not available.
    r = s.run_ps("choco --version")
    if r.status_code == 0:
        print("Ran choco successfully.")
        print("output:\n", r.std_out.decode('utf-8'))

    # example of a choco installation
    run_ps('choco install -y notepadplusplus', 'Install Notepad++')


