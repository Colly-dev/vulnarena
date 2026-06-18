# ⚠️ CRITICAL SECURITY WARNING ⚠️

**VulnArena is an INTENTIONALLY VULNERABLE web application lab.**

> **DO NOT** deploy this application on public-facing servers.
> **DO NOT** expose it to the internet.
> **DO NOT** use it in production environments.
> **DO NOT** connect it to real data or systems.

This project is designed **SOLELY** for security education, penetration testing practice, and AppSec research in isolated environments. By using this software, you accept full responsibility for your actions and agree to use it ethically and legally.

---

## 🚀 Project Overview

**VulnArena** is a comprehensive, portfolio-ready cybersecurity project featuring a deliberately vulnerable Flask and PHP web application lab. It is designed to demonstrate common web vulnerabilities and their corresponding secure remediations.

### 🎯 Core Objectives
- Provide a hands-on environment for practicing manual and automated pentesting.
- Demonstrate the "Before vs. After" of application security.
- Showcase offensive security workflows and reporting.

---

## 📸 Screenshots

*(Screenshots can be found in `docs/screenshots/` after running the lab)*

1. **Lab Startup Banner**
2. **Vulnerable Login Page**
3. **SQL Injection Demonstration**
4. **XSS Payload Execution**
5. **Admin Panel Bypass**

---

## 🏗️ Architecture

The lab consists of multiple components orchestrated via Docker:
- **Flask App**: Modern Python web framework with various vulnerabilities.
- **PHP App**: Classic PHP vulnerabilities including SQLi and File Upload.
- **MySQL**: Shared database for both applications.
- **Nginx**: Web server for the PHP application.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask), PHP 8.1
- **Database**: MySQL, SQLAlchemy
- **Containerization**: Docker, Docker Compose
- **Testing/Security**: Pytest, Requests, BeautifulSoup4

---

## 🛡️ Implemented Vulnerabilities
| Vulnerability | Description | Secure Version |
| :--- | :--- | :--- |
| **SQL Injection** | Auth bypass & UNION-based | Parameterized Queries |
| **XSS** | Reflected & DOM-based | Output Encoding & CSP |
| **CSRF** | Email change bypass | Anti-CSRF Tokens |
| **SSRF** | Internal metadata access | Input Validation/Allowlisting |
| **IDOR** | User data enumeration | Proper AuthZ Checks |
| **Insecure Upload** | Arbitrary file upload | Extension Filtering |

---

## ⚙️ Installation & Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.10+ (for local scripts)

### Quick Start
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vulnarena
   ```
2. Start the lab:
   ```bash
   bash automation/startup/start_lab.sh
   ```
3. Access the apps:
   - Flask: [http://localhost:5000](http://localhost:5000)
   - PHP: [http://localhost:8080](http://localhost:8080)

---

## 🧪 Running Tests
```bash
pytest tests/
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
