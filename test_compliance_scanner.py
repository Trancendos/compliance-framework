import unittest
import sqlite3
import os
from compliance_scanner_free_tier import ComplianceScannerDB

class TestComplianceScannerDB(unittest.TestCase):

    def setUp(self):
        self.db_file = "test_compliance_scanner.db"
        self.db = ComplianceScannerDB(self.db_file)

    def test_connection_is_open(self):
        self.assertIsNotNone(self.db.conn)
        # Check if the connection is active by sending a simple query
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT 1")
        self.assertIsNotNone(cursor.fetchone())

    def test_close_connection(self):
        # Ensure the close_connection method exists
        self.assertTrue(hasattr(self.db, 'close_connection'), "close_connection method not found")

        # Close the connection
        self.db.close_connection()

        # Verify the connection is closed by trying to use it
        with self.assertRaises(sqlite3.ProgrammingError):
            self.db.conn.cursor()

    def tearDown(self):
        # The test_close_connection test closes the connection.
        # For other tests, we should ensure the connection is closed.
        if self.db.conn:
             self.db.close_connection()
        # Clean up the database file
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

if __name__ == '__main__':
    unittest.main()
