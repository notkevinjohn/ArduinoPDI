class FunctionData():
	name = None
	returnType = None
	args = []

	def __str__(self):
		args = [str(x[0])+" "+str(x[1]) for x in self.args]
		argString = ", ".join(args)
		string = ""
		string += self.returnType
		string += " "
		string += self.name
		string += "("
		string += argString
		string += ")"
		return string

