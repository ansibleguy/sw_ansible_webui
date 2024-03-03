[![AnsibleGuy-WebUI Logo](https://raw.githubusercontent.com/ansibleguy/webui/latest/src/ansibleguy-webui/aw/static/img/logo.svg)](https://github.com/ansibleguy/webui)

# Ansible Role - AnsibleGuy-WebUI

Role to provision [a basic WebUI for using Ansible](https://github.com/ansibleguy/webui) on a linux server.

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
  * Ansible dependencies (_minimal_)


* **Configuration**
  * 


  * **Default config**:
    * 
 

  * **Default opt-ins**:
    * 


  * **Default opt-outs**:
    * 

## Info

* **Note:** this role currently only supports debian-based systems


* **Note:** Most of the role's functionality can be opted in or out.

  For all available options - see the default-config located in the main defaults-file!


* **Warning:** Not every setting/variable you provide will be checked for validity. Bad config might break the role!


## Usage

### Config

Define the config as needed:

```yaml
ansible-webui:

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
* 
*

To debug errors - you can set the 'debug' variable at runtime:
```bash
ansible-playbook -K -D -i inventory/hosts.yml playbook.yml -e debug=yes
```
