#!/usr/bin/python3
from ArduinoSketchParser import ArduinoSketchParser

functionData = ArduinoSketchParser("Firmware.c").parse()
for key in functionData:
	functions = functionData[key]
	for function in functions:
		print (key, function)
