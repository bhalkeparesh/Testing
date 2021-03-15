import unittest
from Add import Add,sub
class TestSum(unittest.TestCase):
	def test_1(self):
		self.assertEqual(Add(2,3),5,"adition must 5")
	def test_2(self):
		self.assertEqual(Add(3,3),6,"adition must 6")
	def test_3(self):
		self.assertEqual(sub(2,3),-1,"adition must 5")
	def test_4(self):
		self.assertEqual(Add(3,3),6,"adition must 6")