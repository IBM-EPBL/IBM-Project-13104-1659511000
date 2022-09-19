int tempMode=0;
int t;
void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(12,OUTPUT);
}
void loop()
{
  int motion=digitalRead(2);
  if(motion==1){
  	Serial.println("Motion detected");
    tone(12,3000);
    delay(1000);
  }
  t=tempMode;
    Serial.println(t);
    if(t>60)
    {
      tone(12,4000);
      delay(1000);
    }
  else
    Serial.println("low temp");
  delay(1000);
    Serial.println("No Motion");
  tone(12,2500);
    delay(1000);
  }
  