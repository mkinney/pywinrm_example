# Simple repo to use pywinrm to talk with Windows instance

Create/use python virtual environment:

    virtualenv venv
    source venv/bin/activate

Install python libs:

    pip install pywinrm

If using Vagrant, see Vagrantfile in this directory.

If using Mech, see the Mechfile in this directory.

From Windows, ensure winrm is enabled:

    winrm get winrm/config

