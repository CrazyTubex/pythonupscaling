from scripts.setup import setup
from scripts.upscale import upscale
import unittest




class TestUpScale(unittest.TestCase):
    def test_setup(self):
        self.assertNotEqual(setup(), False)
    def test_upscale(self):
        self.assertEqual(upscale(setup(), 'imageforunittest.png'), True)
        
    

