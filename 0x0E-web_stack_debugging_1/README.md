Sure! Here's a concise README file for your project:

---

# Web Stack Debugging #1

**Objective:** Debug and fix issues in the Nginx web server setup.

## Tasks

### Task 0: Nginx likes port 80
- **Issue:** Nginx is not listening on port 80.
- **Requirements:** 
  - Nginx must be running and listening on port 80.
  - Write a Bash script to automate the fix.
- **Usage:**
  ```bash
  ./0-nginx_likes_port_80
  ```
  Test with:
  ```bash
  curl 0:80
  ```

### Task 1: Make it sweet and short
- **Objective:** Simplify the fix from Task 0 in a concise script.
- **Requirements:**
  - The Bash script must be 5 lines or less.
  - The service must report that Nginx is not running.
- **Usage:**
  ```bash
  ./1-debugging_made_short
  ```
  Test with:
  ```bash
  curl 0:80
