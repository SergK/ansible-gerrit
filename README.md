Ansible Role: Gerrit
====================

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
    - { role: sergk.gerrit }
```

License
-------

MIT

Author Information
------------------

Sergiy Kulanov
