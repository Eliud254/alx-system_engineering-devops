# Web Stack Debugging #2 Project

## Overview

This project focuses on debugging web stack-related issues on a Unix machine running Ubuntu 20.04 LTS. The tasks involve running software as another user and configuring Nginx to run as the less privileged `nginx` user for enhanced security.

## Learning Objectives

- Understand the importance of not running web servers as the root user for security reasons.
- Learn how to run software as another user using Bash scripts.
- Debug and fix configurations to ensure Nginx is running as the `nginx` user.

## Tasks

### Task 0: Run software as another user

Create a Bash script (`0-iamsomeoneelse`) that accepts a username as an argument and runs the `whoami` command under the specified user. This script helps demonstrate running commands as privileged users without logging in as root.

Example:

```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
```

### Task 1: Run Nginx as Nginx

Configure the Nginx container to run as the `nginx` user instead of the default root user. This improves security by limiting the impact of potential security issues. The Nginx server should listen on all active IPs on port 8080.

Requirements:

- Nginx must be running as the `nginx` user.
- Nginx must be listening on all active IPs on port 8080.
- Do not use `apt-get remove`.
- Write a Bash script (`1-run_nginx_as_nginx`) to configure the container according to the above requirements.

After debugging, verify the changes:

```bash
root@container-id:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
root@container-id:~#
root@container-id:~# nc -z 0 8080 ; echo $?
0
root@container-id:~#
```

## Usage

Follow the instructions for each task to debug and configure the software accordingly. Execute the provided Bash scripts to automate the setup and validate the changes.
