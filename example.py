from compliance_scanner_free_tier import ComplianceScannerDB

def main():
    """
    An example script to demonstrate the usage of the ComplianceScannerDB class.
    """
    db = ComplianceScannerDB("compliance_scanner.db")

    # Scenario 1: Scan with no violations
    print("--- Running Scan 1: No Violations ---")
    scan_id_1 = db.insert_scan("Scan completed with no violations.")
    if scan_id_1:
        print(f"Scan 1 registered with ID: {scan_id_1}")
        print("Historical Data after Scan 1:")
        print(db.get_historical_data())
        print("Violations for Scan 1 (should be empty):")
        print(db.get_violations(scan_id_1))
    print("-" * 20)

    # Scenario 2: Scan with a violation
    print("\n--- Running Scan 2: Violation Detected ---")
    scan_id_2 = db.insert_scan("Scan completed with violations.")
    if scan_id_2:
        db.insert_violation(scan_id_2, "Minor configuration issue detected.")
        print(f"Scan 2 registered with ID: {scan_id_2}")
        print("Historical Data after Scan 2:")
        print(db.get_historical_data())
        print(f"Violations for Scan 2 (should show one violation):")
        print(db.get_violations(scan_id_2))
    print("-" * 20)

    # Close the database connection
    db.close_connection()
    print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()
