# VulnArena: Full-Stack Security Research & Pentest Laboratory

![Security](https://img.shields.io/badge/Security-Pentesting-red)
![Tech](https://img.shields.io/badge/Tech-Flask%20%7C%20PHP%20%7C%20Docker-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> [!CAUTION]
> **LEGAL & ETHICAL DISCLAIMER**
> This repository contains **intentionally vulnerable software**. It is designed strictly for educational purposes, security research, and penetration testing practice. **Never** deploy this application on public-facing servers or production environments. Unauthorized access to computer systems is illegal. Use this lab responsibly in isolated environments.

---

## 🛡️ Project Vision

**VulnArena** is a comprehensive, multi-stack web application laboratory designed to bridge the gap between theoretical security knowledge and practical application. By providing a "Before vs. After" perspective on critical vulnerabilities, this project serves as a robust platform for:

*   **Security Engineers** to analyze exploit patterns and develop robust mitigations.
*   **Penetration Testers** to hone manual exploitation and automation skills.
*   **Developers** to understand the root causes of common vulnerabilities like the OWASP Top 10.

## 🚀 Key Features

*   **Hybrid Architecture**: Combines a modern **Python/Flask** backend with a classic **PHP 8.1** environment to demonstrate vulnerability patterns across different tech stacks.
*   **Exploit-to-Remediation Mapping**: Every vulnerable endpoint is paired with a `secure_version` implementation, demonstrating industry-standard fixes (e.g., Parameterized Queries, CSP, Secure Session Management).
*   **Automated Security Workflows**: Includes custom Python-based attack scripts and wrappers for industry tools (sqlmap, ffuf) to demonstrate automated vulnerability validation.
*   **Containerized Orchestration**: Fully automated deployment using **Docker & Docker Compose**, ensuring a consistent, isolated, and reproducible lab environment.
*   **Integrated Reporting**: A built-in reporting engine that transforms raw pentest findings into professional, human-readable HTML reports.

## 🏗️ Technical Architecture

The lab is orchestrated as a microservices environment:

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend/API** | Flask, Jinja2, Bootstrap | Modern web interface & API vulnerabilities |
| **Legacy App** | PHP 8.1, Apache | Traditional web vulnerability patterns |
| **Database** | MySQL 8.0 | Centralized data store for both applications |
| **Security Layer** | SQLAlchemy, bcrypt | Implementation of secure remediations |
| **DevOps** | Docker, Bash | Environment isolation & automation |

## 🛡️ Vulnerability Coverage & Remediations

| Vulnerability Class | Lab Implementation | Professional Remediation |
| :--- | :--- | :--- |
| **Injection** | SQLi (Auth Bypass, UNION-based) | Parameterized Queries & ORM usage |
| **Broken Access Control** | IDOR (User Enum), Admin Bypass | Attribute-Based Access Control (ABAC) |
| **Cross-Site Scripting** | Reflected & DOM-based XSS | Context-aware Output Encoding & CSP |
| **Broken Auth** | Weak Session Mgmt, Plaintext Passwords | Bcrypt Hashing & Secure Cookie Attributes |
| **SSRF** | Internal Metadata Access | Strict URL Validation & Egress Filtering |
| **Insecure Uploads** | Arbitrary File Execution | MIME-type Validation & Filename Sanitization |

## 🛠️ Installation

### Prerequisites
*   **Python 3.12+**
*   **Docker & Docker Compose** (Required for database and PHP app orchestration)
*   **Git**

### Setup & OS-Specific Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/Colly-dev/vulnarena.git
cd vulnarena
```

#### 2. Create and Activate Virtual Environment
| Operating System | Command |
| :--- | :--- |
| **Windows (CMD)** | `python -m venv venv` <br> `venv\Scripts\activate` |
| **Windows (PowerShell)** | `python -m venv venv` <br> `.\venv\Scripts\Activate.ps1` |
| **Linux / macOS** | `python3 -m venv venv` <br> `source venv/bin/activate` |

#### 3. Install Dependencies
Regardless of your OS, once the virtual environment is activated, run:
```bash
pip install -r requirements.txt
```
*Note for Linux Users: You might need to install `python3-venv` first if it's not present: `sudo apt install python3-venv`.*

#### 4. Start Lab Services
To launch the integrated environment using Docker:
```bash
bash automation/startup/start_lab.sh
```
*Note: You must accept the security disclaimer to proceed. This will start the Flask app, PHP app, and MySQL database.*

## 📖 Usage

VulnArena provides a comprehensive CLI and web interface for security testing:

### Lab Management
*   **Start the Lab**: `python src/core/engine.py start`
*   **Stop the Lab**: `python src/core/engine.py stop`

### Automated Security Testing
*   **Run Full Test Suite**: `pytest tests/`
*   **Validate Vulnerabilities**: `python src/attacks/automated/vuln_validator.py`
*   **Execute SQLi Bypass**: `python src/vulnerabilities/sql_injection/auth_bypass.py`

### Access Points
*   **Flask Dashboard**: [http://localhost:5000](http://localhost:5000)
*   **PHP Lab Environment**: [http://localhost:8080](http://localhost:8080)
*   **MySQL Database**: `localhost:3306`

---
**Developed for the Security Community.**
If you find this project useful for your learning or research, feel free to contribute or reach out!
