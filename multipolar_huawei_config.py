#!/usr/bin/python3

# Copyright: (c) 2021, Hidayah Ramadlana <hidayah.ramadalana@multipolar.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''

'''

EXAMPLES = r'''

'''

RETURN = r'''

'''

# all logic function



def run_module():
    # SOP:1 Change this: 
    # param input
    module_args = dict(
        command = dict(type='list', required=True),
        ansible_host = dict(type='str', required=False),
        ansible_network_os = dict(type='str', required=False),
        ansible_user=dict(type='str', required=False),
        ansible_ssh_pass=dict(type='str', required=False),
        ansible_platform=dict(type='str', required=False),
    )

    # SOP: 2 Change this
    # result prototype
    result = dict(
        changed=False,
        return_from_devices=""
    )

    # [do not change] create new AnsibleModule instance called (module)
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # [do not change] checkmode if true, only return the result immediately, all bellow code after this block cannot executed
    if module.check_mode:
        result['message_from_user'] = "this is check mode enable message"
        module.exit_json(**result)

    # SOP: 3 Change this
    # ALL LOGIC FOR RETURN MESSAGE IS DO IN HERE
    # change result value using module params or bussiness logic
    from netmiko import ConnectHandler

    def call_huawei(command,device_type, device_ip, device_username, device_password, device_port):
        # all platform or device_type can be see in here:
        # https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md

        huawei = {
        'device_type': device_type,
        'host':   device_ip,
        'username': device_username,
        'password': device_password,
        'port' : device_port
        }
        net_connect = ConnectHandler(**huawei)
        try:
            out = net_connect.send_config_set(command)
            net_connect.disconnect()
            result['changed'] = False
            return out
        except:
            result['changed'] = True
            return "configured"

    proposed_args = {
        'command': module.params['command'],
        'device_type': module.params['ansible_network_os'],
        'device_ip':   module.params['ansible_host'],
        'device_username': module.params['ansible_user'],
        'device_password': module.params['ansible_ssh_pass'],
        # hardcode port
        'device_port': 22
        }
    device_cli_output = call_huawei(**proposed_args)

    output = device_cli_output

    # SOP: 3 END OF LOGIC FOR RETURN MESSAGE 
    

    # RESULT MODIFICATION
    result['return_from_devices'] = output
    # [do not change] is Changed Logic
    # if its True, then changed will be true with yellow text
    # result['changed'] = True

    # [do not change] Fail Condition Logic
    if module.params['command'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # [do not change]in the event of a successful module execution
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()