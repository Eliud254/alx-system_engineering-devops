Here is a possible README.md file for the project:

# 0x09. Web infrastructure design

This project is about designing a simple web infrastructure that hosts a website reachable via www.foobar.com. The web stack consists of a single server with a LAMP stack (Linux, Apache, MySQL, PHP).
i

## Explanation

The diagram shows the main components of the web infrastructure and how they interact with each other.

- A **server** is a physical or virtual machine that runs an operating system and provides services to clients over a network.
- A **domain name** is a human-readable identifier that maps to an IP address, which is a numerical label that identifies a device on a network. Domain names are managed by the Domain Name System (DNS), which is a distributed database that translates domain names to IP addresses and vice versa.
- A **DNS record** is a data entry in the DNS that defines how a domain name is resolved. For example, an A record maps a domain name to an IPv4 address, and a CNAME record maps a domain name to another domain name. In this case, www.foobar.com is a CNAME record that points to foobar.com, which is an A record that points to the server IP 8.8.8.8.
- A **web server** is a software that handles HTTP requests from clients and serves web pages or files. In this case, Nginx is the web server that listens on port 80 and serves the static files (HTML, CSS, images, etc.) from the /var/www/html directory.
- An **application server** is a software that runs the application logic and executes the dynamic content (PHP scripts, etc.) that the web server cannot handle. In this case, PHP-FPM is the application server that listens on port 9000 and processes the PHP files from the /var/www/html directory.
- An **application file** is a source code file that contains the logic and functionality of the web application. In this case, the application files are the PHP files that generate the web pages dynamically based on the user input and the database data.
- A **database** is a software that stores and manages data in a structured way. In this case, MySQL is the database that runs on port 3306 and stores the data for the web application in tables and columns.
- The user accesses the website by typing www.foobar.com in the browser. The browser sends a DNS query to the DNS resolver, which is a server that knows how to find the IP address of a domain name. The DNS resolver contacts the authoritative DNS server for the foobar.com domain, which is the server that has the final authority over the DNS records for that domain. The authoritative DNS server responds with the IP address of foobar.com, which is 8.8.8.8. The browser then sends an HTTP request to the server at 8.8.8.8 on port 80. The web server receives the request and checks the URI (Uniform Resource Identifier) to determine what file to serve. If the URI is a static file, the web server serves it directly from the /var/www/html directory. If the URI is a PHP file, the web server passes the request to the application server via the FastCGI protocol. The application server executes the PHP file and queries the database if needed. The application server returns the output of the PHP file to the web server, which then sends it back to the browser as an HTTP response. The browser renders the response as a web page and displays it to the user.
