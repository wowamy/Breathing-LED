int brightness1 = 0;
int fadeAmount1 = 5;
int brightness2 = 0;
int fadeAmount2 = 5;
int save1=0;
int times1=0;
int save2=0;
int times2=0;

void setup()
{
  Serial.begin(115200);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop() {
  times1=millis()-save1;
  times2=millis()-save2;

  if(times1>=30){
    if(brightness1<=0||brightness1>=255){
      fadeAmount1=-fadeAmount1;
    }
    brightness1=brightness1+fadeAmount1;

    if(brightness1>255){
      brightness1=255;
    }
     if(brightness1<0){
      brightness1=0;
    }
    analogWrite(3,brightness1);
    save1=millis();
  }
  if(times2>=50){
    if(brightness2<=0||brightness2>=255){
      fadeAmount2=-fadeAmount2;
    }
    brightness2=brightness2+fadeAmount2;

    if(brightness2>255){
      brightness2=255;
    }
     if(brightness2<0){
      brightness2=0;
    }
    analogWrite(5,brightness2);
    save2=millis();
  }
}