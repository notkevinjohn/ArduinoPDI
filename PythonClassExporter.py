#!/usr/bin/python3
from TypeMapping import TypeMapping

class PythonClassExporter():
	adornmentKey = "callable"
	indentation = "\t"
	#indentation = "    "

	def __init__(self, functionData):
		self.functions = []
		for key in functionData:
			functions = functionData[key]
			for function in functions:
				if key == self.adornmentKey:
					self.functions.append(function)

	def export(self, filename):
		with open (filename, "w+") as file:
			for function in self.functions:
				file.write(self.writeFunctionHeader(function))
				file.write('\n')


	def writeFunctionHeader(self, function):
		header = "def "
		header += function.name
		header += "("
		pargs = []
		for arg in function.args:
			pargs.append(arg.ptype+" "+arg.name)

		header+=", ".join(pargs)
		header += ")"
		header += ":\n"
		header += self.indentation+"pass\n"
		return header
