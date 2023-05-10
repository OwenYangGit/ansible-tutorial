## where to set variables
- Defining variables in a play
```
- hosts: webservers
  vars:
    http_port: 80
```

- Defining variables in included files and roles
```
---

- hosts: all
  remote_user: root
  vars:
    favcolor: blue
  vars_files:
    - /vars/external_vars.yml
  tasks:
  - name: This is just a placeholder
    ansible.builtin.command: /bin/echo foo
```