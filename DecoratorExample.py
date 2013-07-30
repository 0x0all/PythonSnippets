

# ----- Example 1: Food ---------

def bread(fcn):
	def wrapper():
		print ' /------\ '
		print fcn()
		print ' \______/ '
	return wrapper

@bread
def sandwich(food='|=burger-|'):
	print food

sandwich()


# ----- Example 2 Bold/italic text ---------


def bold(fn):
	def wrapper(arg1):
		return fn('<b>' + arg1 + '</b>')
	return wrapper

def italics(fn):
	def wrapper(arg1):
		return fn('<i>' + arg1 + '</i>')
	return wrapper

@bold
@italics
def write(message=""):
	return message

print write("Hello!")