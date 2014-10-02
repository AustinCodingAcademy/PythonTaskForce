Python Task Force
===============

#### Pre-install these applications
* Database Access
  * MySQL Workbench 6.1 - http://www.mysql.com/products/workbench/
  * Sequel Pro (OSX Only) - http://www.sequelpro.com/download
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
```bash
$ git status
```
Add one file to staging area
```bash
$ git add myfile.py.py
```
Add multiple files to staging area
```bash
$ git add .
```
Commit all staged files
```bash
$ git commit
```
Commit all modified unstaged files
```bash
$ git commit -a
```
View all remote branches
```bash
$ git branch -r
```
Get all remote branches
```bash
$ git pull
```
Checkout an existing remote branch
```bash
$ git checkout githubBranch
```
Create a new local branch
```bash
$ git checkout -b myNewLocalbranch
```
Push a newly created local branch to remote
```bash
$ git push -u origin myNewLocalBranch
```
Push to remote when local branch and remote branch exist and have the same name
```bash
$ git push
```
Incorporate all changes that are in the remote tracking branch into your local branch
```bash
$ git pull
```
View history of all commits
```bash
$ git log
```
Reset your working directory to a pristine state (Note this will wipe out any changes you made)
```bash
$ git reset HEAD --hard
```
