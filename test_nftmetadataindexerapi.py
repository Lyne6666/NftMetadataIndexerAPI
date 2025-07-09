# test_nftmetadataindexerapi.py
"""
Tests for NftMetadataIndexerAPI module.
"""

import unittest
from nftmetadataindexerapi import NftMetadataIndexerAPI

class TestNftMetadataIndexerAPI(unittest.TestCase):
    """Test cases for NftMetadataIndexerAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerAPI()
        self.assertIsInstance(instance, NftMetadataIndexerAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
