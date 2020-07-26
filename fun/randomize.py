#!/usr/bin/python3

# The Magi
# Sabi. Simple, Lightweight, but Not Beautiful

import random, sys, os, string

letters = string.ascii_lowercase + string.digits

def randomizeName(listing):
    path = ""
    newName = ""
    if "/" in listing:
        path = listing.rsplit("/")[0] + "/"
        ext = listing.rsplit(".")[1]
        oldName = listing.rsplit("/")[1].rsplit(".")[0]
    else:
        ext = listing.rsplit(".")[1]
        oldName = listing.rsplit(".")[0]

    for i in oldName:
        if newName == "":
            newName += string.ascii_lowercase[random.randrange(0,25)]
        else:
            newName += letters[random.randrange(0,len(letters))]

    while len(newName) < 16:
        newName += letters[random.randrange(0,len(letters))]

    if len(newName) > 16:
        newName = newName[:16]

    newName += "." + ext

    os.rename(listing, path + newName)



def directoryCrawl(listing):
    print(listing + " is a directory. Skipping.")

    """
    # Future Addition: Run directory crawl if -d flag present
    # Incomplete, not working logic.

    files = os.listdir(listing)
    for f in files:
        if os.path.isdir(listing + "/" + f):
            directoryCrawl(listing + "/" + f)
        else:
            randomizeName(listing)
    """

#################
# Start Program #
#################

if len(sys.argv) == 1:
    sys.exit("Enter files as arguments to randomize")

for listing in sys.argv[1:]:
    if listing == os.path.basename(__file__):
        continue
    if os.path.isdir(listing):
        directoryCrawl(listing)
    elif os.path.isfile(listing):
        randomizeName(listing)
sys.exit("All files have been randomized")
