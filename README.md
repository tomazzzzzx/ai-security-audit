# AI Security Audit

AI model security auditing toolkit: adversarial robustness, data poisoning, model extraction, privacy leakage.

## Audit Suites
- **Adversarial Robustness**: PGD, C&W, AutoAttack
- **Data Poisoning**: Label flip, backdoor, dirty label detection
- **Model Extraction**: Membership inference, model inversion attacks
- **Privacy Leakage**: Differential privacy accounting

## Quick Start
```bash
python audit.py --model model.pt --suite robustness --report report.html
```

## Output
Generates detailed HTML report with severity scores, attack success rates, and remediation recommendations.

## License: MIT
