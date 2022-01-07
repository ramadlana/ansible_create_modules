 # all platform or device_type can be see in here:
    # https://github.com/ktbyers/netmiko/blob/develop/PLATFORMS.md
from netmiko import ConnectHandler

perangkat = {
    'device_type': 'huawei',
    'host':   '10.14.19.80',
    'username': 'huawei',
    'password': 'Huawei@123',
    'port' : 22
}
net_connect = ConnectHandler(**perangkat)
out = net_connect.send_command("display ver")
net_connect.disconnect()
print(out)

# proposed_args = {
#         # 'command': ["system-view", "interface GigabitEthernet3/0/1.101", "vlan-type dot1q 101", "mpls l2vc 1.1.1.5 101", "statistic enable"],
#         'command': ["sysname PE-D1-RDC-TRANSIT3", "interface LoopBack 190"],
#         'device_type': 'huawei',
#         'device_ip':   '10.14.19.80',
#         'device_username': 'huawei',
#         'device_password': 'Huawei@123',
#         'device_port': 22
#     }
# device_cli_output = call_huawei(**proposed_args)

# output = device_cli_output
# print(output)