# Healthcare Claims Dimensional Warehouse

Builds a local claims star schema with member, provider, and service dimensions plus a claims fact table.  
Demonstrates reproducible joins and paid-amount reconciliation using synthetic, non-PHI encounters.

## Problem

Healthcare finance reporting requires auditable claim totals across provider and service dimensions.

## Solution and design

Initialize a normalized dimension/fact warehouse from synthetic rows and run tested provider aggregates.

**Stack:** SQL, SQLite, star schema, healthcare analytics

## Quick start

Requires Python 3.11+ (standard library only for the local demo).

```bash
python main.py
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same tests on pushes and pull requests.

## Project layout

- `main.py`: core processing and a small command-line demonstration
- `data/`, `seeds/`, `models/`, `sql/`, `infra/`, `dags/` or `powerbi/`: included only where relevant
- `tests/`: fixture-based expected-value and repeatability checks

## Engineering decisions

- Narrow scope, realistic field names, and synthetic reproducible inputs
- No credentials, customer records, patient data, API tokens, or paid cloud resources
- Visible business logic and deterministic fixtures rather than screenshots of unverifiable dashboards

## Limits and next iteration

All data is entirely synthetic. The warehouse demonstrates analytics modeling, not HIPAA certification or clinical decision support.

A production hardening path would add larger-scale fixtures, alerting, operational runbooks, robust error handling, and integration tests against the real deployment target.

## Portfolio integrity

This is an independently reproducible **portfolio demonstration**, not a claim that these files are employer code or that a cloud workload has been deployed. The fixture data is synthetic.
