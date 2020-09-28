# Systems Tools
These are some tools that I have made to make systems administration easier.

## License
In the /tools repo at https://github.com/sabi/tools you can find a copy of the MIT License.  Please distribute it and include it with each copy of this software.

## Installation
*Note*: Code in this will often show the use for how to run these scripts if they are not installed into your path.
To install these scripts into your path.  Copy them into `/usr/local/bin` then you can summon them from anywhere by just calling their name.
You could add symbolic links if you prefer to not have to use the .py extension.  Or could alias them in your .bashrc file.

## Description of Scripts

### findSlash.py
This generates a list of block devices that contain / and a list of devices that dont.  Currently, this is not an ideal setup. But was for functional use.
If someone wants to make this more general purpose, instead of checking against the size of the disk, there is a better alternative.  This was built to simply
distinguish / devices from data storage disks.  Pretty slapped together.

### genHosts.py
This reads the current Ansible hosts file and then allows you to conveniently add new hosts to the file.  
`python3 genHosts.py name_of_host category_for_hosts_file`
I am using this appended to my install script for each new server installation so that my Ansible files stay up to date.
