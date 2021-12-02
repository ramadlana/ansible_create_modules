#!/usr/bin/python3

# Copyright: (c) 2021, Hidayah Ramadlana <hidayah.ramadalana@multipolar.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
This is module for HUAWEI vrp with command display ip routing-table
and only for public route-table
please locate this on
/usr/share/ansible/plugins/modules
'''

EXAMPLES = r'''
- name: TEST MULTIPOLAR MODULE
  hosts: metrodevice
  connection: local
  gather_facts: no

  tasks:
    - name: RUN CALL HUAWEI MODULE
      multipolar_module_huawei_display_ip_routing_table:
        command: 'display ip routing-table'
        ansible_host: '{{ hostvars[inventory_hostname].ansible_host }}'
        ansible_network_os: '{{ hostvars[inventory_hostname].ansible_network_os }}'
        ansible_user: '{{ hostvars[inventory_hostname].ansible_user }}'
        ansible_ssh_pass: '{{ hostvars[inventory_hostname].ansible_ssh_pass }}'
        ansible_platform: '{{ hostvars[inventory_hostname].ansible_platform }}'
      register: output

    - name: PRINT OUTPUT SUCCESS MODULE
      debug:
        msg: '{{ output }}'
'''

RETURN = r'''
"msg": {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/libexec/platform-python"
        },
        "changed": false,
        "failed": false,
        "return_from_devices": [
            {
                "cost": "65000",
                "destination": "1.1.1.1/32",
                "flag": "D",
                "interface": "Eth-Trunk4",
                "nexthop": "172.31.104.69",
                "pre": "10",
                "proto": "OSPF",
                "routetables": "Public"
            },
            {
                "cost": "0",
                "destination": "1.1.1.5/32",
                "flag": "D",
                "interface": "LoopBack0",
                "nexthop": "127.0.0.1",
                "pre": "0",
                "proto": "Direct",
                "routetables": "Public"
            },
    ----- OMITED ----------
'''

# all logic function


def run_module():
    # SOP:1 Change this: 
    # param input
    module_args = dict(
        command=dict(type='str', required=True),
        ansible_host=dict(type='str', required=False),
        ansible_network_os=dict(type='str', required=False),
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
        return net_connect.send_command(command)

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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ NTC TEMPLATE PARSER ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """ntc_templates.parse."""
    import os

    try:
        from textfsm import clitable

        HAS_CLITABLE = True
    except ImportError:
        HAS_CLITABLE = False

    def _get_template_dir():
        template_dir = os.environ.get("NTC_TEMPLATES_DIR")
        if template_dir is None:
            package_dir = os.path.dirname(__file__)
            template_dir = os.path.join(package_dir, "templates")
            if not os.path.isdir(template_dir):
                project_dir = os.path.dirname(os.path.dirname(os.path.dirname(template_dir)))
                template_dir = os.path.join(project_dir, "templates")

        return template_dir


    def _clitable_to_dict(cli_table):
        """Convert TextFSM cli_table object to list of dictionaries."""
        objs = []
        for row in cli_table:
            temp_dict = {}
            for index, element in enumerate(row):
                temp_dict[cli_table.header[index].lower()] = element
            objs.append(temp_dict)

        return objs


    def parse_output(platform=None, command=None, data=None):
        """Return the structured data based on the output from a network device."""

        if not HAS_CLITABLE:
            msg = """
    The TextFSM library is not currently supported on Windows. If you are NOT using Windows
    you should be able to 'pip install textfsm' to fix this issue. If you are using Windows
    then you will need to install the patch referenced here:

    https://github.com/google/textfsm/pull/82

    """
            raise ImportError(msg)

        template_dir = _get_template_dir()
        cli_table = clitable.CliTable("index", template_dir)

        attrs = {"Command": command, "Platform": platform}
        try:
            cli_table.ParseCmd(data, attrs)
            structured_data = _clitable_to_dict(cli_table)
        except clitable.CliTableError as e:
            raise Exception(
                'Unable to parse command "{0}" on platform {1} - {2}'.format(
                    command, platform, str(e)
                )
            )
            # Invalid or Missing template
            # module.fail_json(msg='parsing error', error=str(e))
            # rather than fail, fallback to return raw text
            # structured_data = [data]

        return structured_data

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ END OF TEMPLATE PARSER ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # NTC TEMPLATE LOCATION PLEASE CHANGE THIS TO UPDATED NTC TEMPLATES DIRECTORY
    os.environ["NTC_TEMPLATES_DIR"] = "/usr/share/ansible/plugins/modules/ntc-templates/ntc_templates/templates"


    parsed = parse_output(platform=module.params['ansible_platform'], command=module.params['command'], data=device_cli_output)

    # RESULT MODIFICATION
    result['return_from_devices'] = parsed

    # SOP: 3 END OF LOGIC FOR RETURN MESSAGE 
    
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