Python Task Force
===============

#### Pre-install these applications
* Database Access - MySQL Workbench 6.1 - http://www.mysql.com/products/workbench/
* Developer Virtualization - VirtualBox - https://www.virtualbox.org/wiki/Downloads
* Quick VM Setup - Vagrant - https://www.vagrantup.com/downloads.html
* IDE - PyCharm CE - http://www.jetbrains.com/pycharm/download/
* git GUI Client - SourceTree - http://www.sourcetreeapp.com/

#### VagrantFile
```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "https://s3.amazonaws.com/austincodingacademy/boxes/pyVagrant.box"
  config.vm.network "private_network", ip: "10.10.10.33"
  config.vm.synced_folder "repos", "/home/vagrant/repos"
end
```

#### VMs /etc/hosts entry
```
10.10.10.33 aca.local
```
#### MySQL Credentials (Local to VM)
* host: localhost
* username: root
* password: something
* database: acadb
```bash
$ mysql -u root -p -h localhost
Enter Password: something
```

#### Vagrant Commands
Boot up VM
```
vagrant up
```
SSH into VM
```
vagrant ssh
```
Stop the VM
```
vagrant halt
```
