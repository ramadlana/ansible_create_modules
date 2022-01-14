from netmiko import ConnectHandler

def call_huawei(command,command2, device_type, device_ip, device_username, device_password, device_port):
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
    net_connect.send_command_timing(command_string="enable")
    net_connect.send_command_timing(command_string="config")
    output = net_connect.send_command_timing(
    command_string=command,
    strip_prompt=False,
    strip_command=False
    )
    if "Are you sure to release service virtual port(s)?" in output:
        output += net_connect.send_command_timing(
            command_string="y\n",
            strip_prompt=False,
            strip_command=False
        )
    net_connect.send_command_timing(command_string=command2)
    net_connect.disconnect()
    return output

proposed_args = {
        # 'command': module.params['command'],
        'command': "undo service-port 61",
        'command2': "service-port vlan 3001 gpon  0/2/0 ont 5 gemport 2 multi-service user-vlan 200 tag-transform translate inbound traffic-table index 163 outbound traffic-table index 250",
        'device_type': 'huawei_olt',
        'device_ip': '10.14.19.26',
        'device_username': 'huawei',
        'device_password': 'huawei123',
        # hardcode port
        'device_port': 22
    }
device_cli_output = call_huawei(**proposed_args)

output = device_cli_output
print(output)