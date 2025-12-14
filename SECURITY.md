# Security Policy

## Supported Versions
We provide security updates for the following versions:

| Version | Supported          |
|---------|--------------------|
| 1.x     | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability
If you discover a security vulnerability in FinAI Trader, please report it responsibly. Do not disclose the issue publicly until we've had a chance to address it.

### How to Report
- Email us at security@finai.com with details.
- Include: Description, steps to reproduce, affected versions, and potential impact.
- Use PGP encryption if possible (public key available on request).

### Response Process
- We will acknowledge your report within 48 hours.
- We'll investigate and provide updates every 7 days.
- If confirmed, we'll patch it in the next release and credit you (if desired).
- For critical issues, we may issue a hotfix.

## Best Practices
- Use secure API keys and store them in `.env` (never commit secrets).
- Enable 2FA on GitHub and connected services (e.g., Stripe, Binance).
- Run security scans via GitHub Actions (`security-scan.yml`).
- Monitor dependencies with Dependabot.

We appreciate your help in keeping FinAI Trader secure!
