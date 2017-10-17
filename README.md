Ansible Role: Gerrit
====================

[![Build Status](https://api.travis-ci.org/SergK/ansible-gerrit.svg?branch=master)](https://travis-ci.org/SergK/ansible-gerrit)

Setup Gerrit Service on Debian

Requirements
------------

None.

Role Variables
--------------

All variables defined in `default/main.yml` and `vars/main.yml`

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: gerrit
  roles:
    - { role: SergK.gerrit }
```

License
-------

MIT

Author Information
------------------

Sergiy Kulanov
