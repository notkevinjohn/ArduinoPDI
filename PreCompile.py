#!/usr/bin/python3
from ArduinoSketchParser import ArduinoSketchParser
from PythonClassExporter import PythonClassExporter

functionData = ArduinoSketchParser("Firmware.c").parse()
exporter = PythonClassExporter(functionData)
exporter.export("Wrapper.py")

#for key in functionData:
#	functions = functionData[key]
#	for function in functions:
#		print (key, function)


