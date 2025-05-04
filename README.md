
# Shodan Project: nginx Fingerprinting & Version Risk Audit

# Description:
This project uses Shodan to identify nginx web servers, fingerprint their versions, and assess associated risks using public vulnerability databases.

## Focus:
- Shodan query: product:nginx http.title:"Welcome"
- Detection of default configuration pages
- Version mapping to CVEs
- Risk summary and hardening recommendations
