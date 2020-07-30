/*     Simple Stepper Motor Control Exaple Code
 *      
 *  by Dejan Nedelkovski, www.HowToMechatronics.com
 *  
 */
// defines pins numbers
//x-D
//y-L
//z-R
//e-F
//f-B




const int xstep = 54;
const int xdir = 55; 
const int xenable=38;


const int ystep = 60;
const int ydir = 61; 
const int yenable=56;


const int zstep = 46;
const int zdir = 48; 
const int zenable=62;


const int estep = 26;
const int edir = 28; 
const int eenable=24;


const int fstep = 36;
const int fdir = 34; 
const int fenable=30;


char incomingData='0';
int delaytime=1000; //speed of stepper(microsec)
int delaytime2=1000; //wait time after move(ms)



void setup() {
  // Sets the two pins as Outputs
  Serial.begin(9600);
  pinMode(xstep,OUTPUT); 
  pinMode(xdir,OUTPUT);
  pinMode(xenable, OUTPUT);

  pinMode(ystep,OUTPUT); 
  pinMode(ydir,OUTPUT);
  pinMode(yenable, OUTPUT);
  
  pinMode(zstep,OUTPUT); 
  pinMode(zdir,OUTPUT);
  pinMode(zenable, OUTPUT);

  pinMode(estep,OUTPUT); 
  pinMode(edir,OUTPUT);
  pinMode(eenable, OUTPUT);

  pinMode(fstep,OUTPUT); 
  pinMode(fdir,OUTPUT);
  pinMode(fenable, OUTPUT);

  
  
}
void loop() {


  
  while (Serial.available()) {
    incomingData = Serial.read();
    if (incomingData == 'D') {
       D();}
    else if (incomingData == 'L') {
       L();}
    else if (incomingData == 'R') {
       R();}
    else if (incomingData == 'F') {
       F();}
    else if (incomingData == 'B') {
       B();}              
       
       
       
    }
    
  }


  
   
  
  

void D(){
  digitalWrite(xenable    , LOW);
  digitalWrite(xdir,HIGH);
  
  for(int x = 0; x < 50; x++) {
    digitalWrite(xstep,HIGH); 
    delayMicroseconds(delaytime); 
    digitalWrite(xstep,LOW); 
    delayMicroseconds(delaytime); 
  }
  digitalWrite(xenable, HIGH);
  delay(delaytime2); 
}
void L(){
  digitalWrite(yenable    , LOW);
  digitalWrite(ydir,HIGH);
  
  for(int x = 0; x < 50; x++) {
    digitalWrite(ystep,HIGH); 
    delayMicroseconds(delaytime); 
    digitalWrite(ystep,LOW); 
    delayMicroseconds(delaytime); 
  }
  digitalWrite(yenable, HIGH);
  delay(delaytime2); 
}
void R(){
  digitalWrite(zenable    , LOW);
  digitalWrite(zdir,HIGH);
  
  for(int x = 0; x < 50; x++) {
    digitalWrite(zstep,HIGH); 
    delayMicroseconds(delaytime); 
    digitalWrite(zstep,LOW); 
    delayMicroseconds(delaytime); 
  }
  digitalWrite(zenable, HIGH);
  delay(delaytime2); 
}
void F(){
  digitalWrite(eenable    , LOW);
  digitalWrite(edir,HIGH);
  
  for(int x = 0; x < 50; x++) {
    digitalWrite(step,HIGH); 
    delayMicroseconds(delaytime); 
    digitalWrite(estep,LOW); 
    delayMicroseconds(delaytime); 
  }
  digitalWrite(eenable, HIGH);
  delay(delaytime2); 
}
void B(){
  digitalWrite(fenable    , LOW);
  digitalWrite(fdir,HIGH);
  
  for(int x = 0; x < 50; x++) {
    digitalWrite(fstep,HIGH); 
    delayMicroseconds(delaytime); 
    digitalWrite(fstep,LOW); 
    delayMicroseconds(delaytime); 
  }
  digitalWrite(fenable, HIGH);
  delay(delaytime2); 
}


