# Web Stack with Redundancy

This repository contains a simplified diagram of a LAMP (Linux, Apache, MySQL, PHP) stack with considerations for system redundancy.

## Web Stack Diagram

         +-----------------------------------+
         |                                   |
         |               Load Balancer       |
         |                                   |
         +--------+--------------------------+
                  |
    +-------------+--------------+
    |                            |
    |            Web Servers      |
    |                            |
    +-------------+--------------+
                  |
    +-------------+--------------+
    |                            |
    |           Database Servers  |
    |                            |
    +-------------+--------------+

## Component Explanations

1. **Load Balancer**:
   - The Load Balancer distributes incoming web traffic across multiple web servers to ensure optimal resource usage and high availability.
   - It monitors the health of each web server and routes traffic only to healthy servers.

2. **Web Servers (Apache)**:
   - These servers handle incoming HTTP requests from clients (browsers).
   - They serve static content and process dynamic content using PHP.

3. **Database Servers (MySQL)**:
   - These servers store and manage the website's data in a MySQL database.
   - They respond to queries from the web servers, retrieving and updating data as needed.

## System Redundancy

System redundancy involves duplicating critical components or systems to ensure continued operation in case of failure. In this web stack:

- **Load Balancer Redundancy**:
  - You can have multiple load balancers working in tandem. If one fails, the others can take over, ensuring uninterrupted traffic distribution.

- **Web Server Redundancy**:
  - Multiple web servers are used to distribute the load. If one server fails, the others can continue serving traffic.

- **Database Server Redundancy**:
  - Techniques like master-slave replication or clustering can be employed to create redundancy for the database. If one database server fails, another can take over.

## Acronyms

- **LAMP**:
  - Acronym for a popular open-source web development platform: Linux (operating system), Apache (web server), MySQL (database), PHP (scripting language).

- **SPOF**:
  - Stands for "Single Point of Failure". It refers to a component that, if it fails, will cause the entire system to fail. Redundancy is implemented to mitigate SPOFs.

- **QPS**:
  - Stands for "Queries Per Second". It measures the number of database queries a system can handle in one second. It's an important metric for database performance.

Feel free to use and modify this information as needed for your specific project.
