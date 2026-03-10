# SentryClaw 🛡️
**A Zero-Trust Supervisor for OpenClaw.**

SentryClaw acts as a mandatory "Governor" for agents like OpenClaw. It intercepts all outbound communications, scans for sensitive information (PII, API Keys, Proprietary Data), and ensures that no sensitive payload is transmitted over unencrypted channels.

## Core Features
- **Semantic PII Detection:** Uses NLP to identify sensitive context beyond simple regex.
- **Protocol Enforcement:** Blocks outbound `http` requests containing sensitive data, forcing `https` or GPG encryption.
- **Human-in-the-Loop (HITL) Trigger:** Pauses execution for high-risk data exfiltration attempts.
- **Audit Logging:** Maintains a tamper-proof record of all blocked and redacted attempts.
