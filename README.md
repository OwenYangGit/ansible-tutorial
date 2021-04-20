## Ansible testing project
- About control node test environment with docker on local
```
version: "3.9"
services:
  ansible:
    image: ubuntu:20.04
    stdin_open: true
    tty: true
    container_name: ansible
```

### ansible control node container installation
```shell=
docker-compose up -d
docker exec -it ansible bash
apt-get update
apt-get install ansible
```
### Base OS
- windows server 2016 std

### winrm setting
```shell=
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
```
### ansible test windows ping
```
ansible -i inventory win -m win_ping
```

### Put inventory file list managed machine following example
```
[win]
10.1.21.119


[win:vars]
ansible_user=test
ansible_password=testpass
ansible_connection=winrm
ansible_winrm_transport=basic
ansible_winrm_server_cert_validation=ignore
ansible_port=5985

[dev]
10.1.1.41

[dev:vars]
ansible_ssh_user=test
#ansible_ssh_private_key_file=~/.ssh/id_rsa
```

### For windows ping pong playbook example
```yaml=
---
- hosts: win
  tasks:
    # task 1
    - name: test connection
      win_ping:
      register: message

    # task 2
    - name: print debug message
      debug:
        msg: "{{ message }}"
```