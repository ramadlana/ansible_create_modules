# This is for testing purposed
# 1. put unparsed data on unparsed variable
# 2. ctrl+p and search for vendorname_osname_show_test
# 3. edit the textfsm
# 4. run the test here

import os
import json
from ntc_templates.parse import parse_output

directory = os.path.dirname(__file__)
fileLoc = os.path.join(directory, "ntc-templates/ntc_templates/templates")
os.environ["NTC_TEMPLATES_DIR"] = fileLoc

unparsed="""
display vlan  desc 1-4093 | no-more 
  ------------------------------------------------------
  VLAN             VLAN description
  ------------------------------------------------------
   110             IPTV-Multicast                  
   111             IPTV-Unicast                    
   250             SPEEDY 2                        
   319             OAM                             
   500             SIP-1                           
  1419             VLAN_MGT_OASIS_10.14.19.0/24    
  2250             SPEEDY                          
  ------------------------------------------------------
  Total: 7       

XGSPON-D3-DDS_LAB#
"""
parsed = parse_output(platform="huawei_olt", command="display vlan  desc 1-4093 | no-more", data=unparsed)
print(json.dumps(parsed, indent=4))
