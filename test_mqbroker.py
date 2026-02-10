# test_mqbroker.py
"""
Tests for MqBroker module.
"""

import unittest
from mqbroker import MqBroker

class TestMqBroker(unittest.TestCase):
    """Test cases for MqBroker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MqBroker()
        self.assertIsInstance(instance, MqBroker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MqBroker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
