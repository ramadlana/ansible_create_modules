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
    net_connect.send_command_timing(command_string="enable")
    output = net_connect.send_command_timing(
    command_string=command,
    strip_prompt=False,
    strip_command=False
    )
    if "<cr>" in output:
        output += net_connect.send_command_timing(
            command_string="\n",
            strip_prompt=False,
            strip_command=False
        )

    net_connect.disconnect()
    return output

proposed_args = {
        # 'command': module.params['command'],
        'command': "display vlan  desc 1-4093 | no-more",
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