import os, json
from parse import parse_output

os.environ["NTC_TEMPLATES_DIR"] = "/opt/ntc-templates/ntc_templates/templates"

unparsed="""
XGSPON-D3-DDS_LAB#display service-port vlan 3001 
{ <cr>|e2e<K>|inner-vlan<K>|sort-by<K>||<K> }: 

  Command:
          display service-port vlan 3001
  Switch-Oriented Flow List
  -----------------------------------------------------------------------------
   INDEX VLAN VLAN     PORT F/ S/ P VPI  VCI   FLOW  FLOW       RX   TX   STATE
         ID   ATTR     TYPE                    TYPE  PARA
  -----------------------------------------------------------------------------
      61 3001 common   gpon 0/2 /0  5    2     vlan  200        250  163  down 
      63 3001 common   gpon 0/2 /0  6    2     vlan  200        250  163  down 
  -----------------------------------------------------------------------------
   Total : 2  (Up/Down :    0/2)
   Note : F--Frame, S--Slot, P--Port,
          VPI indicates ONT ID for PON, VCI indicates GEM index for GPON,
          v/e--vlan/encap, pritag--priority-tagged,
          ppp--pppoe, ip--ipoe, ip4--ipv4oe, ip6--ipv6oe, vxl--vxlan.
          When FLOW TYPE is plist, the value of FLOW PARA is a byte in
          hexadecimal format and indicates a priority list. Eight bits
          of its binary value indicate priorities 0-7 from the least
          significant bit to the most significant bit. Value 1 indicates
          that the priority is used. For example, if FLOW PARA is 0x23 and
          its binary format is 0010 0011, priorities 0, 1 and 5 are used
"""
parsed = parse_output(platform="huawei_olt", command="display service-port vlan 2250", data=unparsed)
print(json.dumps(parsed, indent=4))