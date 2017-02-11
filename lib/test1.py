""" Test class to test each function returns what it is designed to do """
import json

class UnitTest1(object):
	def function_true(self, value):
		if not value == True:
			raise ValueError('Value must be (bool) True')
		return value

	def function_false(self, value):
		if  not value == False:
			raise ValueError('Value must be (bool) False')
		return value

	def function_int(self, value):
		if not isinstance(value, int):
			raise ValueError('Value must be of type int')
		return True

	def function_float(self, value):
		if not isinstance(value, float):
			raise ValueError('Value must be of type float')
		return True

	def function_json(self, value):
		try:
			json.loads(value)
		except:
			raise ValueError('Value must be a valid JSON')
		return True

	def function_simple(self, value):
		if not value == True:
			raise ValueError('Value must be (bool) True Mother Fucker')
		return value

	def run(self):
		# test function_true
		self.function_true(True)

		# test function_false
		self.function_false(False)

		# test function_int
		self.function_int(1)

		# test function_float
		self.function_float(1.5)

		# test function_json
		self.function_json(json.dumps({'key': 'value'}))

		# test function_simple
		if not self.function_simple(True):
			raise ValueError('Must return (bool) True')		

		# if we get here all tests have passed
		print 'Test Passed!'

if __name__ == '__main__':
	app = UnitTest1()
	app.run()