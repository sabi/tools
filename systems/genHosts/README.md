# genHosts
Sabi. Simple, Lightweight, but Not Beautiful.
 
## Setup
- Download and extract this genHosts directory
- Copy the hosts file generator to your PATH
  - `# cp genHosts.py /usr/local/bin`
- Create an easy to call symlink
  - `# ln -s /usr/local/bin/genHosts.py /usr/local/bin/genHosts`
- Consider creating a systemd service to start genHosts at boot

## How to use
- Anytime you need to add a new host to your Ansible hosts file.  `curl http://your_ansible_master_ip:11110/ansible_category/hostname_of_new_node`
- *Suggestion*: Consider appending `curl http://your_ansible_master_ip:11110/$1/$2` to your installation scripts so that you can keep your hosts file up to date as you build new servers.
