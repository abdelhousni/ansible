# -*- coding: utf-8 -*-

# Authors:
#   Thomas Woerner <twoerner@redhat.com>
#
# Based on ipa-server-install code
#
# Copyright (C) 2017-2022  Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'supported_by': 'community',
    'status': ['preview'],
}

DOCUMENTATION = '''
---
module: ipaserver_master_password
short_description: Generate kerberos master password if not given
description:
  Generate kerberos master password if not given
options:
  dm_password:
    description: Directory Manager password
    type: str
    required: yes
  master_password:
    description: kerberos master password (normally autogenerated)
    type: str
    required: no
author:
    - Thomas Woerner (@t-woerner)
'''

EXAMPLES = '''
'''

RETURN = '''
password:
  description: The master password
  type: str
  returned: always
'''

import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.ansible_ipa_server import (
    check_imports,
    setup_logging, options, paths, read_cache, ipa_generate_password
)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            # basic
            dm_password=dict(required=True, type='str', no_log=True),
            master_password=dict(required=False, type='str', no_log=True),
        ),
        supports_check_mode=False,
    )

    module._ansible_debug = True
    check_imports(module)
    setup_logging()

    options.dm_password = module.params.get('dm_password')
    options.master_password = module.params.get('master_password')

    # This will override any settings passed in on the cmdline
    if os.path.isfile(paths.ROOT_IPA_CACHE):
        # dm_password check removed, checked already
        try:
            cache_vars = read_cache(options.dm_password)
            options.__dict__.update(cache_vars)
        except Exception as e:
            module.fail_json(msg="Cannot process the cache file: %s" % str(e))

    if not options.master_password:
        options.master_password = ipa_generate_password()

    module.exit_json(changed=True,
                     password=options.master_password)


if __name__ == '__main__':
    main()
