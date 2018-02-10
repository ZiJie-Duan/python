import unittest
from mokuaiku import corez

class cscs(unittest.TestCase):

	def test_my(self):
		zz = corez()
		self.assertEqual(zz,'0x133ecf20x1317d33')


unittest.main()