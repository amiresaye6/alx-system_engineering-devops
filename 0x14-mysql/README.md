# MySQL Installation Guide

This guide provides instructions for installing MySQL on Ubuntu using the official MySQL APT repository.

## Prerequisites

- Ubuntu operating system (version 18.04 or later recommended)

## Installation Steps

1. **Download and Install MySQL APT Repository Configuration Package:**

    ```bash
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb
    sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb
    ```

    During the installation, choose `mysql-5.7` as the MySQL version.

2. **Update Package Lists:**

    ```bash
    sudo apt-get update
    ```

3. **Install MySQL Server:**

    ```bash
    sudo apt-get install mysql-server
    ```

4. **Secure your MySQL installation:**

    After installation, MySQL provides a script to help you secure your installation. Run:

    ```bash
    sudo mysql_secure_installation
    ```

    Follow the prompts to set a root password and secure other aspects of the MySQL installation.

5. **Access MySQL:**

    ```bash
    mysql -u root -p
    ```

    Enter the password you set during the secure installation process.

## Additional Notes

- If you encounter any issues or have specific requirements, refer to the [official MySQL documentation](https://dev.mysql.com/doc/) for the most up-to-date instructions and information.

- Ensure that your system meets the [MySQL system requirements](https://dev.mysql.com/doc/refman/5.7/en/requirements.html).

- For security best practices, consider configuring a firewall and limiting access to your MySQL server.

