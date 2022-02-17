#!/usr/bin/env python3

import os
import sys
from time import sleep
import prlsdkapi

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("default")

if 'VM_NAME' in os.environ:
    VM_NAME = os.environ['VM_NAME']
else:
    VM_NAME = 'macOS'
if 'INSTALL_COMMAND' in os.environ:
    INSTALL_COMMAND = os.environ['INSTALL_COMMAND']
else:
    INSTALL_COMMAND = '/Volumes/Image Volume/install'
if 'SDK_LIBRARY' in os.environ:
    SDK_LIBRARY = os.environ['SDK_LIBRARY']
    prlsdkapi.prlsdk.SetSDKLibraryPath(SDK_LIBRARY)
else:
    warnings.warn(
        "The SDK_LIBRARY environment variable is not set. This may not work.")


def sendKey(vm, io, key):
    if io is None:
        raise RuntimeError("IO not connected to virtual machine")
    keycodes = prlsdkapi.prlsdk.consts.ScanCodesList
    chars = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'H',
        'i': 'I',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'o': 'O',
        'p': 'P',
        'q': 'Q',
        'r': 'R',
        's': 'S',
        't': 'T',
        'u': 'U',
        'v': 'V',
        'w': 'W',
        'x': 'X',
        'y': 'Y',
        'z': 'Z',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '\\': 'BACKSLASH',
        '[': 'CBRACE_LEFT',
        ']': 'CBRACE_RIGHT',
        ';': 'COLON',
        '.': 'GREATER',
        ',': 'LESS',
        '§': 'LESS_GREATER',
        '-': 'MINUS',
        '=': 'PAD_EQUAL',
        '+': 'PAD_PLUS',
        '/': 'PAD_SLASH',
        '*': 'PAD_STAR',
        "'": 'QUOTE',
        '`': 'TILDA',
        ' ': 'SPACE',
        '	': 'TAB'
    }
    shiftChars = {
        'A': 'A',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F',
        'G': 'G',
        'H': 'H',
        'I': 'I',
        'J': 'J',
        'K': 'K',
        'L': 'L',
        'M': 'M',
        'N': 'N',
        'O': 'O',
        'P': 'P',
        'Q': 'Q',
        'R': 'R',
        'S': 'S',
        'T': 'T',
        'U': 'U',
        'V': 'V',
        'W': 'W',
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
        ')': '0',
        '!': '1',
        '@': '2',
        '#': '3',
        '$': '4',
        '%': '5',
        '^': '6',
        '&': '7',
        '*': '8',
        '(': '9',
        '|': 'BACKSLASH',
        '{': 'CBRACE_LEFT',
        '}': 'CBRACE_RIGHT',
        ':': 'COLON',
        '>': 'GREATER',
        '<': 'LESS',
        '±': 'LESS_GREATER',
        '_': 'MINUS',
        '"': 'QUOTE',
        '?': 'SLASH',
        '~': 'TILDA'
    }
    if key in chars:
        io.send_key_event(vm, keycodes[chars[key]], prlsdkapi.consts.PKE_CLICK)
    elif key in shiftChars:
        io.send_key_event(
            vm, keycodes['SHIFT_LEFT'], prlsdkapi.consts.PKE_PRESS
        )
        io.send_key_event(
            vm, keycodes[shiftChars[key]], prlsdkapi.consts.PKE_CLICK
        )
        io.send_key_event(
            vm, keycodes['SHIFT_LEFT'], prlsdkapi.consts.PKE_RELEASE
        )
    elif key in keycodes:
        io.send_key_event(
            vm, keycodes[key], prlsdkapi.consts.PKE_CLICK
        )
    elif key.upper() in keycodes:
        io.send_key_event(
            vm, keycodes[key.upper()], prlsdkapi.consts.PKE_CLICK
        )
    else:
        raise RuntimeError("Unable to find keycode for '{}'".format(key))


def sendEnter(vm, io):
    sendKey(vm, io, 'enter')


def sendCmdShiftT(vm, io):
    keycodes = prlsdkapi.consts.ScanCodesList
    io.send_key_event(vm, keycodes['CMD_LEFT'], prlsdkapi.consts.PKE_PRESS)
    io.send_key_event(vm, keycodes['SHIFT_LEFT'], prlsdkapi.consts.PKE_PRESS)
    io.send_key_event(vm, keycodes['T'], prlsdkapi.consts.PKE_CLICK)
    io.send_key_event(vm, keycodes['SHIFT_LEFT'], prlsdkapi.consts.PKE_RELEASE)
    io.send_key_event(vm, keycodes['CMD_LEFT'], prlsdkapi.consts.PKE_RELEASE)


def sendCommand(vm, io, text):
    for i in range(len(text)):
        sendKey(vm, io, text[i])
    sendEnter(vm, io)


prlsdkapi.init_desktop_sdk()
service = prlsdkapi.Server()
service.login_local().wait()
vmList = service.get_vm_list().wait()
vm = None
vmName = VM_NAME
for i in range(vmList.get_params_count()):
    if vmList.get_param_by_index(i).get_name() == vmName:
        vm = vmList.get_param_by_index(i)
        break
if vm is None:
    raise RuntimeError(
        "Unable to access virtual machine '{}'.".format(vmName))
io = prlsdkapi.VmIO()
runstate = vm.get_state().wait().get_param().get_state()
if runstate != prlsdkapi.consts.VMS_RUNNING:
    raise RuntimeError(
        "Virtual machine '{}' is not running".format(vm.get_name()))
io.connect_to_vm(vm).wait()
sendEnter(vm, io)
sleep(5)
sendCmdShiftT(vm, io)
sleep(5)
sendCommand(vm, io, INSTALL_COMMAND)
io.disconnect_from_vm(vm)
prlsdkapi.deinit_sdk()
