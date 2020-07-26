#!/usr/bin/python3

# The Magi
# Sabi. Simple, Lightweight, but Not Beautiful

import string, random, sys, os


if len(sys.argv) != 2:
    sys.exit("Please enter one file name to change.\npython3 randomName.py waifu.png")
if sys.argv[1] in ["-h","--help"]:
    sys.exit("Enter the name of a file to provide a random name.\npython3 randomName.py waifu.png")

new = ""
ext = ""
old = sys.argv[1]
if "." in old:
    ext = "." + old.rsplit('.',1)[1]
for i in range(random.randrange(8,17)):
    new += string.ascii_lowercase[random.randrange(0,26)]
new += ext

if os.path.isfile(os.getcwd() + "/" + old):
    os.rename(os.getcwd() + "/" + old, os.getcwd() + "/" + new)
    print(old + "changed to " + new)
else:
    print(new)
