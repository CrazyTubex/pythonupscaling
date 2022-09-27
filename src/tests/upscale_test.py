from scripts.setup import setup
from scripts.upscale import upscale
from scripts.upscale import read_image
import unittest
from pathlib import Path
import os





class TestUpScale(unittest.TestCase):
    def test_setup(self):
        self.assertNotEqual(setup()[1], False)
    def test_read_image(self):
        self.assertEqual(read_image('imageforunittest.png', (str(Path(os.getcwd()).parent)+'/input/'))[1], True)
    def test_upscale(self):
        self.assertEqual(upscale(setup()[0], 'imageforunittest.png', (str(Path(os.getcwd()).parent)+'/input/'), (str(Path(os.getcwd()).parent)+'/output/')), True)
        
    

