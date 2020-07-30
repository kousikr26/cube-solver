/*     Simple Stepper Motor Control Exaple Code
 *      
 *  by Dejan Nedelkovski, www.HowToMechatronics.com
 *  
 */
// defines pins numbers
const int stepPiny = 60; 
const int dirPiny = 61;   
const int Y_ENABLE_PIN=56;
const int stepPinx = 54; 
const int dirPinx = 55; 
const int X_ENABLE_PIN=38;
const int stepPinz = 46; 
const int dirPinz = 48;   
const int Z_ENABLE_PIN=62;
const int stepPine = 26; 
const int dirPine = 28; 
const int E_ENABLE_PIN=24;
const int stepPinf = 36; 
const int dirPinf = 34;   
const int F_ENABLE_PIN=30;
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPiny,OUTPUT); 
  pinMode(dirPiny,OUTPUT);
  pinMode(Y_ENABLE_PIN    , OUTPUT);
  digitalWrite(Y_ENABLE_PIN    , LOW);
  pinMode(stepPinx,OUTPUT); 
  pinMode(dirPinx,OUTPUT);
  pinMode(X_ENABLE_PIN    , OUTPUT);
  digitalWrite(X_ENABLE_PIN    , LOW);
  pinMode(stepPinz,OUTPUT); 
  pinMode(dirPinz,OUTPUT);
  pinMode(Z_ENABLE_PIN    , OUTPUT);
  digitalWrite(Z_ENABLE_PIN    , LOW);
  pinMode(stepPine,OUTPUT); 
  pinMode(dirPine,OUTPUT);
  pinMode(E_ENABLE_PIN    , OUTPUT);
  digitalWrite(E_ENABLE_PIN    , LOW);
  pinMode(stepPinf,OUTPUT); 
  pinMode(dirPinf,OUTPUT);
  pinMode(F_ENABLE_PIN    , OUTPUT);
  digitalWrite(F_ENABLE_PIN    , LOW);
  
}
void loop() {
   /*digitalWrite(dirPinx,LOW);// Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinx,HIGH); 
    delayMicroseconds(1000); 
    digitalWrite(stepPinx,LOW); 
    delayMicroseconds(1000); 
  }
  delay(1000); // One second delay*/
  //digitalWrite(dirPin2,HIGH);// Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinz,HIGH); 
    delayMicroseconds(1250); 
    digitalWrite(stepPinz,LOW); 
    delayMicroseconds(1250); 
  }
  delay(1000);/*
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinz,HIGH); 
    delayMicroseconds(1250); 
    digitalWrite(stepPinz,LOW); 
    delayMicroseconds(1250); 
  }delay(1000);// One second delay
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPine,HIGH); 
    delayMicroseconds(1250); 
    digitalWrite(stepPine,LOW); 
    delayMicroseconds(1250); 
  }delay(1000);// One second delay
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPinf,HIGH); 
    delayMicroseconds(1250); 
    digitalWrite(stepPinf,LOW); 
    delayMicroseconds(1250); 
  }delay(1000);// One second delay*/
  
  
}
