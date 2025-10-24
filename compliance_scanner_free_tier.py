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
            print(f"Error connecting to database: {e}")
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
            print(f"Error creating tables: {e}")

    def insert_scan(self, scan_result):
        """Insert a new scan result."""
        sql = '''INSERT INTO scans(timestamp, scan_result)
                 VALUES(datetime('now'), ?)'''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (scan_result,))
            self.conn.commit()
            return cur.lastrowid
        except Error as e:
            print(f"Error inserting scan: {e}")
            return None

    def insert_violation(self, scan_id, violation):
        """Insert a new violation."""
        sql = '''INSERT INTO violations(scan_id, violation)
                 VALUES(?, ?)'''
        try:
            cur = self.conn.cursor()
            cur.execute(sql, (scan_id, violation))
            self.conn.commit()
            return cur.lastrowid
        except Error as e:
            print(f"Error inserting violation: {e}")
            return None

    def get_historical_data(self):
        """Retrieve all compliance scans."""
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM scans")
            return cur.fetchall()
        except Error as e:
            print(f"Error retrieving historical data: {e}")
            return []

    def get_violations(self, scan_id):
        """Retrieve violations for a specific scan."""
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM violations WHERE scan_id=?", (scan_id,))
            return cur.fetchall()
        except Error as e:
            print(f"Error retrieving violations: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()

