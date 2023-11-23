#!/usr/bin/python3
import re
from pycparser import parse_file, c_generator

class PreCompiler():
	adornmentPattern = "^\/\/\[(.*?)\]"
	adornments = []

	def __init__(self, target):
		self.parseAdornments(target)
		self.parseCCode(target)

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
					self.adornments.append([adornmentKeys, nextLine])


	def parseCCode(self, target, use_cpp=True):
		ast = parse_file(target, use_cpp=use_cpp)
		generator = c_generator.CGenerator()
		print (generator.visit(ast))

if __name__ == "__main__":
	precompiler = PreCompiler('Sketch.c')
	print (precompiler.adornments)

