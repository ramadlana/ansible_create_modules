def call_huawei(command,device_type, device_ip, device_username, device_password, device_port):
    # all platform or device_type can be see in here:
    # https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md

    huawei = {
    'command': command,
    'device_type': device_type,
    'host':   device_ip,
    'username': device_username,
    'password': device_password,
    'port' : device_port
    }

    return huawei

proposed_args= {
        'command': 'command',
        'device_type':'asasd',
        'device_ip':   'asas',
        'device_username': 'asas',
        'device_password': 'asas',
        # hardcode port
        'device_port': 22
    }
device_cli_output = call_huawei(**proposed_args)
print(device_cli_output)