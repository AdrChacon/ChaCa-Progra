// Arduino pin numbers
const int X_pin = 0; // analog pin connected to first X output
const int Y_pin = 1; // analog pin connected to first Y output   
const int X2_pin = 2; // analog pin connected to second X output
const int Y2_pin = 3; // analog pin conected to second Y output
int Player1Shoot = 2;
int Player2Shoot = 7;

int valP1 = 0;
int valP2 = 0;

int buttonState = 0;

void setup() {
  pinMode(Player1Shoot, INPUT);
  pinMode(Player2Shoot, INPUT);
  Serial.begin(9600);
}

void loop() {
  valP1 = digitalRead(Player1Shoot);
  valP2 = digitalRead(Player2Shoot);
  int Eje_XP1 = analogRead(X_pin);
  int Eje_YP1 = analogRead(Y_pin);
  int Eje_XP2 = analogRead(X2_pin);
  int Eje_YP2 = analogRead(Y2_pin);
  int NUM = 0;
  if (Eje_XP1 > 600) {
    Serial.println(1);
    NUM++;
    }
  if (Eje_XP1 < 400){
    Serial.println(2);
    NUM++;
    }
  if (Eje_YP1 > 600) {
    Serial.println(3);
    NUM++;
    }
  if (Eje_YP1 < 400){
    Serial.println(4);
    NUM++;
    }
  if (valP1 == 1){
    Serial.println(10);
    NUM++;
    }
  if (Eje_XP2 > 600) {
    Serial.println(5);
    NUM++;
    }
  if (Eje_XP2 < 400){
    Serial.println(6);
    NUM++;
    }
  if (Eje_YP2 > 600) {
    Serial.println(7);
    NUM++;
    }
  if (Eje_YP2 < 400){
    Serial.println(8);
    NUM++;
    }
  if (valP2 == 1){
    Serial.println(11);
    NUM++;
    }
  if (NUM == 0){
    Serial.println(9);
    }
  delay(20);
}

