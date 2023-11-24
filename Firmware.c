#include <SparkFun_UHF_RFID_Reader.h>
#include <SoftwareSerial.h>
SoftwareSerial softSerial(2, 3);
RFID nano;
int timeout = 5000;
char inbytes[9];
char tagData[8];
char arguments[8];
int serialIndex = 0;

void setup(){
	Serial.begin(9600);
	while (!Serial);
	Serial.println("RFID Firmware v1.0");
	if (setupNano(38400) == false)
	{
		Serial.println("Module failed to respond. Please check wiring.");
		while (1);
	}
	nano.setReadPower(0);
	nano.setWritePower(0);
	writeData(arguments);

	nano.setRegion(REGION_NORTHAMERICA);
	nano.setReadPower(2700);
	nano.setWritePower(2700);

}

void loop(){
	if(Serial.available() > 0 ){
		String message = serialMessage();
	}
}

String serialMessage(){
	char inbyte;
	while(Serial.available() > 0)
	{
		inbyte = Serial.read();
		inbytes[serialIndex] = inbyte;
		serialIndex++;
		if (inbyte == '\r') {
			deserializeMessage(inbytes);
			for (int j=0; j<9; j++){
				inbytes[j] = 0;
			}
			serialIndex=0;
		}
	}
}

void deserializeMessage(char inbytes[]){
	int success = 0;
	char command = inbytes[0];
	Serial.println(command);
	if (command == 'r'){
		success = readData();
		if (success == 1){
			printArray(tagData, 8);
		}
		else {
			Serial.println("no tag found");
		}
	}
	if (command == 'w'){
		for (int i=0; i<8; i++){
			arguments[i] = inbytes[i+1];
		}
		success = writeData(arguments);
		Serial.println(success==1);
	}
}

void printArray(char array[], int len){
	for(int i=0; i<len; i++){
		Serial.print(array[i]);
	}
	Serial.println("");
}

//[callable]
bool readData(){
	byte responseType;
	char dataOut[10];
	byte len = sizeof(dataOut);

	responseType = nano.readUserData(dataOut, len);
	if (responseType == RESPONSE_SUCCESS){
		for (byte x = 0; x < len; x++){
			//Serial.println(dataOut[x]);
                        tagData[x] = char(dataOut[x]);
                }
		return 1;
	}
	else {
		return 0;
	}

}

//[callable]
bool writeData(char dataIn[]){
	byte responseType = nano.writeUserData(dataIn, 8);
	if (responseType == RESPONSE_SUCCESS) {
		return 1;
	}
	else {
		return 0;
	}
}

boolean setupNano(long baudRate){
	nano.begin(softSerial);
	softSerial.begin(baudRate);
	while (!softSerial);
	while (softSerial.available()) softSerial.read();

	nano.getVersion();
	if (nano.msg[0] == ERROR_WRONG_OPCODE_RESPONSE)
	{
		nano.stopReading();
		Serial.println(F("Module continuously reading. Asking it to stop..."));
		delay(1500);
	}
	else
	{
		softSerial.begin(115200);
		nano.setBaud(baudRate);
		softSerial.begin(baudRate);
		delay(250);
	}

	nano.getVersion();
	if (nano.msg[0] != ALL_GOOD) return (false);
	nano.setTagProtocol();
	nano.setAntennaPort();
	return (true);
}
