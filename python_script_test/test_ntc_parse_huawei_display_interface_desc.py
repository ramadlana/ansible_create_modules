# This is for testing purposed
# 1. put unparsed data on unparsed variable
# 2. ctrl+p and search for vendorname_osname_show_test
# 3. edit the textfsm
# 4. run the test here

import os, json
from parse import parse_output

os.environ["NTC_TEMPLATES_DIR"] = "/opt/ntc-templates/ntc_templates/templates"

unparsed="""
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(E): E-Trunk down
(b): BFD down
(B): Bit-error-detection down
(e): ETHOAM down
(d): Dampening Suppressed
Interface                     PHY     Protocol Description            
Aux0/0/1                      down    down     HUAWEI, Aux0/0/1 Interface
Eth-Trunk0                    down    down     HUAWEI, Eth-Trunk0 Interface
Eth-Trunk1                    down    down     HUAWEI, Eth-Trunk1 Interface
Eth-Trunk4                    up      up       trunk_T-D1-RDC-Transit_TO_PE-D1-RDC-Transit
Eth-Trunk5                    down    down     trunk_T-D1-RDC-Transit to PE-VPN
Eth-Trunk6                    up      up       trunk_T-D1-RDC-Transit to BRAS02-D3-DDS
Eth-Trunk6.11                 up      up       SERVICE_BRASXT-D1-RDC-TRANSIT
Eth-Trunk6.12                 up      up       SERVICE_BRASXT-D1-RDC-TRANSIT
Eth-Trunk6.13                 up      up       SERVICE_BRASXT-D1-RDC-TRANSIT
Eth-Trunk6.14                 up      up       SERVICE_BRASXT-D1-RDC-TRANSIT
Eth-Trunk6.15                 up      up       SERVICE_BRASXT-D1-RDC-TRANSIT
Eth-Trunk6.100                up      down     l2VPN_BRAS_ANSIBLE
Eth-Trunk6.101                up      up       HUAWEI, Eth-Trunk6.101 Interface
GE0/0/0                       up      up       HUAWEI, GigabitEthernet0/0/0 Interface
GE1/0/0(10G)                  down    down     HUAWEI, GigabitEthernet1/0/0 Interface
GE1/1/0                       down    down     trunk_T-D1-RDC-Transit to PE-VPN
GE1/1/1                       down    down     HUAWEI, GigabitEthernet1/1/1 Interface
GE1/1/2                       up      up       T-D1-RDC-TRANSIT_BRAS
GE1/1/3                       up      up       Trunk_T-D1-RDC-Transit_TO_PE-D1-RDC-Transit
GE1/1/4                       down    down     HUAWEI, GigabitEthernet1/1/4 Interface
GE1/1/5                       up      down     HUAWEI, GigabitEthernet1/1/5 Interface
GE1/1/6                       down    down     HUAWEI, GigabitEthernet1/1/6 Interface
GE1/1/7                       down    down     HUAWEI, GigabitEthernet1/1/7 Interface
GE1/1/8                       down    down     HUAWEI, GigabitEthernet1/1/8 Interface
GE1/1/9                       down    down     HUAWEI, GigabitEthernet1/1/9 Interface
GE1/1/10                      down    down     HUAWEI, GigabitEthernet1/1/10 Interface
GE1/1/11                      down    down     HUAWEI, GigabitEthernet1/1/11 Interface
GE3/0/0                       down    down     HUAWEI, GigabitEthernet3/0/0 Interface
GE3/0/1                       down    down     HUAWEI, GigabitEthernet3/0/1 Interface
GE3/0/1.101                   down    down     HUAWEI, GigabitEthernet3/0/1.101 Interface
GE3/0/2                       down    down     HUAWEI, GigabitEthernet3/0/2 Interface
GE3/0/3                       down    down     HUAWEI, GigabitEthernet3/0/3 Interface
GE3/0/4                       down    down     HUAWEI, GigabitEthernet3/0/4 Interface
GE3/0/5                       down    down     HUAWEI, GigabitEthernet3/0/5 Interface
GE3/0/6                       down    down     HUAWEI, GigabitEthernet3/0/6 Interface
GE3/0/7                       down    down     HUAWEI, GigabitEthernet3/0/7 Interface
GE3/2/0                       down    down     HUAWEI, GigabitEthernet3/2/0 Interface
GE3/2/1                       down    down     HUAWEI, GigabitEthernet3/2/1 Interface
GE3/2/2                       down    down     HUAWEI, GigabitEthernet3/2/2 Interface
GE3/2/3                       down    down     HUAWEI, GigabitEthernet3/2/3 Interface
GE3/2/4                       down    down     HUAWEI, GigabitEthernet3/2/4 Interface
GE3/2/5                       down    down     HUAWEI, GigabitEthernet3/2/5 Interface
GE3/2/6                       down    down     HUAWEI, GigabitEthernet3/2/6 Interface
GE3/2/7                       down    down     HUAWEI, GigabitEthernet3/2/7 Interface
Log0                          up      up(s)    HUAWEI, Logic-Channel0 Interface
Loop0                         up      up(s)    HUAWEI, LoopBack0 Interface
NULL0                         up      up(s)    HUAWEI, NULL0 Interface
VT0                           up      up(s)    HUAWEI, Virtual-Template0 Interface
"""
parsed = parse_output(platform="vrp", command="display interface desc", data=unparsed)
print(json.dumps(parsed, indent=4))
