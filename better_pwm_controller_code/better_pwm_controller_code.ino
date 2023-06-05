#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  20
#define SERVOMAX  200
#define SERVO_FREQ 50

uint8_t servonum = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("8 channel Servo test!");

  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);

  delay(10);
}

void setServoPulse(uint8_t n, double pulse) {
  double pulselength;
  
  pulselength = 1000000;
  pulselength /= SERVO_FREQ;
  pulselength /= 4096;
  pulse *= 1000000;
  pulse /= pulselength;
  pwm.setPWM(n, 0, pulse);
}

String alphabet = "abcdefghijklmnopqrstuvwxyz";

void loop() {
  if (Serial.available()) {
    String myString = Serial.readString();

    for (int i = 0; i < myString.length(); i++) {
      char currentChar = myString.charAt(i);
      int index = alphabet.indexOf(currentChar);
      index = index % 15;

      Serial.println(currentChar);

      makeServoHit(index);
      delay(40); // Delay before moving to the next servo position
    }

    Serial.print("Received data: ");
    Serial.println(myString);
  }
}

void makeServoHit(uint8_t snum) {
  // Phase 1: Go Down
  for (uint16_t pulselen = SERVOMAX; pulselen >= SERVOMIN; pulselen--) {
    pwm.setPWM(snum, 0, pulselen);
    delayMicroseconds(5); // Decreased delay for faster movement
  }
  
  delay(5); // Delay at the bottom position
  
  // Phase 2: Go Up
  for (uint16_t pulselen = SERVOMIN; pulselen <= SERVOMAX; pulselen++) {
    pwm.setPWM(snum, 0, pulselen);
    delayMicroseconds(5); // Decreased delay for faster movement
  }
  
  delay(5); // Delay at the top position
}
