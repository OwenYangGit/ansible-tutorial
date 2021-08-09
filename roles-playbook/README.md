## Quick deploy new environment with swarm

## About roles-playbook 

### Prepare inventory file , for example
[AP1]
192.168.1.1 ansible_become_password="pwd"

[AP1:vars]
ansible_ssh_user=example
ansible_ssh_private_key_file=priv-key

[AP2]
192.168.1.2 ansible_become_password="pwd"

[AP2:vars]
ansible_ssh_user=example
ansible_ssh_private_key_file=priv-key


### group_vars on top level
```
group_vars/
    all
```
#### all for setting variables , for example
```
AP1_LIST: ["service1","service2","service3"]
AP2_LIST: ["service4","service5"]
AP1_HOSTNAME: "AP1"
AP2_HOSTNAME: "AP2"
REG_ENDPOINT: "IP:5000"
REG_USER: "test"
REG_PASS: "example"
SWARM_OVERLAY_NETWORK: "example-overlay"
SWARM_OVERLAY_NETWORK_CIDR: "192.168.1.0/24"
```

### common
```
files/
    daemon.json # for setting docker daemon configuration
vars/
    main.yml # Whatever you want to install packages list
```

#### daemon.json , for example
```
{
    "insecure-registries" : ["PRIV_IP_ADDR:PORT"]
}
```