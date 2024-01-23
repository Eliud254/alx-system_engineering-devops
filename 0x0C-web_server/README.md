# Project 0x0C: Web Server

## Introduction

This project, led by Sylvain Kalache, focuses on web server configuration, DevOps, and SysAdmin skills. The primary goal is to ensure that your `web-01` server is configured according to requirements. Additionally, you are expected to create a Bash script that automates the configuration of an Ubuntu machine, eliminating the need for manual intervention.

## Project Details

- **Project Dates:** Start - January 22, 2024, 6:00 AM | End - January 24, 2024, 6:00 AM
- **Checker Release:** January 22, 2024, 6:00 PM
- **Auto Review:** A review will be automatically launched at the project deadline.

## Concepts Covered

### Main Concepts
- **Child Process:**
  - Understanding the role of a child process is crucial for this project.

### Key Aspects Evaluated
- **Configuration Requirements:**
  - Grading based on the correct configuration of the `web-01` server.
- **Automation Script:**
  - Evaluation of the Bash script's ability to automate server configuration without human intervention.

### Example Scenario
- If, for instance, you need to create a file `/tmp/test` containing the string "hello world" and modify the Nginx configuration to listen on port 8080 instead of 80, you are expected to automate this using a Bash script.

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

## Guidance and Philosophy

This project emphasizes the importance of automating tasks to increase efficiency. A lazy Software Engineer, in this context, is someone who automates repetitive tasks, enabling a focus on more intellectually stimulating work. The checker will execute your script as the root user, eliminating the need for `sudo` commands.

## Testing Your Script

Feel free to reproduce the checker environment:

1. Start a Ubuntu 20.04 sandbox.
2. Run your script on it.
3. Observe its behavior.

## Learning Objectives

Upon completion of this project, you should be able to explain:

- The main role of a web server.
- The concept of a child process.
- The reason web servers have parent and child processes.
- The primary HTTP requests.
- DNS fundamentals, including its role and common record types (A, CNAME, TXT, MX).

## Resources

### Reading and Watching
- [How the web works](#)
- [Nginx](#)
- [How to Configure Nginx](#)
- [Child process concept page](#)
- [Root and subdomain](#)
- [HTTP requests](#)
- [HTTP redirection](#)
- [Not found HTTP response code](#)
- [Log files on Linux](#)

### For Reference
- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

### Man or Help Commands
- `scp`
- `curl`
