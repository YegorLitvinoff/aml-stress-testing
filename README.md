# AML Stress Testing: Automated Compliance Simulation & Risk Logic Verification

## 📌 Business Case & Overview
Anti-Money Laundering (AML) system perimeters must remain resilient against evolving financial crime vectors. Static thresholds are constantly probed by bad actors utilizing transaction splitting, mule account networks, and rapid money routing. To guarantee complete system compliance, risk departments must pivot from manual rule auditing to proactive, automated system verification.

This project introduces an **Automated AML Stress-Testing Engine** written in Python designed to evaluate system defense mechanisms against complex simulated transaction attacks. By deploying daily scheduled pipelines, the framework evaluates current scoring rules and AML barriers, enabling security teams to catch systemic and operational compliance risks before they materialize.

## 🎯 Key Objectives
* **Proactive Risk Discovery:** Simulate multi-layered financial crime scenarios (e.g., structuring, smurfing, layered velocity spikes) to pressure-test database triggers.
* **Automated Daily Validation:** Establish end-to-end automated pipelines that run complex transaction arrays against active production rule profiles.
* **Scoring Logic Performance Audit:** Quantify how effectively current AML scoring algorithms isolate complex transactional anomalies under peak simulated volumes.

## 🛠️ Tech Stack & Architecture
* **Automation & Engine:** Python 3.10 (Pandas, NumPy for data manipulation; dynamic simulation scripting).
* **Testing Methods:** Boundary value testing, attack simulation vectors, transactional scenario modeling.
* **Data Structuring:** Configuration and operational metric tracking layers driven by automated JSON reporting artifacts.

## 📂 Project Structure
```text
├── automation/
│   └── run_daily_stress.py          # Master execution script automating the daily AML test run
├── requirements.txt                 # Environment dependencies
└── README.md                        # Project documentation
```

## 📊 Core Simulation Concepts
The stress-testing engine simulates high-risk patterns to verify AML logic:
1. **Structuring & Smurfing Attacks:** Breaking down a large, reportable sum into randomly timed transfers across multiple accounts to test boundary alert systems.
2. **Rapid Capital Draining (Velocity Scenarios):** Simulating sudden, concurrent cross-border transfers within narrow execution windows to evaluate speed-lock thresholds.
3. **Mule Account Layering:** Mimicking complex pass-through transfer chains where funds are passed across multiple entities instantly to audit graph-based detection paths and export the results into structured compliance audit reports (`daily_aml_stress_log.json`).

---
*Developed by Yegor Litvinov (Risk Data Analyst).*
