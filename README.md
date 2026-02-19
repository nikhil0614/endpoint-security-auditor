# 🔐 Endpoint Security Auditor

A lightweight Linux endpoint security auditing tool that performs baseline system hardening checks and generates a structured PDF security report.

This project combines:

- 🖥️ Bash scripting for security configuration checks  
- 📄 Python automation for PDF report generation  

---

## 📌 Overview

The Endpoint Security Auditor performs basic security assessments on a Linux system to detect common misconfigurations and security weaknesses.

It checks:

- SSH root login configuration  
- World-writable files  
- Sudo privilege misuse  
- Kernel security parameters  
- Failed login attempts  

The results can be reviewed in the terminal and formatted into a professional PDF report.

---

## 🏗️ Project Structure

```
endpoint-security-auditor/
│
├── auditor.sh              # Bash security audit script
├── report_generator.py     # Python PDF report generator
├── audit_report.pdf        # Generated report (after execution)
└── README.md
```

---

## ⚙️ Features

### 1️⃣ SSH Root Login Check
Verifies whether `PermitRootLogin` is properly configured in:

```
/etc/ssh/sshd_config
```

If root login is enabled, it may pose a security risk.

---

### 2️⃣ World-Writable File Detection
Scans the entire filesystem for files with global write permissions:

```bash
find / -type f -perm -0002
```

World-writable files can allow unauthorized modification.

---

### 3️⃣ Sudo Privilege Audit
Checks `/etc/sudoers` (excluding comments) to identify potentially excessive privilege assignments:

```bash
grep -v '^#' /etc/sudoers
```

---

### 4️⃣ Kernel Parameter Verification
Validates important kernel settings such as core dump configuration:

```bash
sysctl -a | grep core_pattern
```

Misconfigured kernel parameters may expose sensitive data.

---

### 5️⃣ Failed Login Monitoring
Scans authentication logs for failed login attempts (possible brute-force activity):

```bash
grep "Failed password" /var/log/auth.log
```

---

## 🧪 Requirements

### System Requirements
- Linux OS (Ubuntu / Kali / CentOS recommended)
- Root privileges for full scan

### Python Requirements
- Python 3.x
- `fpdf` library

Install dependency:

```bash
pip install fpdf
```

---

## 🚀 Usage

### Step 1: Run Security Audit Script

Make the script executable:

```bash
chmod +x auditor.sh
```

Run the script with root privileges:

```bash
sudo ./auditor.sh
```

This will display audit findings in the terminal.

---

### Step 2: Generate PDF Report

Run:

```bash
python3 report_generator.py
```

This will generate:

```
audit_report.pdf
```

---

## 📄 Example Report Output

```
Endpoint Security Report

Check: Root Login Disabled
Status: Pass

Check: No World-Writable Files
Status: Fail

Check: Sudoers File Misuse
Status: Pass

Check: Kernel Parameters
Status: Pass

Check: Failed Login Attempts
Status: Fail
```

---

## 🛡️ Security Use Cases

- Baseline system hardening validation  
- Cybersecurity lab practice  
- Pre-deployment server checks  
- Blue team skill development  
- Academic security projects  

---

## ⚠️ Limitations

- Not a vulnerability scanner  
- Does not detect CVEs  
- Requires manual review of some outputs  
- No automated severity scoring  
- Designed for learning and baseline auditing  

---

## 🔮 Future Improvements

Potential upgrades:

- CIS Benchmark integration  
- Automated PASS/FAIL detection logic  
- JSON-based structured logging  
- Severity classification (Low / Medium / High)  
- Email alerts  
- Cron-based scheduled scans  
- SIEM integration  
- Colorized CLI output  
- Advanced log parsing with regex scoring  
- HTML report generation  

---

## 📚 Educational Value

This project demonstrates:

- Linux security auditing fundamentals  
- Bash scripting for system inspection  
- Log analysis basics  
- Privilege auditing techniques  
- Python automation  
- PDF report generation  

---

## 👨‍💻 Author

Developed by cybersecurity and ethical hacking club sac