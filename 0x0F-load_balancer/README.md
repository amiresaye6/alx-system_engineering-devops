# Redundant Web Server Setup - README

## Introduction
This README provides guidance on setting up redundancy for web servers to improve infrastructure reliability and handle increased traffic.

## Requirements
- 2 additional servers: 
  - gc-[STUDENT_ID]-web-02-XXXXXXXXXX
  - gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
- Ubuntu server operating system

## Steps to Achieve Redundancy
1. **Server Provisioning**
    - Provision two new Ubuntu servers: `gc-[STUDENT_ID]-web-02-XXXXXXXXXX` and `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`.

2. **Bash Scripts for Configuration**
    - Create Bash scripts to automate the setup process for a new Ubuntu server:
    
    - **Script 1: Initial Server Configuration**
        - Filename: `initial_server_config.sh`
        - Purpose: Installs necessary packages, sets up basic configurations, and ensures system updates.

    - **Script 2: Web Server Configuration**
        - Filename: `web_server_config.sh`
        - Purpose: Installs and configures web server software (e.g., Apache or Nginx), sets up necessary directories, and ensures services are running.

    - **Script 3: Load Balancer Configuration**
        - Filename: `load_balancer_config.sh`
        - Purpose: Sets up load balancing software (e.g., HAProxy or Nginx) to distribute traffic among web servers and ensures its proper functioning.

3. **Execution Order**
    - Execute the scripts in the following order:
        1. `initial_server_config.sh` on both web servers and load balancer.
        2. `web_server_config.sh` on both web servers.
        3. `load_balancer_config.sh` on the load balancer.

4. **Testing Redundancy**
    - Verify redundancy by testing the setup:
        - Simulate server failure by stopping one web server and ensuring the second web server handles requests effectively.
        - Test load balancing functionality by distributing traffic among both web servers using the load balancer.

## Notes
- Ensure proper permissions are set for executing the Bash scripts (`chmod +x script_name.sh`).
- Modify the scripts as necessary to accommodate specific software or configurations used in your environment.
- Regularly update and maintain the servers and configurations to ensure optimal performance and reliability.
