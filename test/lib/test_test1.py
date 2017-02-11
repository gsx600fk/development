import json
import mock
from lib.test1 import UnitTest1
from development.test.__init__ import UnitTestBase, unittest

class UnitTest(UnitTestBase):

	def test_function_true(self):
		app = UnitTest1()
		result = app.function_true(True)
		self.assertTrue(result)

	def test_fail_function_true(self):
		app = UnitTest1()
		with self.assertRaises(ValueError):
			app.function_true(False)

	def test_function_false(self):
		app = UnitTest1()
		result = app.function_false(False)
		self.assertFalse(result)

	def test_fail_function_false(self):
		app = UnitTest1()
		with self.assertRaises(ValueError):
			app.function_false(True)

	def test_function_int(self):
		app = UnitTest1()
		result = app.function_int(1)
		self.assertTrue(result)

	def test_fail_function_int(self):
		app = UnitTest1()
		with self.assertRaises(ValueError):
			app.function_int(1.0)

	def test_function_float(self):
		app = UnitTest1()
		result = app.function_float(1.0)
		self.assertTrue(result)

	def test_fail_function_float(self):
		app = UnitTest1()
		with self.assertRaises(ValueError):
			app.function_float(1)

	def test_function_json(self):
		app = UnitTest1()
		result = app.function_json(json.dumps({'key': 'value'}))
		self.assertTrue(result)

	def test_fail_function_json(self):
		app = UnitTest1()
		with self.assertRaises(ValueError):
			app.function_json({'key': 'value'})

	def test_function_simple(self):
		app = UnitTest1()
		result = app.function_simple(True)
		self.assertTrue(result)


	def test_fail_function_simple(self):
		app = UnitTest1()
		with self.assertRaises(ValueError):
			app.function_simple(False)


if __name__ == '__main__':
	unittest.main()
