#!/usr/bin/python3


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule


def run_module():
    # Defining params structure that can receive
    module_args = dict(
        ucapan=dict(type='str', required=False, default=False),
        isChanged=dict(type='bool', required=False, default=False)
    )

    # will be return
    result = dict(
        changed=False,
        ucapan='',
    )

    # create new AnsibleModule instance called (module)
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # checkmode if true, only return the result immediately, all bellow code after this block cannot executed
    if module.check_mode:
        result['check_mode_msg'] = "this is check mode enable message"
        module.exit_json(**result)

    # ALL LOGIC (trial)
    # result['ucapan'] = module.params['ucapan']

    # # is Changed Logic (yellow)
    # if module.params['isChanged']:
    #     result['changed'] = True

    #  # Fail Condition Logic (red)
    # if module.params['ucapan'] == 'gagal':
    #     module.fail_json(msg='you type gagal, so this program return red colour', **result)
    
    # # return success (green)
    # module.exit_json(**result)
    # END of LOGIC

    # LOGIC (real)
    # 192.168.1.1
    # # 1. check ping on DCN to PE
    # from netmiko import ConnectHandler
    # # so on
    # # 1.b parsing (lanjut jam 3)
    # loss = "0% loss"
    # if (loss == "0% loss"):
    #     outpu_from_dcn = "available"

    # # 2. if timeout
    #     # 2.a return "available"
    #     if (outpu_from_dcn == "available"):
            
    # 3. if reply
        # 3.a return "already used"
        # so on

    # END of LOGIC (real)

def main():
    run_module()


if __name__ == '__main__':
    main()


# Latihan:
# 1. buat inputan nama, umur, alamat
        # return = hello (nama), jika umur > 30 --> anda sudah tua, anda beralamt di (alamat)
# 2. pake inventory, ke huawei olt -> ssh -> show version, -> return apa adanya
