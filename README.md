Python Task Force
===============

####pyVagrant VM box
https://s3.amazonaws.com/austincodingacademy/boxes/pyVagrant.box

####Amazon AWS CLI Configutation
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#config-settings-and-precedence

####VagrantFile
```
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "https://s3.amazonaws.com/austincodingacademy/boxes/pyVagrant.box"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder "shared_data", "/home/vagrant/shared_data"
end
```
