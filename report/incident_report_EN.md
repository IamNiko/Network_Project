
# 🛡️ Security Incident Report

## 1. Summary

**Incident Type:** Unauthorized login attempts and SQL Injection simulation  
**Date Detected:** 2025-05-11 to 2025-05-12  
**Detection Method:** Manual log review + TCP packet capture (tcpdump)  
**Target System:** Flask web application on Raspberry Pi  
**Severity:** Medium  
**Status:** Analyzed and contained

---

## 2. Context and Environment

- **Target Host IP:** 192.168.1.78 (Raspberry Pi)
- **Attacker Host IP:** 192.168.1.24 (Parrot OS Linux)  
- **Application:** Flask web app exposing `/login` and `/register`  
- **Database:** SQLite3 (`clients.db`)  
- **Capture File:** `incident_report.pcap`  

---

## 3. Timeline of Events

| Time (UTC)       | Event Description                         |
|------------------|--------------------------------------------|
| 2025-05-12 00:42:20 | Failed login with username: `admin`        |
| 2025-05-12 00:42:37 | Failed login with username: `root`         |
| 2025-05-12 00:42:58 | Failed login with username: `test`         |
| 2025-05-12 00:43:16 | Failed login with username: `asd`          |
| 2025-05-12 00:43:30 | Failed login with username: `test`         |
| 2025-05-12 00:43:49 | Failed login with username: `root`         |
| 2025-05-12 00:44:02 | SQLi attempt: `' OR '1'='1`                |
| 2025-05-12 00:44:11 | SQLi attempt: `admin'--`                  |
| 2025-05-12 00:45:08 | User `test` registered                    |
| 2025-05-12 00:45:19 | Login successful as `test`               |

---

## 4. Evidence Collected

### A. Logs from `clients.db`
```
Fail    admin         192.168.1.24    2025-05-12 00:42:20
Fail    root          192.168.1.24    2025-05-12 00:42:37
Fail    test          192.168.1.24    2025-05-12 00:42:58
Fail    asd           192.168.1.24    2025-05-12 00:43:16
Fail    test          192.168.1.24    2025-05-12 00:43:30
Fail    root          192.168.1.24    2025-05-12 00:43:49
Fail    ' OR '1'='1   192.168.1.24    2025-05-12 00:44:02
Fail    admin'--      192.168.1.24    2025-05-12 00:44:11
register test         192.168.1.24    2025-05-12 00:45:08
login    test         192.168.1.24    2025-05-12 00:45:19
```

### B. Packet Capture
- File: `incident_report.pcap`
- Captured traffic includes:
  - TCP SYN scan (Nmap)
  - HTTP POST login and registration attempts
  - SQLi payloads

### C. Nmap Commands Executed
```bash
nmap -sS -p- -Pn 192.168.1.78
nmap -sV 192.168.1.78
```

---

## 5. Root Cause Analysis

- Application accepted unsanitized SQL input (simulated vulnerability)
- No protection against brute-force login attempts
- Flask server exposed on port 5000 without reverse proxy or firewall

---

## 6. Mitigation Actions

- Closed direct access to port 5000
- Added Nginx reverse proxy for frontend routing
- Parameterized SQL queries implemented
- Future: add fail2ban-style protection and alerting

---

## 7. Recommendations

- Do not expose Flask dev server to the network
- Use reverse proxy (Nginx) with TLS
- Apply input validation and use ORM or parameterized queries
- Monitor logs and alert on suspicious activity

---

## 8. Visual Evidence (Captured with Wireshark)

### 8.1 SYN Scan
![SYN Scan](report/syn_scan.png)

### 8.2 SYN/ACK Responses
![SYN/ACK Responses](report/syn_ack_responses.png)

### 8.3 HTTP POST Login & SQLi Attempts
![POST Requests](report/http_post_login.png)

### 8.4 Full TCP Flow Overview
![Traffic Overview](report/full_traffic_overview.png)

---

## 9. Analyst

**Name:** Nicolás Gentile  
**Role:** SOC Analyst (Simulated Incident Response)  
**Email:** [your_email@domain.com]  
**Date:** 2025-05-12
