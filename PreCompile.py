#!/usr/bin/python3
from ArduinoSketchParser import ArduinoSketchParser
from InterfaceGenerator import InterfaceGenerator
from PythonClassExporter import PythonClassExporter

device = "/dev/arduino-mega"
sketchData = ArduinoSketchParser("Sketch.c").parse()
interface = InterfaceGenerator(sketchData).writeFile("Interface.txt")
#exporter = PythonClassExporter(sketchData, device)


