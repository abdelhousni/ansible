Role Name
=========

Perform backup of IOS XE and Junos devices.

Requirements
------------

Ensure the cisco.ios and junipernetworks.junos collections are installed.

Role Variables
--------------

ansible_network_os must be defined.

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: net_backup }

License
-------

BSD

Author Information
------------------

Ricardo da Costa <rdacosta@redhat.com>
