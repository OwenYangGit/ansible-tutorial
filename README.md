## Ansible testing project
- About control node test environment with docker on local
```
version: "3.9"
services:
  ansible:
    image: ubuntu:20.04
    # mapping develop folder to ansible container , you can setup any file location on own host
    volumes:
      - ./:/playbook
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
# Windows server managed node
[win]
10.1.21.119


[win:vars]
ansible_user=test
ansible_password=testpass
ansible_connection=winrm
ansible_winrm_transport=basic
ansible_winrm_server_cert_validation=ignore
ansible_port=5985

# Linux ubuntu 20.04 server LTS managed node
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

### 關於 gather_facts
這是 ansible 在調用 managed machine 時會取得遠端機器的一些資訊，該功能可以搭配 playbook 的條件式或一些客製化需求的時候使用 , 但需要再 playbook 裡面添加 gather_facts 的參數 , 而 ansible 提供 `setup` 模組來列出可以取得的遠端機器資訊
```
  - name: Play win
    hosts: win
    gather_facts: yes
    tasks:
      # - name: windows node ping pong
      #   win_ping:
      #   when: ansible_distribution == 'Ubuntu'
      - name: Check OS distributions
        ansible.builtin.setup:
          filter: ansible_distribution
        register: host_os
      - name: print handling result
        debug:
          msg: "{{ host_os }}"
```

### 在 dev ( Ubuntu 18.04 ) 上安裝調用 docker_stack module 所需的 package
```
sudo apt-get install python3-pip
pip3 install jsondiff
pip3 install PyYAML
```