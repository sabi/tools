#!/usr/bin/python3

# findSlash.py
# Sabi. Simple, Lightweight, but Not Beautiful

# See LICENSE for a copy of the MIT License (found in the /tools directory)
# that should be distributed with this software

import os, string, sys

version = 1.0

def help():
    sys.exit("""
python3 where_is_slash.py [option]

Options:
    -h  --help          : print this menu
    -sa --slash-all     : print list of disk name-size pairs associated with slash
    -sn --slash-names   : print list of all disk names associated with slash
    -ss --slash-sizes   : print list of all sizes of disks associated with slash
    -da --data-all      : print list of all disk name-size pairs associated with data
    -dn --data-names    : print list of all disk names associated with data
    -ds --data-size     : print list of all sizes of disks associated with data
    """)

# Get list of block devices with /dev/sdX name and size
lsblk = os.popen("lsblk -o name,size").read().split()
lsblk = lsblk[2:]

# Create a dictionary of dictionaries of data disks and slash devices
# key:value -> name:size   Ex: "slash":{sda:938G}
blkDevices = {"data":{},"slash":{}}
state = 0
for dev in lsblk:
    if dev[0] not in string.ascii_letters and dev[0] not in string.digits:
        dev = dev[2:]
    if state == 0:
        pair = []
        pair.append(dev)
        state = 1
    elif state == 1:
        pair.append(dev)
        if pair[1][-1] != "T":
            blkDevices["slash"][pair[0]] = pair[1]
        else:
            blkDevices["data"][pair[0]] = pair[1]
        state = 0

if len(sys.argv) > 1:
    if sys.argv[1] in ["-h", "--help"]:
        help()
    elif sys.argv[1] in ["-sa","--slash-all"]:
        for name,size in blkDevices["slash"].items():
            print(name, size)
    elif sys.argv[1] in ["-sn","--slash-names","--slash-name"]:
        for i in blkDevices["slash"].keys():
            print(i)
    elif sys.argv[1] in ["-ss","--slash-sizes","--slash-size"]:
        for i in blkDevices["slash"].values():
            print(i)
    elif sys.argv[1] in ["-da","--data-all"]:
        for name,size in blkDevices["data"].items():
            print(name, size)
    elif sys.argv[1] in ["-dn","--data-names","--data-name"]:
        for i in blkDevices["data"].keys():
            print(i)
    elif sys.argv[1] in ["-ds","--data-sizes","--data-size"]:
        for i in blkDevices["data"].values():
            print(i)
    elif sys.argv[1] in ["-v","--version"]:
        sys.exit(version)
else:
    help()
