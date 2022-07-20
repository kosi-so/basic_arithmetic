import unittest
import basic_arith

class TestBasicArith (unittest.TestCase):

	def test_add(self):
		self.assertEqual(basic_arith.add(15, 10), 25)
		self.assertEqual(basic_arith.add(-15, 10), -5)
		self.assertEqual(basic_arith.add(-15, -10), -35)

	def test_subtraction(self):
		self.assertEqual(basic_arith.subtract(15, 10), 5)
		self.assertEqual(basic_arith.subtract(-15, 10), -25)
		self.assertEqual(basic_arith.subtract(-15, -10), -5)

	def test_multiply(self):
		self.assertEqual(basic_arith.multiply(15, 10), 150)
		self.assertEqual(basic_arith.multiply(-15, 10), -150)
		self.assertEqual(basic_arith.multiply(-15, -10), 150)

	def test_divide(self):
		self.assertEqual(basic_arith.divide(15, 3), 5)
		self.assertEqual(basic_arith.divide(-15, 3), -5)
		self.assertEqual(basic_arith.divide(-15, -3), 5)

	def test_floor(self):
		self.assertEqual(basic_arith.floor(15, 10), 1)
		self.assertEqual(basic_arith.floor(-15, 10), -1)
		self.assertEqual(basic_arith.floor(-15, -10), 1)


if __name__ == "__main__":
	unittest.main()