#!/usr/bin/python3
import re
#from pycparser import parse_file, c_generator

class PreCompiler():
	adornmentPattern = "^\/\/\[(.*?)\]"
	adornments = {}
	sanitized = []
	code = []

	def __init__(self, target):
		self.parse(target)

	def parse(self, target):
		with open (target) as file:
			lines = file.readlines()
			for i in range(0,len(lines)):
				line = lines[i]
				if self.checkAdornment(line):
					adornmentKeys = self.parseAdornment(line)
					print (adornmentKeys)
				#	nextLine = lines[i+1]
				#	functionName = self.extractFunctionName(nextLine)

				#elif sexlf.checkSanitize(line):
				#	self.sanitized.append(line)
				#else:
				#	self.code.append(line)

	def checkAdornment(self, line):
		if re.match(self.adornmentPattern, line):
			return True
		return False

	def parseAdornment(self, line):
		line = line.replace('[','')
		line = line.replace(']','')
		line = line.replace('/','')
		adornmentKeys = line.split(",")
		adornmentKeys = [x.strip() for x in adornmentKeys]
		return adornmentKeys


	#def checkSanitize(self, line):
	#	if "#include" in line:
	#		return True
	#	return False

	#def extractFunctionName(self, functionString):
	#	functionName = functionString.split(" ")[1].split("(")[0]
	#	return functionName

	#def exportPartial(self):
	#	with open("partial.c", "w+") as file:
	#		for line in self.code:

if __name__ == "__main__":
	precompiler = PreCompiler('Firmware.c')
	for key in precompiler.adornments:
		print (key, precompiler.adornments[key])
