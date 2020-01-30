#!/usr/bin/env python
import sys
import winrm

# Note: Requires python to be installed first
def arg_check():
    if len(sys.argv) < 2:
        print('Warning: Need to provide ip for windows instance.')
        sys.exit(1)

install_pyinfra = """
Set-ExecutionPolicy Unrestricted
Set-Location $HOME
. .\venv\Scripts\activate.ps1
pip install pyinfra
"""

def run_ps(ps, message):
    r = s.run_ps(ps)
    if r.status_code == 0:
        print('{} was a success'.format(message))

def run_ps_with_output(ps):
    r = s.run_ps(ps)
    if r.status_code == 0:
        print('Success. {}'.format(r.std_out.decode('utf-8')))
    else:
        print('ERR. {}'.format(r.std_err.decode('utf-8')))


if __name__ == '__main__':
    arg_check()
    print("Going to install pyinfra...")
    s = winrm.Session('{}:5985'.format(sys.argv[1]), auth=('vagrant', 'vagrant'))
    run_ps('pip install virtualenv', 'Install virtualenv')
    run_ps('python -m pip install --upgrade pip', 'Upgrade pip')
    run_ps('if ( -not (Test-Path "$HOME\\venv" -PathType Any )) { virtualenv.exe venv }',
           'Create python virtual environment (if we need to)')
    run_ps(install_pyinfra, 'Install pyinfra')
    run_ps_with_output('Set-Location $HOME ; . .\venv\Scripts\activate.ps1 ; pyinfra --version')
