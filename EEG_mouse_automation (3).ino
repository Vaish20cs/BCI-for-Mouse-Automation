int eegPin=A14;
int eegValue;
void setup() {
  // put your setup code here, to run once:
  pinMode(eegPin,INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
eegRead();
}
void eegRead()
{
  eegValue=analogRead(eegPin);
  Serial.println(eegValue);
}
