# test_corerift.py
"""
Tests for CoreRift module.
"""

import unittest
from corerift import CoreRift

class TestCoreRift(unittest.TestCase):
    """Test cases for CoreRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreRift()
        self.assertIsInstance(instance, CoreRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
