# Simple repo to use pywinrm to talk with Windows instance

Create/use python virtual environment:

    virtualenv venv
    source venv/bin/activate

Install python libs:

    pip install pywinrm

If using Vagrant, this Vagrantfile should work:

    Vagrant.configure("2") do |config|
      config.vm.box = "StefanScherer/windows_2019"
    end

If using Mech, this Mechfile should work:

    {
      "box": "StefanScherer/windows_2019",
      "box_version": "2019.11.15",
      "name": "windows2019",
      "url": "https://vagrantcloud.com/StefanScherer/boxes/windows_2019/versions/2019.11.15/providers/vmware_desktop.box"
    }

From Windows, ensure winrm is enabled:

    winrm get winrm/config

