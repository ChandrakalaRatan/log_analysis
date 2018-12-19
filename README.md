# Log Analysis Project
## Objective:
Log Analysis is the first project in Udacity Nano Degree Program. The objective of the project is to create a reporting tool that prints out reports manipulating data from database. This reporting tool is created using python program and psql queries and we use  python module  psycopg2 to connect to the database.

## Requirements: 
The reporting tool needed to answer the following questions:
1. Display the most popular three articles of all time?
2. Display most popular authors of all time?
3. On which days when more than 1% of requests had errors?

## System Requirements
Download Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download Vagrant from  Download it from vagrantup.com. and install.
2. Download the VM configuration frome FSND-Virtual-Machine.zip and install.
3. Clone this repository to a directory of your choice.
4. Change directory to the vagrant directory 
5. Download  log_analysis.py files from the respository and move them to your vagrant directory within your VM

## How to run the program
1. Run the command vagrant up. To start the virtual machine
2. Run vagrant ssh to log in to your newly installed Linux VM!
3. Download  and extract the newsdata.zip in you working directory and Run psql -d news -f newsdata.sql
4. Execute the following two queries to create two view for problem 3
CREATE VIEW errors AS  SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT)  AS no_error_request FROM log WHERE NOT status='200 OK' GROUP BY day ORDER BY day;
CREATE VIEW total AS SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT) AS total_requests FROM log GROUP BY day ORDER BY day;
5. Run this command  python log_analysis.py to see the result and verify with log_analysis_result.rft
