#!/usr/bin/env python3

import prlsdkapi

newlibrary = "/Users/chjones/Development/mkmacvm/prlsdkapi/Library/Frameworks/ParallelsVirtualizationSDK.framework/Versions/9/ParallelsVirtualizationSDK"

prlsdkapi.prlsdk.SetSDKLibraryPath(newlibrary)
prlsdkapi.init_desktop_sdk()
service = prlsdkapi.Server()
service.login_local().wait()
vmList = service.get_vm_list().wait()
for i in range(vmList.get_params_count()):
    if vmList.get_param_by_index(i).get_name() == "macOS":
        macVm = vmList.get_param_by_index(i)
        break
if macVm is None:
    print("Unable to access virtual machine 'macOS'. Exiting.")
    exit(1)

prlsdkapi.deinit_sdk()
