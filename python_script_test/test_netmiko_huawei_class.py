from netmiko import ConnectHandler
huawei = {
    'device_type': 'huawei',
    'host':   "10.14.19.80",
    'username': 'huawei',
    'password': 'Huawei@123',
    'port' : 22
    }
net_connect = ConnectHandler(**huawei)

# net_connect.disconnect()
try:
    out = net_connect.send_config_set(["sysname PE-D1-RDC-TRANSIT-t2", "commit"])
    print(out)
except:
    print("exception triggered")