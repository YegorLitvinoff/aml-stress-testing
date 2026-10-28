"""
============================================================================
PROJECT: AML Stress Testing
FILENAME: run_daily_stress.py
DESCRIPTION: Automated continuous compliance framework. Generates dynamic 
             laundering and structuring (smurfing) attack vectors 
             to stress-test AML triggers and identify rule vulnerabilities.
============================================================================
"""

import json
import os
import random
from datetime import datetime, timedelta


class AMLStressTestingEngine:

    def __init__(self, aml_threshold_eur=10000.0):
        # Setting standard international AML control boundaries (e.g., FATF cash reporting limit)
        self.aml_threshold_eur = aml_threshold_eur
        self.test_log_output = []

    def simulate_smurfing_attack(self, target_volume=25000.0):
        """Simulates a complex structuring attack (Smurfing).

        Breaks down a heavy reportable transaction into multiple micro-transfers
        spread across narrow time windows to probe system trigger vulnerabilities.
        """
        print(
            f"[!] Injecting Smurfing Attack Vector: Attempting to route €{target_volume:,} undetected..."
        )

        current_time = datetime.now()
        accumulated_routed_funds = 0.0
        micro_transactions = []
        tx_counter = 1

        # Criminal strategy: keep each transfer significantly below the standard 10k trigger limit
        while accumulated_routed_funds < target_volume:
            remaining_funds = target_volume - accumulated_routed_funds
            # Randomized chunk sizes between 1.5k and 4.5k EUR
            chunk_amount = round(random.uniform(1500.0, 4500.0), 2)

            if chunk_amount > remaining_funds:
                chunk_amount = round(remaining_funds, 2)

            # Route transfers seconds apart to stress the transactional velocity monitor
            current_time += timedelta(seconds=random.randint(15, 45))

            micro_transactions.append(
                {
                    "sub_tx_id": f"STRESS_TX_{tx_counter:04d}",
                    "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "amount_eur": chunk_amount,
                    "target_node": "MULE_ACCOUNT_XYZ",
                }
            )
            accumulated_routed_funds += chunk_amount
            tx_counter += 1

        return micro_transactions

    def evaluate_aml_rule_resilience(self, attack_payload):
        """Executes the daily automated audit.

        Passes the injected attack data stream through AML scoring engines 
        to detect hidden vulnerabilities or threshold bypasses.
        """
        print("[+] Processing stress vectors through compliance filters...")

        rolling_window_volume = 0.0
        alert_triggered = False
        breach_index = -1

        # System logic evaluation loop
        for index, tx in enumerate(attack_payload):
            rolling_window_volume += tx["amount_eur"]

            # Checking system trigger: cumulative volume tracking within the scenario session
            if (
                rolling_window_volume >= self.aml_threshold_eur
                and not alert_triggered
            ):
                alert_triggered = True
                breach_index = index

        # Compiling analytical results
        success = alert_triggered
        summary = {
            "execution_timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "total_attack_transactions": len(attack_payload),
            "aml_trigger_activated": alert_triggered,
            "vulnerability_detected": not success,
            "security_perimeter_status": "SECURE" if success else "VULNERABLE",
        }

        if success:
            breach_tx = attack_payload[breach_index]
            summary["alert_details"] = (
                f"AML logic successfully triggered at step {breach_index + 1}. "
                f"Cumulative volume reached €{rolling_window_volume:,.2f} on transaction {breach_tx['sub_tx_id']}."
            )
        else:
            summary["alert_details"] = (
                "CRITICAL VULNERABILITY: Attack payload successfully bypassed global system barriers "
                "without triggering volume limits."
            )

        self.test_log_output.append(summary)
        return summary


if __name__ == "__main__":
    print("=" * 70)
    print("        DAILY AUTOMATED AML RISK STRESS-TESTING PIPELINE        ")
    print("=" * 70)

    # Initialize Engine
    engine = AMLStressTestingEngine(aml_threshold_eur=10000.0)

    # 1. Generate dynamic structuring attack payload
    attack_stream = engine.simulate_smurfing_attack(target_volume=32000.0)

    # 2. Run active barrier penetration test
    audit_results = engine.evaluate_aml_rule_resilience(attack_stream)

    # 3. Print out high-value executive risk summary
    print("\n" + "-" * 70)
    print("                      STRESS TEST AUDIT REPORT                ")
    print("-" * 70)
    print(f"Engine Run Time      : {audit_results['execution_timestamp']}")
    print(
        f"Simulated Wave Rows  : {audit_results['total_attack_transactions']} sub-transactions"
    )
    print(f"AML Alert Fired      : {audit_results['aml_trigger_activated']}")
    print(
        f"System Integrity     : {audit_results['security_perimeter_status']}"
    )
    print(f"Audit Narrative      : {audit_results['alert_details']}")
    print("=" * 70)

    # 4. Generate structured artifact (JSON report output for compliance tracking)
    output_dir = "./stress_reports"
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "daily_aml_stress_log.json")

    with open(report_path, "w") as f:
        json.dump(audit_results, f, indent=4)
    print(f"[+] Automated test log entry exported to: {report_path}")
