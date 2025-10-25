<a href="https://github.com/O-X-L/ansible-webui">
  <img src="https://raw.githubusercontent.com/O-X-L/ansible-webui/latest/src/oxl-ansible-webui/aw/static/img/logo.svg" alt="AnsibleGuy-WebUI Logo" width="300"/>
</a>

# Ansible Role - Ansible-WebUI

Role to provision [a basic WebUI for using Ansible](https://github.com/O-X-L/ansible-webui) on a linux server.

**DISCLAIMER**: This WebUI is an **unofficial community project**! Do not confuse it with the vanilla [Ansible](https://ansible.com/) product!

[![Lint](https://github.com/O-X-L/ansible-role-ansible-webui/actions/workflows/lint.yml/badge.svg)](https://github.com/O-X-L/ansible-role-ansible-webui/actions/workflows/lint.yml)
[![Ansible Galaxy](https://badges.oss.oxl.app/galaxy.badge.svg)](https://galaxy.ansible.com/ui/standalone/roles/oxlorg/ansible_webui)

**Molecule Integration-Tests**:

* Status: [![Molecule Test Status](https://badges.oss.oxl.app/sw_ansible_webui.molecule.svg)](https://github.com/O-X-L/ansible-role-oxl-cicd/blob/latest/templates/usr/local/bin/cicd/molecule.sh.j2) |
[![Functional-Tests](https://github.com/O-X-L/ansible-role-ansible-webui/actions/workflows/integration_test_result.yml/badge.svg)](https://github.com/O-X-L/ansible-role-ansible-webui/actions/workflows/integration_test_result.yml)
* Logs: [API](https://ci.oss.oxl.app/api/job/ansible-test-molecule-sw_ansible_webui/logs?token=2b7bba30-9a37-4b57-be8a-99e23016ce70&lines=1000) | [Short](https://badges.oss.oxl.app/log/molecule_sw_ansible_webui_test_short.log) | [Full](https://badges.oss.oxl.app/log/molecule_sw_ansible_webui_test.log)

Internal CI: [Tester Role](https://github.com/O-X-L/ansible-role-oxl-cicd) | [Jobs API](https://github.com/O-X-L/github-self-hosted-jobs-systemd)

**Tested:**
* Debian 12

----

## Install

```bash
# latest
ansible-galaxy role install git+https://github.com/O-X-L/ansible-role-ansible-webui

# from galaxy
ansible-galaxy install oxlorg.ansible_webui

# or to custom role-path
ansible-galaxy install oxlorg.ansible_webui --roles-path ./roles

# install dependencies
ansible-galaxy install -r requirements.yml
```

----

## Advertisement

* Need **professional support** using Ansible? Contact us:

  E-Mail: [contact@oxl.at](mailto:contact@oxl.at)

  Tel: [+43 3115 40 900 0](tel:+433115409000)

  Web: [EN](https://www.o-x-l.com) | [DE](https://www.oxl.at)

  Language: German or English

----

## Usage

### Config

Define the config as needed:

Minimal config:

```yaml
ansible_webui:
  config:
    AW_HOSTNAMES: 'ansible.template.oxl.at'
```

Options:

```yaml
ansible_webui:
  manage:
    webserver: true  # install and configure local nginx with min-ca cert
    backup: true  # install service for daily local database backup (if database is managed)
    user: true  # create service-user 'ansible-webui'
    ansible_cfg: true  # provision /home/ansible-webui/ansible.cfg

  requirements:  # requirements your execution-environment needs
    pip: ['httpx']  # any python3-modules
    collections: ['community.general']  # any ansible-collections (if persistent_requirements=true)
    roles: []  # any ansible-roles (if persistent_requirements=true)

  config:  # for options see: https://webui.oxl.at/en/latest/usage/4_config.html#settings
    AW_HOSTNAMES: 'ansible.template.oxl.at'
    # AW_SECRET: '...'  # minimum 30 characters; random one will be used if none was provided

  ansible_config:  # /home/ansible-webui/ansible.cfg => if manage.ansible_cfg=true; see: https://docs.ansible.com/ansible/latest/reference_appendices/config.html
    defaults:  # section
      remote_port: 48322
      vault_id_match: 'webui'
    diff:
      context: 2

  nginx:
    ...   # configure the webserver settings => see: https://github.com/O-X-L/ansible-role-nginx
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
* webserver

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```

----

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

  For all available options - see the default-config located in [the main defaults-file](https://github.com/O-X-L/ansible-role-ansible-webui/blob/latest/defaults/main/1_main.yml)!


* **Warning:** Not every setting/variable you provide will be checked for validity. Bad config might break the role!
