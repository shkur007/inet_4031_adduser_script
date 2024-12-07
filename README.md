Assignment 9: Managing Users and Automating User Management
Description
This assignment focuses on Linux user account and group management using both manual command-line tools and Python automation. The first part involves creating and managing users and groups manually. The second part automates these processes using a Python script, showcasing the importance of scripting in systems administration.

Key Components
Part 1: Manual User and Group Management
Goal: Learn and practice creating, managing, and removing Linux user accounts and groups using commands like adduser, deluser, and manual edits to /etc/group.
Tasks:
Create users user01, user02, and user03 with unique credentials and metadata.
Test user accounts using SSH and confirm their details in /etc/passwd.
Create and manage groups group01 and group02, assigning users to groups both programmatically and via manual file edits.
Delete user03 and clean up their home directory.
Part 2: Automating User and Group Management with Python
Goal: Automate the creation of users and groups using a Python script (create-users.py), which reads data from a structured input file.
Tasks:
Develop a Python script that uses the adduser command to create users and assigns them to specified groups.
Handle edge cases, such as malformed input or missing data.
Sync the script and associated files to GitHub with clear documentation.
Requirements
Hardware
Ubuntu 24.04 Virtual Machine (fresh installation recommended)
Host system capable of running VirtualBox or another hypervisor
Software
Python 3
Git (for version control)
SSH client for user testing
Repository Files
create-users.py: Python script to automate user and group creation.
create-users.input: Input file with a list of users and groups to be created.
README.md: Documentation for repository setup, usage, and operation.
How to Run
Part 1: Manual User Management
Create and Manage Users
Use commands like adduser and deluser to create and delete user accounts:

  
      
sudo adduser user01
sudo deluser user03 --remove-home
Assign Groups
Use adduser to assign users to groups, or manually edit /etc/group:

  
      
sudo adduser user01 group01
sudo nano /etc/group
Test User Accounts
Test user logins using SSH and verify user information:

  
      
ssh user01@localhost
grep user01 /etc/passwd
Part 2: Python Automation
Set Up Repository Clone the repository containing the Python script:

  
      
git clone <repository-url>
cd inet_4031_adduser_script
Prepare Input File
Create or edit the create-users.input file with user details in the following format:

ruby
      
username:password:LastName:FirstName:Groups
Run the Script
Execute the Python script with the input file:

  
      
sudo ./create-users.py < create-users.input
Verify Automation
Confirm that users and groups have been correctly created:

  
      
grep user0 /etc/passwd
grep user0 /etc/group
Sync Code with GitHub
Ensure your repository is updated and contains the following files:

create-users.py
create-users.input
README.md Push the changes to GitHub:
  
      
git add .
git commit -m "Automated user management script and input file"
git push origin main
Notes
Input File Format: Ensure all user details follow the colon-delimited structure in create-users.input.
Use # to comment out lines for skipping users.
Script Execution: Use chmod +x to make the Python script executable.
Password Hashing: Use openssl passwd -6 to generate hashed passwords for secure user account creation.

