CREATE TABLE dim_provider(provider_id TEXT PRIMARY KEY, provider_name TEXT NOT NULL);
CREATE TABLE dim_service(service_code TEXT PRIMARY KEY, service_name TEXT NOT NULL);
CREATE TABLE fact_claim(claim_id TEXT PRIMARY KEY, member_id TEXT NOT NULL,provider_id TEXT REFERENCES dim_provider(provider_id),service_code TEXT REFERENCES dim_service(service_code), paid_amount REAL NOT NULL CHECK(paid_amount>=0));
