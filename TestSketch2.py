from SerialManager import SerialManager

class TestSketch():

	def __init__(self):
		self.serialManager = SerialManager(9600,"/dev/arduino-mega","TestSketch","1.0")
		self.serialManager.connect()


if __name__ == "__main__":
	testsketch = TestSketch()


