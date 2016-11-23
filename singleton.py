# 1. We will allow the creation of only one instance of the Singleton class.
# 2. If an instance exists, we will serve the same object again.
# refer to Packt.Learning.Python.Design.Patterns.2nd.Edition.178588803X

class Singleton(object):
	# override the __new__ method to control the object creation
	def __new__(cls):
		# To check whether the class already has an instance.
		if not hasattr(cls, '_Singleton__instance'):
			cls.__instance = super(Singleton, cls).__new__(cls)
			return cls.__instance
		else:
			print("Instance already created:", cls.getInstance())
			return cls.__instance
	
	@classmethod
	def getInstance(cls):
		if not hasattr(cls, '_Singleton__instance'):
			raise ValueError("Please create a instance at first!")
		return cls.__instance


s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton()
print("s: ", s)
print("s1: ", s1)