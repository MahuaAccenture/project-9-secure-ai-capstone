# pip-audit CVE Comparison

| Severity | Unpinned Baseline | Hardened Pinned |
|---|---:|---:|
| Critical | 0 | 0 |
| High | 0 | 0 |
| Medium | 0 | 0 |
| Low | 0 | 0 |
| **Total** | **0** | **0** |

## Results

The baseline dependency scan and hardened pinned dependency scan
both reported zero known vulnerabilities.

The total CVE reduction was 0 because no known vulnerabilities
were detected in the baseline scan.

## Evidence

- Baseline scan: `pip_audit_before.json`
- Hardened scan: `pip_audit_after.json`

## Tools

pip-audit was used to audit the Python dependencies.
The hardened environment uses exact dependency versions
recorded in `requirements_pinned.txt`.
