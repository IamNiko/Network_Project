# 🕵️‍♂️ Network Incident Simulation — Simulación de Incidente de Red

Este proyecto es una simulación real de un incidente de ciberseguridad sobre un servidor Flask ejecutado en una Raspberry Pi, con tráfico capturado y analizado profesionalmente.

This project simulates a real-world cyber incident against a Flask server hosted on a Raspberry Pi. The traffic was captured and analyzed as part of a SOC-style report.

---

## 🇪🇸 Descripción en Español

### 🎯 Objetivo
Simular un escenario de ataque típico: escaneo con Nmap, fuerza bruta, SQLi, y login válido. Registrar logs y tráfico con `tcpdump`, y documentar todo el análisis en un informe SOC.

### 🛠️ Tecnologías usadas
- Python + Flask
- SQLite3
- Wireshark
- Nmap
- curl
- tcpdump
- Git y GitHub

### 🗂️ Estructura del proyecto
```
/report/                    ← Informe completo del incidente
  ├── incident_report.md
  ├── incident_report_ES.md
  ├── incident_report_EN.md
  └── *.png                 ← Capturas de pantalla desde Wireshark
/templates/, /static/       ← Archivos web del servidor Flask
/init_db.py, /app.py        ← Código backend
```

### 📖 Cómo correr el servidor
```bash
python init_db.py
python app.py
```

### 📎 Informe del incidente
Ver el informe completo y las capturas en la carpeta [`report/`](report/).

---

## 🇺🇸 English Description

### 🎯 Goal
Simulate a common attack pattern: Nmap scan, brute force, SQL injection, and valid login. Capture traffic using `tcpdump`, store logs in SQLite3, and produce a full SOC-style incident report.

### 🛠️ Tech Stack
- Python + Flask
- SQLite3
- Wireshark
- Nmap
- curl
- tcpdump
- Git & GitHub

### 🗂️ Project Structure
```
/report/                    ← Full incident report and visual evidence
  ├── incident_report.md
  ├── incident_report_ES.md
  ├── incident_report_EN.md
  └── *.png                 ← Wireshark screenshots
/templates/, /static/       ← Flask web files
/init_db.py, /app.py        ← Backend code
```

### 📖 Run the Server
```bash
python init_db.py
python app.py
```

### 📎 Incident Report
See the full report and screenshots in the [`report/`](report/) folder.

---

## 🧠 Autor / Author

**Nicolás Gentile**  
SOC & Cybersecurity Analyst in training  
GitHub: [IamNiko](https://github.com/IamNiko)
