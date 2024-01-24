# MySQL 5.7.x Installation Guide

This guide provides step-by-step instructions for installing MySQL 5.7.x on Ubuntu using the official MySQL APT repository.

## Prerequisites

- Ubuntu operating system (version 18.04 or later recommended)

## Installation Steps
 **Install MySQL Server 5.7.x:**

    ```bash
    vim signature.key
    # get the signature key from here https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html
    sudo apt-key add signature.key
    sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
    sudo apt-get update
    sudo apt-cache policy mysql-server
    sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
    ```


**Access MySQL:**

    ```bash
    mysql -u root -p
    or
    sudo mysql -p
    ```

    Enter the password you set during the secure installation process.

## Additional Notes

- If you encounter any issues or have specific requirements, refer to the [official MySQL documentation](https://dev.mysql.com/doc/) for the most up-to-date instructions and information.

- Ensure that your system meets the [MySQL 5.7 system requirements](https://dev.mysql.com/doc/refman/5.7/en/requirements.html).

- For security best practices, consider configuring a firewall and limiting access to your MySQL server.
