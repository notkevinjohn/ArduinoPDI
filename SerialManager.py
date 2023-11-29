import os
import serial
import time

class SerialManager():
	timeout = 3
	def __init__(self, baudrate, device, firmware, version):
		self.ser = serial.Serial()
		self.ser.timeout = self.timeout
		self.ser.port = device
		self.ser.baudrate = baudrate
		self.version = version
		self.firmware = firmware

	def connect(self):
		if not os.path.exists(self.ser.port):
			raise Exception('device ' +self.ser.port+' not found')
		self.ser.open()
		self.restart()
		firmware = self.expect(self.firmware)
		if firmware == None:
			raise Exception('firmware ' +self.firmware+' not found')
		version = firmware.split(" ")[1]
		if not version == self.version:
			raise Exception('version '+version+' does not match expected version '+self.version)

	def restart(self):
		self.ser.setDTR(False)
		time.sleep(1)
		self.ser.flushInput()
		self.ser.setDTR(True)

	def close(self):
		self.ser.close()

	def expect(self, string, invert=False):
		timeinit = time.perf_counter()
		while(time.perf_counter() < timeinit+self.timeout):
			line = self.readLine()
			print (line)
			if invert == False:
				if string in line:
					return line
			if invert == True:
				if not string in line:
					return line
		return None

	def readLine(self):
		timeinit = time.perf_counter()
		while(time.perf_counter() < timeinit+0.5):
			response = self.ser.readline().decode().strip()
			return response
		return None


	def sendCommand(self, command, expect=None):
		if expect == None:
			expect = command
		print (command)
		self.ser.write(command+("\r").encode())
		received = self.expect(expect)
		print (received)
		if received == None:
			raise Exception('command '+command+' not received')
		self.ser.flushInput()
		self.ser.flushOutput()
		time.sleep(0.10)
		timeinit = time.perf_counter()
		result = None
		while(time.perf_counter() < timeinit+self.timeout):
			result = self.readLine()
			if not result == "":
				break
		return result

