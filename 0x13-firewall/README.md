# UFW (Uncomplicated Firewall) Configuration README

## Introduction

Welcome to this README guide for configuring UFW (Uncomplicated Firewall). This guide provides a simple set of instructions to set up UFW with a default policy of denying incoming traffic while allowing specific ports for SSH, HTTPS, and HTTP.

## Instructions

```bash
# 1. Set Default Policy for Incoming Traffic
sudo ufw default deny incoming

# 2. Allow SSH (Port 22)
sudo ufw allow 22

# 3. Allow HTTPS (Port 443)
sudo ufw allow 443

# 4. Allow HTTP (Port 80)
sudo ufw allow 80

# 5. Enable UFW
sudo ufw enable
