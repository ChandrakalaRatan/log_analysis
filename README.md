# Log Analysis Project
## Objective:
Log Analysis is the first project in Udacity Nano Degree Program. The objective of the project is to create a reporting tool that prints out reports manipulating data from database. This reporting tool is created using python program and psql queries and we use  python module  psycopg2 to connect to the database.

## Requirements: 
The reporting tool needed to answer the following questions:
1. Display the most popular three articles of all time?
2. Display most popular authors of all time?
3. On which days when more than 1% of requests had errors?

## Setup 
We use a virtual machine (VM) to run a web server and a web app that uses it. The VM is a Linux system that runs on top of your own machine. You can share files easily between your computer and the VM. We use the Vagrant software to configure and manage the VM. Here are the tools you'll need to install to get it running:

## Install Git
If you don't already have Git installed, download Git from git-scm.com. Install the version for your operating system.
On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).
(On Mac or Linux systems you can use the regular terminal program.) 
You will need Git to install the configuration for the VM. 

## Install VirtualBox
VirtualBox is the software that actually runs the VM. You can download it from virtualbox.org, here. 

Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.
Vagrant

## Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. You can download it from vagrantup.com. Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Terminals to use
Windows: Use the Git Bash program (installed with Git) to get a Unix-style terminal.
Other systems: Use your favorite terminal program.

## Run the virtual machine!
Using the terminal, change directory to current working directory, then type **vagrant up** to launch your virtual machine.

Once it is up and running, type **vagrant ssh.** This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. 

When you want to log out, type exit at the shell prompt. To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.

Now that you have Vagrant up and running type **vagrant ssh** to log into your VM. change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

## To Run Log Analysis Project
From the terminal, run: git clone https://github.com/ChandrakalaRatan/log_analysis.git  and change the directory in **cd log_analysis** directory

Type ls to ensure that you are inside the directory that contains **newsdata.sql**, **log_analysis.py** **log_analysis_result.rft**,**README.md**.

Now Run **psql -d news -f newsdata.sql**

Execute the following two queries to create two view for problem 3

**CREATE VIEW errors AS  SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT)  AS no_error_request FROM log WHERE NOT status='200 OK' GROUP BY day ORDER BY day;**

**CREATE VIEW total AS SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT) AS total_requests FROM log GROUP BY day ORDER BY day;**

Run this command  **python log_analysis.py**  to see the result and verify with **log_analysis_result.rft**
