# 🧛 Hydra’s Fang – Brute Force Attack Simulator

Hydra’s Fang is a Python-based brute-force simulator designed for educational use. It demonstrates how attackers exploit weak credentials and emphasizes the importance of secure authentication.

## Features
- Command-line interface
- ASCII art branding
- Ethical disclaimer prompt
- Response-based success detection
- Modular wordlists

## How to Run
```bash
pip install requests colorama
python hydra.py --url http://example.com/login --userlist wordlists/usernames.txt --passlist wordlists/passwords.txt