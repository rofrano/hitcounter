"""
Test Cases for Hitcounter Service
"""
import json
import unittest
from hitcounter import app


class TestHitcounterService(unittest.TestCase):
    """Test case for HitCounter Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        """Test that the home page works"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_get_hitcount(self):
        """Get the current hit count"""
        resp = self.client.get("/hits")
        self.assertEqual(resp.status_code, 200)
        body = json.loads(resp.data)
        count = body["hits"]
        self.assertEqual(count, 0)

    def test_increment_hitcount(self):
        """Increment the hit count"""
        # increment the counter
        resp = self.client.put("/hits")
        self.assertEqual(resp.status_code, 200)
        body = json.loads(resp.data)
        count = body["hits"]
        self.assertEqual(count, 1)
