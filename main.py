import csv
import sqlite3
from pathlib import Path

def run(path='data/claims.csv'):
    db=sqlite3.connect(':memory:')
    db.executescript(Path('sql/schema.sql').read_text())
    with open(path,newline='') as f: rows=list(csv.DictReader(f))
    for r in rows:
        db.execute('INSERT OR IGNORE INTO dim_provider VALUES (?,?)',(r['provider_id'],r['provider_name']))
        db.execute('INSERT OR IGNORE INTO dim_service VALUES (?,?)',(r['service_code'],r['service_name']))
        db.execute('INSERT INTO fact_claim VALUES (?,?,?,?,?)',(r['claim_id'],r['member_id'],r['provider_id'],r['service_code'],float(r['paid_amount'])))
    result=db.execute('SELECT p.provider_name, ROUND(SUM(f.paid_amount),2) FROM fact_claim f JOIN dim_provider p ON f.provider_id=p.provider_id GROUP BY 1 ORDER BY 1').fetchall()
    return {'claims_loaded':len(rows),'provider_paid_totals':dict(result)}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
