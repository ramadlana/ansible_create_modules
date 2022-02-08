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
