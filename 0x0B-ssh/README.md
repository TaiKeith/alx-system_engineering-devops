# 0x0B. SSH
`DevOps` `SSH` `Network` `SysAdmin` `Security`

## Background Context
Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of [a previous project](https://intranet.alxswe.com/tasks/1223) shared in your intranet profile.

You can access your server information in the [my servers](https://intranet.alxswe.com/servers) section of the intranet, each line with contains the IP andusername you should use to connect via `ssh`.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.

## Resources
**Read or watch:**
* [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
* [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
* [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config File](https://www.ssh.com/academy/ssh/config)
* [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
* [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
* [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc)

**For reference:**
* [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
* [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
* [IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)
* [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
* [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)

**man or help:**
* `ssh`
* `ssh-keygen`
* `env`

## Learning Objectives
### General
* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`
