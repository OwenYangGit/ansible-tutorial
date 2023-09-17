## extra-vars
- `'p_name=demo'`
- `'plugin="mysql,redis"'`

### ansible-playbook command for deploy service example
```
# without any plugin
ansible-playbook -i inventories/dev/ service_deploy.playbook.yml -e 'p_name=demo'

# with plugin mysql and redis
ansible-playbook -i inventories/dev/ service_deploy.playbook.yml -e 'p_name=demo' -e 'plugin="mysql,redis"'

# with plugin only redis
ansible-playbook -i inventories/dev/ service_deploy.playbook.yml -e 'p_name=demo' -e 'plugin="redis"'
```