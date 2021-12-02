#!/usr/bin/python3

# Copyright: (c) 2021, Hidayah Ramadlana <hidayah.ramadalana@multipolar.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: multipolar_module_test

short_description: This is my test module for multipolar module


version_added: "1.0.0"

description: -

options:
    word:
        description: This is the message to send to the test module.
        required: true
        type: str
    
    isChanged
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool

extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Hidayah Ramadlana (@ramadlana)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  multipolar_module_test:
    word: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  multipolar_module_test:
    name: hello world
     true

# fail the module
- name: Test failure of the module
  multipolar_module_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message_from_user:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # Defining params structure that can receive
    module_args = dict(
        isChanged=dict(type='bool', required=False, default=False),
        command=dict(type='str', required=True),
        ansible_host=dict(type='str', required=False),
        ansible_network_os=dict(type='str', required=False),
        ansible_user=dict(type='str', required=False),
        ansible_ssh_pass=dict(type='str', required=False),
    )

    # Defining result structure and fill default value
    result = dict(
        changed=False,
        command='',
        ansible_host='',
        ansible_network_os='',
        ansible_user='',
        ansible_ssh_pass='',
        check_mode_msg=''

    )

    # create new AnsibleModule instance called (module)
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # checkmode if true, only return the result immediately, all bellow code after this block cannot executed
    if module.check_mode:
        result['check_mode_msg'] = "this is check mode enable message"
        module.exit_json(**result)

    # ALL LOGIC FOR RETURN MESSAGE IS DO IN HERE
    result['command']=module.params['command']
    result['ansible_host'] = module.params['ansible_host']
    result['ansible_network_os'] = module.params['ansible_network_os']
    result['ansible_user'] = module.params['ansible_user']
    result['ansible_ssh_pass'] = module.params['ansible_ssh_pass']

    # is Changed Logic
    if module.params['isChanged']:
        result['changed'] = True

    # Fail Condition Logic
    if module.params['command'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()