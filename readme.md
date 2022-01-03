WHEN Development you can create modules on
```
/usr/share/ansible/plugins/modules
if file still development and still on this folder we can call directly on playbook using 
multipolar_module_huawei_display_ip_routing_table:
```

And then after finised create our own collection in 
```
/usr/share/ansible/collections/ansible_collections/multipolar/vrp/plugins/modules
noted its folder stucture
multipolar for workspace
vrp for os for system name
and put modules on plugin/modules

and call on playbook and put module using this format
multipolar.vrp.display_ip_routing_table:
```

MOVE and rename it just using command
```
mv multipolar_module_huawei_display_ip_routing_table.py /usr/share/ansible/collections/ansible_collections/multipolar/vrp/plugins/modules/display_ip_routing_table.py

ansible-playbook -i inventory_host_huawei.yml playbook_for_module_huawei_display_ip_routing_table_using_collection.yml 
```

Template Location
on Linux ENV Vars
export NTC_TEMPLATES_DIR=/opt/ntc-templates/ntc_templates/templates

or

on script.py
```
os.environ["NTC_TEMPLATES_DIR"] = "/opt/ntc-templates/ntc_templates/templates"
```