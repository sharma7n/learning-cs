# Python decorators

def bar(func):
	def in_bar():
		print("buzz")
		func()
	return in_bar

@bar
def foo():
	print("fizz")
	
# foo = bar(foo)
foo()
foo()
foo()