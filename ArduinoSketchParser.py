#!/usr/bin/python3
import re
from TypeMapping import TypeMapping
from FunctionData import *

class ArduinoSketchParser():
	adornmentPattern = "^\/\/\[(.*?)\]"
	adornedFunctions = {}

	def __init__(self, target):
		self.target = target

	def parse(self):
		with open (self.target) as file:
			lines = file.readlines()
			for i in range(0,len(lines)):
				line = lines[i]
				if self.checkAdornment(line):
					adornmentKeys = self.parseAdornment(line)
					nextLine = lines[i+1]
					functionData = self.extractFunctionData(nextLine)
					for key in adornmentKeys:
						if not key in self.adornedFunctions:
							self.adornedFunctions[key] = []
						self.adornedFunctions[key].append(functionData)

		return self.adornedFunctions

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


	def extractFunctionData(self, fstring):
		fdata = FunctionData()
		fdata.name = fstring.split(" ")[1].split("(")[0]
		returnType = fstring.split(" ")[0]
		if TypeMapping.validateType(returnType):
			fdata.returnType = returnType
		args = fstring.split("(")[1].split(")")[0].split(",")
		args = [x.strip() for x in args]
		for arg in args:
			argVals = arg.split(" ")
			if len(argVals) < 2:
				break
			type = arg.split(" ")[0].strip()
			name = arg.split(" ")[1].strip()
			array, length, name = self.checkVariableName(name)
			if TypeMapping.validateType(type):
				farg = FunctionArg()
				farg.name = name
				farg.ctype = type
				farg.ptype = TypeMapping.types[type]
				farg.array = array
				farg.length = length
				fdata.args.append(farg)
		return fdata

	def checkVariableName(self, variableName):
		array = False
		length = None

		if "[" in variableName and "]" in variableName:
			array = True
			length = variableName.split("[")[1]
			length = length.split("]")[0]
			variableName = variableName.replace("["+length+"]", "")
			if length == "":
				length = None
		return array, length, variableName




if __name__ == "__main__":
	asp = ArduinoSketchParser('Firmware.c')
