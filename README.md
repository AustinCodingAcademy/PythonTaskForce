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
```bash
$ vagrant up
```
SSH into VM
```bash
$ vagrant ssh
```
Stop the VM
```bash
$ vagrant halt
```

### Git commands
View the status of your staging area
```
$ git status
```
Add one file to staging area
```
$ git add myfile.py.py
```
Add multiple files to staging area
```
$ git add .
```
Commit all staged files
```
$ git commit
```
Commit all modified unstaged files
```
$ git commit -a
```
View all remote branches
```
$ git branch -r
```
Get all remote branches
```
$ git pull
```
Checkout an existing remote branch
```
$ git checkout githubBranch
```
Create a new local branch
```
$ git checkout -b myNewLocalbranch
```
Push a newly created local branch to remote
```
$ git push -u origin myNewLocalBranch
```
Push to remote when local branch and remote branch exist and have the same name
```
$ git push
```
Incorporate all changes that are in the remote tracking branch into your local branch
```
$ git pull
```
View history of all commits
```
$ git log
```
Reset your working directory to a pristine state (Note this will wipe out any changes you made)
```
$ git reset HEAD --hard
```
