
# 🛡️ Informe de Incidente de Seguridad

## 1. Resumen

**Tipo de Incidente:** Intentos de acceso no autorizado y simulación de inyección SQL  
**Fecha de Detección:** 11 al 12 de mayo de 2025  
**Método de Detección:** Revisión manual de logs + captura de paquetes TCP (tcpdump)  
**Sistema Objetivo:** Aplicación web Flask en Raspberry Pi  
**Severidad:** Media  
**Estado:** Analizado y contenido

---

## 2. Contexto y Entorno

- **IP del Servidor Objetivo:** 192.168.1.78 (Raspberry Pi)
- **IP del Atacante:** 192.168.1.24 (Parrot OS Linux)  
- **Aplicación:** Servidor Flask con endpoints `/login` y `/register`  
- **Base de Datos:** SQLite3 (`clients.db`)  
- **Archivo de Captura:** `incident_report.pcap`  

---

## 3. Línea de Tiempo de Eventos

| Hora (UTC)           | Descripción del Evento                    |
|----------------------|--------------------------------------------|
| 2025-05-12 00:42:20  | Intento de login fallido con usuario: `admin`        |
| 2025-05-12 00:42:37  | Intento de login fallido con usuario: `root`         |
| 2025-05-12 00:42:58  | Intento de login fallido con usuario: `test`         |
| 2025-05-12 00:43:16  | Intento de login fallido con usuario: `asd`          |
| 2025-05-12 00:43:30  | Reintento fallido con usuario: `test`                |
| 2025-05-12 00:43:49  | Reintento fallido con usuario: `root`                |
| 2025-05-12 00:44:02  | Intento de inyección SQL: `' OR '1'='1`              |
| 2025-05-12 00:44:11  | Intento de inyección SQL: `admin'--`                |
| 2025-05-12 00:45:08  | Registro de nuevo usuario: `test`                   |
| 2025-05-12 00:45:19  | Login exitoso como `test`                           |

---

## 4. Evidencia Recopilada

### A. Registros extraídos de `clients.db`
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

### B. Captura de Paquetes (`incident_report.pcap`)
- Tráfico capturado incluye:
  - Escaneo TCP tipo SYN (realizado con Nmap)
  - Peticiones HTTP POST a `/login` y `/register`
  - Payloads de inyección SQL

### C. Comandos Nmap Utilizados
```bash
nmap -sS -p- -Pn 192.168.1.78
nmap -sV 192.168.1.78
```

---

## 5. Análisis de la Causa Raíz

- La aplicación aceptaba directamente entradas SQL sin sanitizar (vulnerabilidad simulada)
- No había protección contra fuerza bruta en login
- El servidor Flask estaba expuesto directamente en el puerto 5000, sin proxy ni firewall

---

## 6. Acciones de Mitigación

- Se cerró el acceso directo al puerto 5000
- Se configuró un proxy reverso con Nginx
- Se implementaron consultas SQL parametrizadas
- Plan a futuro: agregar fail2ban y alertas automáticas

---

## 7. Recomendaciones

- No exponer servidores Flask en modo desarrollo a la red
- Utilizar proxy reverso (Nginx) con TLS y filtros
- Aplicar validación de entradas y uso de ORM o SQL seguro
- Monitorear logs en tiempo real y alertar ante comportamientos sospechosos

---

## 8. Evidencia Visual (Capturada con Wireshark)

### 8.1 Escaneo SYN
![Escaneo SYN](report/syn_scan.png)

### 8.2 Respuestas SYN/ACK
![Respuestas SYN/ACK](report/syn_ack_responses.png)

### 8.3 Peticiones HTTP POST con SQLi
![Peticiones POST](report/http_post_login.png)

### 8.4 Vista general del tráfico TCP
![Tráfico TCP completo](report/full_traffic_overview.png)

---

## 9. Analista

**Nombre:** Nicolás Gentile  
**Rol:** Analista SOC (Simulación de Incidente)  
**Email:** [your_email@domain.com]  
**Fecha:** 12 de mayo de 2025
