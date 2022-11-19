#define ECHO_PIN 2
#define TRIG_PIN 3
#define ORG "74jmsm"
#define DEVICE_TYPE "abcd"
#define DEVICE_ID "98765"
#define TOKEN "1234567890"
char server[]=ORG ".messaging.internetofthings.ibmcloud.com";
char publishtopic[]="iot-2/evt/data/fmt/json";
char subscribetopic[]="iot-2/cmd/command/fmt/string";
char authmethod[]="use-token-auth";
char token[]=TOKEN;
char clientId[]="d:"ORG":"DEVICE_TYPE":"DEVICE_ID;
const int out=12;
const int in=13;
void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

float readDistanceCM() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  int duration = pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2;
}

void loop() {
  float distance = readDistanceCM();

  bool isNearby = distance < 100;
  digitalWrite(LED_BUILTIN, isNearby);

  Serial.print("Measured distance: ");
  Serial.println(readDistanceCM());

  delay(100);
}