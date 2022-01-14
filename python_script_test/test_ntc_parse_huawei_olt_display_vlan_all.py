import os, json
from parse import parse_output

os.environ["NTC_TEMPLATES_DIR"] = "/opt/ntc-templates/ntc_templates/templates"

unparsed="""
XGSPON-D3-DDS_LAB#display vlan all 
{ <cr>|vlanattr<K>|vlantype<E><mux,standard,smart,super>||<K> }: 

  Command:
          display vlan all
  -----------------------------------------------------------------------
  VLAN   Type      Attribute  STND-Port NUM   SERV-Port NUM  VLAN-Con NUM
  -----------------------------------------------------------------------
     1   smart     common                 8               0             -
   100   smart     common                 0               0             -
   110   smart     common                 8               0             -
   111   smart     common                 8              11             -
   200   smart     common                 0               0             -
   202   smart     common                 2               0             -
   245   smart     common                 1               1             -
   250   smart     common                 1               1             -
   319   smart     common                 8               0             -
   333   smart     common                 3               1             -
   500   smart     common                 8               0             -
   501   smart     common                 8              11             -
   502   smart     common                 1               0             -
   503   smart     common                 1               0             -
   504   smart     common                 1               0             -
   505   smart     common                 1               0             -
   506   smart     common                 1               0             -
   507   smart     common                 1               0             -
   508   smart     common                 1               0             -
   509   smart     common                 1               0             -
   510   smart     common                 1               0             -
   511   smart     common                 1               0             -
   512   smart     common                 1               0             -
   513   smart     common                 1               0             -
   514   smart     common                 1               0             -
   515   smart     common                 1               0             -
   516   smart     common                 1               0             -
  1419   smart     common                 1               0             -
  2250   smart     common                 8              10             -
  3000   smart     common                 2               1             -
  3001   smart     common                 0              18             -
  3002   smart     common                 0               0             -
  3500   smart     common                 1               0             -
  -----------------------------------------------------------------------
  Total: 33
  Note : STND-Port--standard port, SERV-Port--service virtual port,
         VLAN-Con--vlan-connect

XGSPON-D3-DDS_LAB# 
"""
parsed = parse_output(platform="huawei_olt", command="display vlan all", data=unparsed)
print(json.dumps(parsed, indent=4))