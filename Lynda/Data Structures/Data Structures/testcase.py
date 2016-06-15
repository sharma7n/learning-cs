import traceback

def testcase(method):
	def test_method(self):
		try:
			method(self)
		except AssertionError:
			print("TEST FAILED: " + method.__name__ + " failed.")
			traceback.print_exc()
		except:
			raise
	return test_method
	
def decoratecls(decorator):
	def decorate_cls(cls):
		for attr in cls.__dict__:
			if callable(getattr(cls, attr)):
				setattr(cls, attr, decorator(getattr(cls, attr)))
		return cls
	return decorate_cls
	
def run_tests(test_object):
	tests = list(test_object.__class__.__dict__.values())
	for test in tests:
		if callable(test):
			test(test_object)