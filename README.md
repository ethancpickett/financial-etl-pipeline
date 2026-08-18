# Automated Financial ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-orange)
![SQL](https://img.shields.io/badge/SQL-MySQL%20Workbench-lightgrey)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

An enterprise-grade, modular Extract, Transform, Load (ETL) pipeline engineered to ingest raw, unstandardized financial and transactional data from multi-source systems (CRMs, ERPs, and banking APIs), perform rigorous data quality audits, and load structured records into a secure relational data warehouse.

---

##  Project Motivation & Business Impact
In financial operations and data analytics, raw data is rarely pristine. Inconsistent string formats, missing transaction amounts, and disparate schemas routinely introduce reporting errors that compromise executive decision-making. 

This project bridges domain-specific financial compliance with modern data engineering by automating the entire data cleansing and loading lifecycle. By eliminating manual data wrangling and enforcing strict data integrity rules, this pipeline ensures **100% audit-readiness** and cuts data preparation time significantly.

---

##  Tech Stack
* **Language:** Python (Pandas, SQLAlchemy)
* **Database & Querying:** MySQL Workbench, Relational Database Schemas
* **Logging & Error Handling:** Python `logging` module with structured exception management
* **Architecture:** Modular, separation-of-concerns design pattern (`extract`, `transform`, `load`, and orchestrator `main.py`)

---

##  Project Architecture
```text
financial-etl-pipeline/
│
├── data/
│   ├── raw/                 # Unprocessed multi-source transaction exports
│   └── processed/           # Cleaned and validated staging datasets
│
├── src/
│   ├── __init__.py
│   ├── extract.py           # Multi-source data ingestion routines
│   ├── transform.py         # Data normalization, cleaning, and anomaly removal
│   └── load.py              # Database connection manager and batch loader
│
├── sql/
│   └── schema.sql           # Database initialization and table definitions
│
├── main.py                  # Pipeline orchestrator
└── README.md
