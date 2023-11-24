# 0x05 Processes and Signals

## Overview
This project focuses on processes and signals in a DevOps environment, specifically using Bash scripting. The tasks involve understanding and manipulating processes, PIDs, and signals in a Linux system.

## Project Details
- **Author:** Sylvain Kalache
- **Weight:** 1
- **Start Date:** Nov 24, 2023 6:00 AM
- **End Date:** Nov 25, 2023 6:00 AM
- **Checker Release Date:** Nov 24, 2023 12:00 PM
- **Auto-review:** Will be launched at the deadline

## About Bash Projects
All projects are auto-corrected with Ubuntu 20.04 LTS unless stated otherwise. Plagiarism is strictly forbidden.

## Resources
- Linux PID
- Linux process
- Linux signal
- Process management in Linux
- Man or help commands: ps, pgrep, pkill, kill, exit, trap

## Learning Objectives
By the end of this project, you are expected to:

### General
- Understand what a PID is
- Understand what a process is
- Find a process's PID
- Kill a process
- Understand what a signal is
- Know the two signals that cannot be ignored

## Requirements
### General
- Allowed editors: vi, vim, emacs
- Files interpreted on Ubuntu 20.04 LTS
- Files should end with a new line
- Mandatory README.md file at the root
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any errors
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks

### Task 0: What is my PID
Write a Bash script that displays its own PID.

Example:
```bash
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
```
[Link to Repo - Task 0](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/0-what-is-my-pid)

### Task 1: List your processes
Write a Bash script that displays a list of currently running processes.

Example:
```bash
sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
# Output truncated for brevity
sylvain@ubuntu$
```
[Link to Repo - Task 1](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/1-list_your_processes)

### Task 2: Show your Bash PID
Write a Bash script that displays lines containing the word "bash" to get the PID of your Bash process.

Example:
```bash
sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
# Output truncated for brevity
```
[Link to Repo - Task 2](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/2-show_your_bash_pid)

### Task 3: Show your Bash PID made easy
Write a Bash script that displays the PID and process name of processes containing the word "bash."

Example:
```bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
# Output truncated for brevity
```
[Link to Repo - Task 3](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/3-show_your_bash_pid_made_easy)

### Task 4: To infinity and beyond
Write a Bash script that displays "To infinity and beyond" indefinitely.

Example:
```bash
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
# Use Ctrl+C to terminate
```
[Link to Repo - Task 4](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/4-to_infinity_and_beyond)

### Task 5: Don't stop me now!
Write a Bash script that stops the process started in Task 4.

Example:
```bash
# Terminal #0
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
# Use Ctrl+C to terminate

# Terminal #1
sylvain@ubuntu$ ./5-dont_stop_me_now
```
[Link to Repo - Task 5](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/5-dont_stop_me_now)

### Task 6: Stop me if you can
Write a Bash script that stops the process started in Task 4 without using kill or killall.

Example:
```bash
# Terminal #0
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
# Use Ctrl+C to terminate

# Terminal #1
sylvain@ubuntu$ ./6-stop_me_if_you_can
```
[Link to Repo - Task 6](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/6-stop_me_if_you_can)

### Task 7: Highlander
Write a Bash script that displays "To infinity and beyond" with a sleep, and "I am invincible!!!" when receiving a SIGTERM signal.

Example:
```bash
# Terminal #0
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
# Use Ctrl+C to terminate

# Terminal #1
sylvain@ubuntu$ ./67-stop_me_if_you_can
```
[Link to Repo - Task 7](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/7-highlander)

### Task 8: Beheaded process
Write a Bash script that kills the process started in Task 7.

Example:
```bash
# Terminal #0
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed

# Terminal #1
sylvain@ubuntu$ ./8-beheaded_process
```
[Link to Repo - Task 8](https://github.com/alx-system_engineering-devops/0x05-processes_and_signals/blob/main/8-beheaded_process)
