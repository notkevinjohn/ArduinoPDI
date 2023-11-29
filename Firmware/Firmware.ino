char message[10];
int messageIndex=0;


void setup() {
	Serial.begin(9600);
	while(!Serial){delay(1);}
	Serial.println("TestSketch 1.0");
}

void loop() {
	if(Serial.available() > 0 ){
		serialMessage();
        }

}

String serialMessage()
{
        char c = Serial.read();
        if (c == '\r'){
               Serial.println(message);
		memset(message, 0, sizeof message);
                messageIndex = 0;

	}
        else {
                message[messageIndex] = c;
                messageIndex ++;
        }

}


//[callable]
void test() {
	Serial.println("Test!");
}
