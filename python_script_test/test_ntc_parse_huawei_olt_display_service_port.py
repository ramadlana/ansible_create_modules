import os, json
from parse import parse_output

os.environ["NTC_TEMPLATES_DIR"] = "/opt/ntc-templates/ntc_templates/templates"

unparsed="""
XGSPON-D3-DDS_LAB#display service-port vlan 2250    
{ <cr>|e2e<K>|inner-vlan<K>|sort-by<K>||<K> }: 

  Command:
          display service-port vlan 2250
  Switch-Oriented Flow List
  -----------------------------------------------------------------------------
   INDEX VLAN VLAN     PORT F/ S/ P VPI  VCI   FLOW  FLOW       RX   TX   STATE
         ID   ATTR     TYPE                    TYPE  PARA
  -----------------------------------------------------------------------------
       4 2250 common   gpon 0/2 /0  3    3     vlan  200        240  158  up   
      16 2250 common   gpon 0/2 /2  4    3     vlan  200        40   22   down 
      19 2250 common   gpon 0/2 /2  5    3     vlan  200        40   22   down 
      22 2250 common   gpon 0/2 /2  6    3     vlan  200        40   22   down 
      25 2250 common   gpon 0/2 /2  7    3     vlan  200        40   22   down 
      28 2250 common   gpon 0/2 /2  8    3     vlan  200        40   22   down 
      37 2250 common   gpon 0/2 /3  0    3     vlan  200        40   22   down 
      40 2250 common   gpon 0/2 /3  2    3     vlan  200        40   22   down 
      44 2250 common   gpon 0/2 /3  1    3     vlan  200        40   22   down 
      47 2250 common   gpon 0/2 /3  3    3     vlan  200        40   22   down 
      50 2250 common   gpon 0/2 /0  5    0     vlan  2250       250  163  down 
      51 2250 common   gpon 0/2 /0  6    0     vlan  2250       250  163  down 
  -----------------------------------------------------------------------------
   Total : 12  (Up/Down :    1/11)
   Note : F--Frame, S--Slot, P--Port,
          VPI indicates ONT ID for PON, VCI indicates GEM index for GPON,
          v/e--vlan/encap, pritag--priority-tagged,
          ppp--pppoe, ip--ipoe, ip4--ipv4oe, ip6--ipv6oe, vxl--vxlan.
"""
parsed = parse_output(platform="huawei_olt", command="display service-port vlan 2250", data=unparsed)
print(json.dumps(parsed, indent=4))