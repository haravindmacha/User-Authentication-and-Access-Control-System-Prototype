# User Authentication and Access Control System Prototype for Finvest Holdings

## Project Overview

This project involves designing and implementing a user authentication and access control system prototype for Finvest Holdings, a company specializing in financial planning and investment banking. The prototype aims to enhance the security of their proprietary financial software and data systems by implementing robust access control mechanisms and password policies.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Access Control Policy](#access-control-policy)
- [Password Policy](#password-policy)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributors](#contributors)
- [License](#license)

## Features

- **Role-Based Access Control (RBAC):** Ensures appropriate permissions and access rights for different user roles.
- **Proactive Password Checker:** Enforces a robust password policy to enhance system security.
- **Secure Password File Management:** Utilizes salted hashing techniques to safeguard user credentials.
- **User Interface:** Simple and effective interfaces for user enrolment and login.
- **Extensive Testing:** Validated functionality and security of the prototype.

## Access Control Policy

1. **Clients:** Can view their account balance, investment portfolio, and contact details of their Financial Advisor.
2. **Premium Clients:** Can modify their investment portfolio and view the contact details of their Financial Planner and Investment Analyst.
3. **Employees (except Technical Support):** Can view a client's account balance and investment portfolio.
4. **Financial Planners:** Can view money market instruments.
5. **Financial Advisors and Financial Planners:** Can view private consumer instruments.
6. **Investment Analysts:** Can view money market instruments, derivatives trading, interest instruments, and private consumer instruments.
7. **Technical Support:** Can view a client's information and request client account access for troubleshooting.
8. **Tellers:** Can only access the system during business hours (9:00 AM to 5:00 PM).
9. **Compliance Officers:** Can validate modifications to investment portfolios.

## Password Policy

- Passwords must be 8-12 characters in length.
- Must include at least one upper-case letter, one lower-case letter, one numerical digit, and one special character (!, @, #, $, %, ?, *).
- Common weak passwords and passwords matching the format of common numbers or user IDs are prohibited.

## Technologies Used

- **Programming Languages:** Python, C
- **Security Libraries:** Python Cryptographic Services, C OpenSSL Library
- **Access Control Models:** Role-Based Access Control (RBAC)
- **Development Tools:** Virtual Machine (VM) environment

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/finvest-auth-access-control.git
