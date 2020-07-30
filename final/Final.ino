

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


//char first='0';
//char second='0';
char incomingData='0';

int delaytime=1000; //speed of stepper(microsec)
int delaytime2=500; //wait time after move(ms)

void rotate(int,int,int,int);

void setup() {
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
    incomingData=Serial.read();
    if (incomingData == 'D') {
      
      
      rotate(zstep,zdir,zenable,0);}
    
    else if (incomingData == 'L') {
      rotate(estep,edir,eenable,0);}
    else if (incomingData == 'R') {
       rotate(fstep,fdir,fenable,0);}
    else if (incomingData == 'F') {
       rotate(ystep,ydir,yenable,0);}
    else if (incomingData == 'B') {
       rotate(xstep,xdir,xenable,0);}
    else if (incomingData == 'd') {
      rotate(zstep,zdir,zenable,1);}
    else if (incomingData == 'l') {
      rotate(estep,edir,eenable,1);}
    else if (incomingData == 'r') {
       rotate(fstep,fdir,fenable,1);}
    else if (incomingData == 'f') {
       rotate(ystep,ydir,yenable,1);}
    else if (incomingData == 'b') {
       rotate(xstep,xdir,xenable,1);}
         
    }
  
}

void rotate(int stepPin,int dirPin,int enablePin,int dir){
  digitalWrite(enablePin    , LOW);
  digitalWrite(dirPin,dir);
  
  for(int x = 0; x < 50; x++) {
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(delaytime); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(delaytime); 
  }
  digitalWrite(enablePin, HIGH);
  delay(delaytime2); 
}


