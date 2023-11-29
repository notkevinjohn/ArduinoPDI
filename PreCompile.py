#!/usr/bin/python3
from ArduinoSketchParser import ArduinoSketchParser
from PythonClassExporter import PythonClassExporter

device = "/dev/arduino-mega"
sketchData = ArduinoSketchParser("Sketch.c").parse()
exporter = PythonClassExporter(sketchData, device)


