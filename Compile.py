#!/usr/bin/python3
import re
from pycparser import parse_file, c_generator

class PreCompiler():
	adornmentPattern = "^\/\/\[(.*?)\]"
	adornments = {}
	sanitized = []
	code = []

	def __init__(self, target):
		self.parseAdornments(target)
		self.exportPartial()
		#print (self.sanitized)
		#print (self.code)
		self.parseCCode("partial.c")

	def parseAdornments(self, target):
		with open (target) as file:
			lines = file.readlines()
			for i in range(0,len(lines)):
				line = lines[i]
				if re.match(self.adornmentPattern, line):
					line = line.replace('[','')
					line = line.replace(']','')
					line = line.replace('/','')
					adornmentKeys = line.split(",")
					adornmentKeys = [x.strip() for x in adornmentKeys]
					nextLine = lines[i+1]
					functionName = self.extractFunctionName(nextLine)
					for key in adornmentKeys:
						if not key in self.adornments:
							self.adornments[key] = []
						self.adornments[key].append(functionName)

				elif self.checkSanitize(line):
					self.sanitized.append(line)
				else:
					self.code.append(line)

	def checkSanitize(self, line):
		if "#include" in line:
			return True
		return False

	def extractFunctionName(self, functionString):
		functionName = functionString.split(" ")[1].split("(")[0]
		return functionName

	def exportPartial(self):
		with open("partial.c", "w+") as file:
			for line in self.code:
				file.write(line)

	def parseCCode(self, target, use_cpp=True):
		ast = parse_file(target, use_cpp=use_cpp)
		generator = c_generator.CGenerator()
		for function in ast.ext:
			fname = function.decl.name
			callable = False
			for key in self.adornments:
				if fname in self.adornments[key]:
					if key == "callable":
						callable = True

			print (fname, callable)

if __name__ == "__main__":
	precompiler = PreCompiler('Firmware.c')
	for key in precompiler.adornments:
		print (key, precompiler.adornments[key])
