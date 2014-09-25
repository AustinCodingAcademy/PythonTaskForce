Python Task Force
===============

####pyVagrant VM box
https://s3.amazonaws.com/austincodingacademy/boxes/pyVagrant.box

####Amazon AWS CLI Configuration
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#config-settings-and-precedence

####VagrantFile
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "https://s3.amazonaws.com/austincodingacademy/boxes/pyVagrant.box"
  config.vm.network "private_network", ip: "10.10.10.33"
  config.vm.synced_folder "repos", "/home/vagrant/repos"
end
```

####VMs /etc/hosts entry
```
10.10.10.33 aca.local
```
