# Ransomware Detection and Mitigation System

## Overview

The Ransomware Detection and Mitigation System is a Python-based endpoint security project designed to detect, contain, and recover from ransomware-style attacks in real time.

Modern ransomware attacks can encrypt hundreds of files within seconds, causing significant operational disruption and financial loss. This project demonstrates how endpoint monitoring, behavioural analysis, automated response mechanisms, and backup restoration can work together to minimize damage and improve incident response times.

The system continuously monitors file system activity and identifies suspicious behaviour patterns commonly associated with ransomware, including rapid file modifications, mass file creation, abnormal file renaming operations, and unauthorized changes to protected directories. Upon detection, the system automatically generates alerts, isolates suspicious files, records forensic logs, and restores clean backups.

This project simulates the workflow of a modern Endpoint Detection and Response (EDR) platform and provides hands-on experience with security monitoring, incident response automation, threat detection engineering, and cyber defence techniques.

---

## Problem Statement

Ransomware remains one of the most damaging forms of cybercrime worldwide. Traditional signature-based antivirus solutions may struggle to detect new ransomware variants, especially zero-day threats.

The objective of this project is to develop a lightweight behavioural detection system capable of:

* Monitoring file system activities in real time.
* Detecting ransomware-like behaviour within seconds.
* Automatically responding to suspicious activity.
* Preventing data loss through backup restoration.
* Generating alerts and forensic logs for security analysts.

---

## Key Features

### Real-Time File System Monitoring

The system continuously monitors designated directories using file system event handlers and tracks:

* File modifications
* File creations
* File deletions
* File renaming activities
* Directory changes

---

### Behaviour-Based Detection Engine

Instead of relying solely on known malware signatures, the system analyses behavioural indicators such as:

* High-volume file modifications in a short period
* Mass file encryption patterns
* Rapid file renaming events
* Creation of suspicious file extensions
* Abnormal file access frequency

This approach allows the system to identify previously unseen ransomware variants.

---

### Automated Alerting

When suspicious activity exceeds predefined thresholds, the system immediately generates alerts.

Supported alert methods include:

* Console notifications
* Desktop notifications
* Log file entries
* Future email integration

---

### File Isolation and Quarantine

Detected malicious files can be automatically moved into a quarantine environment to prevent further execution or propagation.

Benefits include:

* Reduced attack impact
* Evidence preservation
* Faster incident containment

---

### Backup Restoration

To simulate business continuity operations, the project includes an automated recovery mechanism that restores clean backups of affected files.

This process helps demonstrate:

* Disaster recovery procedures
* Incident response workflows
* Data protection strategies

---

### Logging and Forensics

The system records all security events for future investigation.

Logged information includes:

* Timestamp
* Event type
* File path
* Detection results
* Response actions

These logs can be used by security analysts during post-incident investigations.

---

## System Architecture

```text
File Activity
      │
      ▼
Real-Time Monitoring Engine
      │
      ▼
Behaviour Analysis Engine
      │
      ▼
Detection Decision
      │
 ┌────┼────┐
 ▼    ▼    ▼
Alert Quarantine Backup Restore
      │
      ▼
Security Logs
```

---

## Project Structure

```text
Ransomware-Detection-System/

├── main.py
├── monitor.py
├── detector.py
├── responder.py
├── backup_restore.py
├── alert.py
├── logger.py
├── requirements.txt
├── README.md

├── backups/
├── quarantine/
├── logs/
├── test_files/
└── screenshots/
```

---

## Technologies Used

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| Python     | Core development language        |
| Watchdog   | File system monitoring           |
| Psutil     | System activity monitoring       |
| Plyer      | Alert notifications              |
| Logging    | Event recording                  |
| VirtualBox | Safe malware testing environment |
| Git        | Version control                  |
| GitHub     | Project hosting                  |

---

## Detection Workflow

1. Monitor file system activity.
2. Count file modifications and rename operations.
3. Compare activity against behavioural thresholds.
4. Generate security alerts upon detection.
5. Quarantine suspicious files.
6. Restore clean backups.
7. Record forensic logs.
8. Continue monitoring.

---

## Testing Environment

All testing was performed in an isolated virtual machine environment to ensure safe execution and containment of simulated ransomware behaviour.

Environment:

* VirtualBox
* Windows Test VM
* Ubuntu Test VM
* Python 3.x

No production systems were used during testing.

---

## Experimental Results

| Metric                        | Result      |
| ----------------------------- | ----------- |
| Detection Time                | 2–3 Seconds |
| Detection Accuracy            | 94%         |
| Ransomware Families Simulated | 5           |
| Data Loss                     | 0%          |
| Recovery Success Rate         | 100%        |

The system successfully detected ransomware-like behaviour across multiple test scenarios while restoring affected files without data loss.

---

## Security Considerations

This project was created for educational and defensive cybersecurity purposes only.

The project does not contain malicious code and should never be used to deploy, distribute, or execute ransomware on unauthorized systems.

All testing should be conducted inside isolated virtual environments.

---

## Future Improvements

Future versions may include:

### Machine Learning Detection

Implement anomaly detection models capable of identifying previously unseen ransomware behaviours.

### SIEM Integration

Forward alerts to platforms such as:

* Splunk
* ELK Stack
* Microsoft Sentinel

### Threat Intelligence Integration

Enrich alerts using threat intelligence feeds and Indicators of Compromise (IOCs).

### Web Dashboard

Develop a real-time dashboard displaying:

* Active alerts
* Detection statistics
* Incident timelines
* System health

### Cloud Backup Support

Support backup restoration through:

* AWS S3
* Azure Blob Storage
* Google Cloud Storage

### SOC Integration

Generate alerts in formats compatible with Security Operations Centre workflows and ticketing systems.

---

## Learning Outcomes

This project demonstrates practical knowledge in:

* Endpoint Detection and Response (EDR)
* Security Monitoring
* Incident Response
* Malware Analysis Concepts
* Threat Detection Engineering
* Digital Forensics Logging
* Python Automation
* Defensive Cybersecurity

---

## Author

**Vishesh Nagdev**  
Master of IT (Cybersecurity) — Macquarie University, Sydney  
[LinkedIn](www.linkedin.com/in/vishesh-nagdev) | [Email](mailto:visheshnagdev210@gmail.com)
