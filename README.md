User Authentication and Access Control System Prototype for Finvest Holdings
Project Overview
This project involves designing and implementing a user authentication and access control system prototype for Finvest Holdings, a company specializing in financial planning and investment banking. The prototype aims to enhance the security of their proprietary financial software and data systems by implementing robust access control mechanisms and password policies.

Table of Contents
Project Overview
Features
Access Control Policy
Password Policy
Technologies Used
Installation
Usage
Testing
Contributors
License
Features
Role-Based Access Control (RBAC): Ensures appropriate permissions and access rights for different user roles.
Proactive Password Checker: Enforces a robust password policy to enhance system security.
Secure Password File Management: Utilizes salted hashing techniques to safeguard user credentials.
User Interface: Simple and effective interfaces for user enrolment and login.
Extensive Testing: Validated functionality and security of the prototype.
Access Control Policy
Clients: Can view their account balance, investment portfolio, and contact details of their Financial Advisor.
Premium Clients: Can modify their investment portfolio and view the contact details of their Financial Planner and Investment Analyst.
Employees (except Technical Support): Can view a client's account balance and investment portfolio.
Financial Planners: Can view money market instruments.
Financial Advisors and Financial Planners: Can view private consumer instruments.
Investment Analysts: Can view money market instruments, derivatives trading, interest instruments, and private consumer instruments.
Technical Support: Can view a client's information and request client account access for troubleshooting.
Tellers: Can only access the system during business hours (9:00 AM to 5:00 PM).
Compliance Officers: Can validate modifications to investment portfolios.
Password Policy
Passwords must be 8-12 characters in length.
Must include at least one upper-case letter, one lower-case letter, one numerical digit, and one special character (!, @, #, $, %, ?, *).
Common weak passwords and passwords matching the format of common numbers or user IDs are prohibited.
Technologies Used
Programming Languages: Python, C
Security Libraries: Python Cryptographic Services, C OpenSSL Library
Access Control Models: Role-Based Access Control (RBAC)
Development Tools: Virtual Machine (VM) environment
Installation
Clone the Repository:
sh
Copy code
git clone https://github.com/yourusername/finvest-auth-access-control.git
Navigate to the Project Directory:
sh
Copy code
cd finvest-auth-access-control
Set Up the Virtual Machine: Follow the instructions provided in the VM setup guide (Module 1 Assignment).
Usage
User Enrolment:

Run the enrolment script to add new users to the system.
Enter the required information (user ID, password, etc.).
The proactive password checker will validate the password based on the defined policy.
Successful enrolment will add the user to the password file.
User Login:

Run the login script.
Enter your user ID and password.
Upon successful authentication, the system will display the operations the user is authorized to perform.
Testing
Access Control Mechanism:

Implemented and tested using predefined roles and permissions.
Verified that users can only access the resources and perform the actions specified in the access control policy.
Password File Management:

Implemented salted hashing for password storage.
Tested the loading and verification of passwords to ensure correctness and security.
Proactive Password Checker:

Designed to enforce the password policy during user enrolment.
Tested with various passwords to ensure compliance with the policy.
Contributors
Your Name - Lead Developer
