---
title: Discovering RPyC
date: '2020-06-27'
slug: decouverte-rpyc
lang: en
key: decouverte-rpyc
---

![](images/Rpyc3-logo-medium.56e72187.png)

Not long ago I discovered RPyC:
https://rpyc.readthedocs.io/en/latest/

It’s a handy tool to control remote machines over SSH.

Why not use Ansible?

It’s simply a different approach. Ansible is great (I do use it sometimes): lots of modules and a big community. But for some tasks I’d rather write Python with loops/while/etc., and I’m not a huge fan of YAML.

RPyC lets two Python processes talk to each other. For example, I can create a Python list on server1, fetch it on my local machine, and then send it through RPyC to a Python process on server2.

I’m exploring the possibilities; here’s an example:

```python
import rpyc 
from rpyc.utils.classic import upload_package 
from rpyc.utils.zerodeploy import MultiServerDeployment 
from rpyc.utils.zerodeploy import DeployedServer 
from plumbum import SshMachine 
import ldap3 
import pyasn1 

# create the deployment 

list_host=['mysrv.domain.lan'] 
list_ssh=[] 

for f in list_host: 
    mach = SshMachine(f, user="root", keyfile="/home/user/.ssh/id_ed25519",port="22") 
    list_ssh.append(mach) 

def get_etc_file(): 
    import glob 
    allfile = [] 
    for i in glob.glob('/etc/*'): 
        allfile.append(i) 
    return allfile 

def get_ldap_version(): 
    import ldap3 
    return ldap3.__version__ 

dep = MultiServerDeployment(list_ssh) 
conns = dep.classic_connect_all() 

for conn in conns: 

    run_get_etc_file = conn.teleport(get_etc_file) 
    print(run_get_etc_file()) 

    rpyc.classic.upload_package(conn, ldap3) 
    rpyc.classic.upload_package(conn, pyasn1) 
    run_get_ldap_version = conn.teleport(get_ldap_version) 

    print(run_get_ldap_version())
```

In this example there’s something interesting: `rpyc.classic.upload_package`. The servers I connect to don’t have the `ldap3` package installed, but it is installed on my machine. With RPyC I push it into the remote Python session (without installing it on the server), and it becomes usable.

`teleport` lets me send a function to the remote interpreter, and then execute it there. I like the idea.

I’m still discovering the tool. **Warning: I haven’t done real production tests or heavy usage**, but I do see interesting potential here.
