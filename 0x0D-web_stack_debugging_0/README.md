# Web Stack Debugging #0

## Overview
This project focuses on debugging web stacks, a crucial skill for Full-Stack Software Engineers. The goal is to identify and fix issues in a broken web stack manually before creating a Bash script for automation.

## Scenario
Imagine a server where certain conditions must be met for a web application to function properly: a copy of the `/etc/passwd` file in `/tmp` and a file named `/tmp/isworking` containing the string "OK." The task involves debugging a provided example and creating a Bash script to automate the fixes.

## Example Fix
```bash
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
```

## Usage
1. Install Docker if not already installed.
2. Use the provided container to simulate the debugging environment.
3. Manually debug and fix the web stack issues.
4. Create a Bash script for automating the fixes.

## Docker Installation (Optional)
- Mac OS
- Windows
- Ubuntu 14.04 (Note: Docker for Ubuntu 14 is deprecated; adjustments needed)
- Ubuntu 16.04
