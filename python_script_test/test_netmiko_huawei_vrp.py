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
    out = net_connect.send_config_set(command)
    net_connect.disconnect()
    return out

proposed_args = {
        # 'command': ["system-view", "interface GigabitEthernet3/0/1.101", "vlan-type dot1q 101", "mpls l2vc 1.1.1.5 101", "statistic enable"],
        'command': ["sysname PE-D1-RDC-TRANSIT3", "interface LoopBack 190"],
        'device_type': 'huawei',
        'device_ip':   '10.14.19.80',
        'device_username': 'huawei',
        'device_password': 'Huawei@123',
        'device_port': 22
    }
device_cli_output = call_huawei(**proposed_args)

output = device_cli_output
print(output)