import unittest
from main.Add import Add,sub
f = open("inputForadd.txt","r")
class TestSum(unittest.TestCase):
	def test_1(self):
		a,b=map(int,f.readline().strip().split(","))
		self.assertEqual(Add(a,b),a+b,f"adition must {a+b}")
	def test_2(self):
		a,b=map(int,f.readline().strip().split(","))
		self.assertEqual(Add(a,b),a+b,f"adition must {a+b}")
	def test_3(self):
		a,b=map(int,f.readline().strip().split(","))
		self.assertEqual(sub(a,b),a-b,f"adition must {a-b}")
	def test_4(self):
		a,b=map(int,f.readline().strip().split(","))
		self.assertEqual(Add(a,b),a+b,f"adition must {a+b}")