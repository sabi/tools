#!/usr/bin/python3

# genHosts.py
# Sabi. Simple, Lightweight, but Not Beautiful

# See LICENSE for a copy of the MIT License (found in the /tools directory)
# that should be distributed with this software

# For more check out https://github.com/sabi

import os, sys

version = 1.0

# This is the path of the hosts file
hostsFile = "W00T"

# This function reads the old hosts and adds each as a key:value pair
# as server group:list of servers
def readOldHosts():
    bigDict = {}
    currentCategory = ""
    with open(hostsFile, "r") as hfile:
        data = hfile.read().splitlines()
    for line in data:
        if line != "" and line[0] == "[":
            currentCategory = line
            bigDict[line] = []
        elif line != "":
            bigDict[currentCategory].append(line)
    return bigDict

# This function is what actually writes the new hosts file
def writeHosts(bigDict):
    with open(hostsFile, "w") as hfile:
        for group in bigDict.keys():
            hfile.write(group + "\n")
            for server in bigDict[group]:
                hfile.write(server + "\n")
            hfile.write("\n")



# Start Program
if len(sys.argv) > 1:
    if sys.argv[1] in ["-h","--help"]:
        sys.exit("python3 genHosts.py name_of_host category_for_hosts_file")
elif len(sys.argv) != 3:
    sys.exit("You must have two arguments.\npython3 genHosts.py name_of_host category_for_hosts_file")

if hostsFile == "W00T":
    sys.exit("Change the path of your hosts file in the top of this script.")

newhost = sys.argv[1]
category = sys.argv[2]
if category[0] != '[' and category[-1] != ']':
    category = '[' + sys.argv[2] + ']'
bigDict = readOldHosts()
if category not in bigDict.keys():
    bigDict[category] = []
bigDict[category].append(newhost)
writeHosts(bigDict)
sys.exit("Hosts file has been updated")
