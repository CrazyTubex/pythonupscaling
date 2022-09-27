from scripts.setup import setup
from scripts.upscale import upscale
from scripts.upscale import read_image
import unittest




class TestUpScale(unittest.TestCase):
    def test_setup(self):
        self.assertNotEqual(setup()[1], False)
    def test_read_image(self):
        self.assertEqual(read_image('imageforunittest.png')[1], True)
    def test_upscale(self):
        self.assertEqual(upscale(setup()[0], 'imageforunittest.png'), True)
        
    

