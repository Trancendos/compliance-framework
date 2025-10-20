import sqlite3
from sqlite3 import Error

class ComplianceScannerDB:
    def __init__(self, db_file):
        """Initialize the database connection."""
        self.conn = self.create_connection(db_file)
        self.create_tables()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_tables(self):
        """Create tables for compliance scans and violations."""
        create_scans_table = """CREATE TABLE IF NOT EXISTS scans (
                                    id INTEGER PRIMARY KEY,
                                    timestamp TEXT NOT NULL,
                                    scan_result TEXT NOT NULL
                                );"""
        
        create_violations_table = """CREATE TABLE IF NOT EXISTS violations (
                                       id INTEGER PRIMARY KEY,
                                       scan_id INTEGER,
                                       violation TEXT NOT NULL,
                                       FOREIGN KEY (scan_id) REFERENCES scans (id)
                                   );"""
        
        try:
            c = self.conn.cursor()
            c.execute(create_scans_table)
            c.execute(create_violations_table)
        except Error as e:
            print(e)

    def insert_scan(self, scan_result):
        """Insert a new scan result."""
        sql = '''INSERT INTO scans(timestamp, scan_result)
                 VALUES(datetime('now'), ?)'''
        cur = self.conn.cursor()
        cur.execute(sql, (scan_result,))
        self.conn.commit()
        return cur.lastrowid

    def insert_violation(self, scan_id, violation):
        """Insert a new violation."""
        sql = '''INSERT INTO violations(scan_id, violation)
                 VALUES(?, ?)'''
        cur = self.conn.cursor()
        cur.execute(sql, (scan_id, violation))
        self.conn.commit()
        return cur.lastrowid

    def get_historical_data(self):
        """Retrieve all compliance scans."""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM scans")
        return cur.fetchall()

    def get_violations(self, scan_id):
        """Retrieve violations for a specific scan."""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM violations WHERE scan_id=?", (scan_id,))
        return cur.fetchall()

# Example usage:
if __name__ == "__main__":
    db = ComplianceScannerDB("compliance_scanner.db")
    scan_id = db.insert_scan("Scan completed with no violations.")
    db.insert_violation(scan_id, "Minor configuration issue detected.")
    print(db.get_historical_data())
    print(db.get_violations(scan_id))
