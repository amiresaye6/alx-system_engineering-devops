# 0x0C-web_server

## General

This repository contains code related to understanding web servers, their functionality, and key concepts in networking.

### Main Role of a Web Server

A web server primarily functions as a mediator between clients and the hosted content, managing requests and delivering responses over the internet.

### Child Process

A child process is a subprocess created by a parent process. In the context of web servers, child processes often refer to instances spawned by the main server process to handle incoming requests independently.

### Parent and Child Processes in Web Servers

Web servers typically employ a parent-child process model to efficiently handle multiple client requests simultaneously. The parent process oversees incoming connections and spawns child processes to manage individual requests, ensuring better resource utilization and scalability.

### Main HTTP Requests

The primary HTTP requests include:
- **GET**: Requests data from a specified resource.
- **POST**: Submits data to be processed to a specified resource.
- **PUT**: Updates a specified resource's data.
- **DELETE**: Deletes a specified resource.

### DNS

Domain Name System (DNS) is a decentralized naming system that translates domain names to IP addresses, facilitating users' access to websites.

### DNS Main Role

DNS serves as the internet's address book, converting human-readable domain names into IP addresses, enabling seamless communication between devices over the internet.

