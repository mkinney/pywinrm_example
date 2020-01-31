# Simple repo to use pywinrm to talk with Windows instance

Create/use python virtual environment:

    virtualenv -p python3 venv
    source venv/bin/activate

Install python libs:

    pip install pywinrm

Optionally, install direnv and run:

    direnv allow

Examples:

    ./simple.py 192.168.3.155
    ./run_ps_memory.py 192.168.3.155
    ./download_and_install_python.py 192.168.3.155
    ./install_pyinfra.py 192.168.3.155

If using Vagrant, see Vagrantfile in this directory.

If using Mech, see the Mechfile in this directory.

    pip install mech
    mech up

From Windows, ensure winrm is enabled:

    winrm get winrm/config

