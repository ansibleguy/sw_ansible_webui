<a href="https://github.com/ansibleguy/webui">
  <img src="https://raw.githubusercontent.com/ansibleguy/webui/latest/src/ansibleguy-webui/aw/static/img/logo.svg" alt="AnsibleGuy-WebUI Logo" width="300"/>
</a>

# Ansible Role - Ansible-WebUI

Role to provision [a basic WebUI for using Ansible](https://github.com/ansibleguy/webui) on a linux server.

**DISCLAIMER**: This WebUI is an **unofficial community project**! Do not confuse it with the vanilla [Ansible](https://ansible.com/) product!

todo: REPLACE: GALAXY_ID

[![Molecule Test Status](https://badges.ansibleguy.net/sw_ansible_webui.molecule.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2)
[![YamlLint Test Status](https://badges.ansibleguy.net/sw_ansible_webui.yamllint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/yamllint.sh.j2)
[![PyLint Test Status](https://badges.ansibleguy.net/sw_ansible_webui.pylint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/pylint.sh.j2)
[![Ansible-Lint Test Status](https://badges.ansibleguy.net/sw_ansible_webui.ansiblelint.svg)](https://github.com/ansibleguy/_meta_cicd/blob/latest/templates/usr/local/bin/cicd/ansiblelint.sh.j2)
[![Ansible Galaxy](https://badges.ansibleguy.net/galaxy.badge.svg)](https://galaxy.ansible.com/ui/standalone/roles/ansibleguy/sw_ansible_webui)

Molecule Logs: [Short](https://badges.ansibleguy.net/log/molecule_sw_ansible_webui_test_short.log), [Full](https://badges.ansibleguy.net/log/molecule_sw_ansible_webui_test.log)

**Tested:**
* Debian 12

## Install

```bash
# latest
ansible-galaxy role install git+https://github.com/ansibleguy/sw_ansible_webui

# from galaxy
ansible-galaxy install ansibleguy.sw_ansible_webui

# or to custom role-path
ansible-galaxy install ansibleguy.sw_ansible_webui --roles-path ./roles

# install dependencies
ansible-galaxy install -r requirements.yml
```

## Functionality

* **Package installation**
  * Python3, Python3-PIP, Python3-Virtualenv, Git, Git-LFS
  * AnsibleGuy-WebUI with its Python3 Module-dependencies


* **Configuration**
  * Virtual-Environment used (`/home/ansible-webui/venv`)

  * **Default config**:
    * Cleanup logs older than 180 days
    * Backup retention 30 days

  * **Default opt-ins**:
    * Installing common Python3 modules (*'jmespath', 'netaddr', 'passlib', 'pywinrm', 'requests', 'cryptography'*)
    * Daily local backups
    * Auto-Upgrade App and Requirements on service-startup
    * Nginx proxy
    * Create service-user

## Info

* **Note:** this role currently only supports debian-based systems


* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in the main defaults-file!


* **Warning:** Not every setting/variable you provide will be checked for validity. Bad config might break the role!


## Usage

### Config

Define the config as needed:

Minimal config:

```yaml
semaphore:
  config:
    AW_HOSTNAMES: 'ansible.template.ansibleguy.net'
```

```yaml
ansible_webui:
  manage:
    webserver: true  # install and configure local nginx with min-ca cert
    backup: true  # install service for daily local database backup (if database is managed)
    user: true  # create service-user 'semaphore'
    ansible_cfg: true  # provision /home/ansible-webui/ansible.cfg

  requirements:  # requirements your execution-environment needs
    pip: ['httpx']  # any python3-modules
    collections: ['community.general']  # any ansible-collections (if persistent_requirements=true)
    roles: []  # any ansible-roles (if persistent_requirements=true)

  config:  # for options see: https://webui.ansibleguy.net/en/latest/usage/4_config.html#settings
    AW_HOSTNAMES: 'ansible.template.ansibleguy.net'
    # AW_SECRET: '...'  # minimum 30 characters; random one will be used if none was provided

  ansible_config:  # /home/ansible-webui/ansible.cfg => if manage.ansible_cfg=true; see: https://docs.ansible.com/ansible/latest/reference_appendices/config.html
    defaults:  # section
      remote_port: 48322
      vault_id_match: 'webui'
    diff:
      context: 2

  nginx:
    ...   # configure the webserver settings => see: https://github.com/ansibleguy/infra_nginx
```

You might want to use 'ansible-vault' to encrypt your passwords:
```bash
ansible-vault encrypt_string
```

### Execution

Run the playbook:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml
```

There are also some useful **tags** available:
* config

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```
