#include <LiquidCrystal.h>
#include <Servo.h>
#include <IRremote.h>
//가변저항 a0
//air 57,58 y,n
//illum 55,56
Servo myServo;
Servo myServo2;
int servoPin1 = 12;
int servoPin2 = 13;
int buttons[] = {14, 15, 16, 17,18}; // 버튼 연결 핀
int pins_LED[] = {2, 3, 4, 5};
int trigPin_y = 6;
int echoPin_y = 7;
int trigPin_n = 8;
int echoPin_n = 9;
int linetracing1 = 10;
int linetracing2 = 11;
int state = -1;
int angle =0;
int angle1=0;
int RGB_LED[]={41,42,43};

LiquidCrystal lcd(44, 45, 46, 47, 48, 49);

int IRpin = 22;  
IRrecv irrecv(IRpin);
decode_results results;

void setup() {
  Serial.begin(9600); // 시리얼 통신 초기화
  for (int i = 0; i < 5; i++) { // 버튼 연결 핀을 입력으로 설정
    pinMode(buttons[i], INPUT);
    digitalWrite(buttons[i],LOW);
  }
  for (int i = 0; i < 4; i++) {
    pinMode(pins_LED[i], OUTPUT);
    digitalWrite(pins_LED[i], LOW);
  }
  for (int i = 0; i < 3; i++) {
    pinMode(RGB_LED[i], OUTPUT);
    digitalWrite(RGB_LED[i],HIGH);
  }

  pinMode(trigPin_y, OUTPUT);
  pinMode(echoPin_y, INPUT);
  pinMode(trigPin_n, OUTPUT);
  pinMode(echoPin_n, INPUT);
  myServo.attach(servoPin2); 
  myServo2.attach(servoPin1); 
  pinMode(linetracing1,INPUT);
  pinMode(linetracing2,INPUT);
//digitalWrite(linetracing1,LOW);
//digitalWrite(linetracing2,LOW);
  irrecv.enableIRIn();
  //lcd.noDisplay();
}


void textLCD(int a,int b,int c){
  lcd.clear();
  lcd.begin(16, 2);

  if (a==1){
    lcd.setCursor(0,1);
    if (c==0){
      lcd.print("ultrasonic");
    }
    if (c==1){
      lcd.print("illuminance");
    }
    if (c==2){
      lcd.print("linetracing");
    }
    if (c==3){
      lcd.print("air");
    }
    lcd.setCursor(13,1);
    lcd.print(b);
    lcd.setCursor(0,0);
    lcd.print("works correctly!");
  }else{
    lcd.setCursor(0,1);
    if (c==0){
      lcd.print("ultrasonic");
    }
    if (c==1){
      lcd.print("illuminance");
    }
    if (c==2){
      lcd.print("linetracing");
    }
    if (c==3){
      lcd.print("air");
    }
    lcd.setCursor(13,1);
    lcd.print(b);
    lcd.setCursor(0,0);
    lcd.print("broken sensor");
  }

}

void show_linetracing(int a,int b){
  if(a==1){
    int trace_y = digitalRead(linetracing1);
    int trace_n = digitalRead(linetracing2);
    Serial.print(trace_y);
    Serial.print(trace_n);
    if (abs(trace_y-trace_n)<=b){
      textLCD(1,b,2);
    }else{
      textLCD(2,b,2);
    }
  }
}

void show_ultrasonic(int a,int b){
  if (a==1){

    digitalWrite(trigPin_y, HIGH);
    digitalWrite(trigPin_y, LOW);
    
    float duration_y = pulseIn(echoPin_y, HIGH);
    float distance_y = duration_y * 340 / 10000 / 2;  

    digitalWrite(trigPin_n, HIGH);
    digitalWrite(trigPin_n, LOW);

    float duration_n = pulseIn(echoPin_n, HIGH);
    float distance_n = duration_n * 340 / 10000 / 2;  
    Serial.println(duration_y);
    Serial.println(duration_n);
    if (abs(distance_y-distance_n)<=b){
      textLCD(1,b,0);
    }else{
      textLCD(2,b,0);
    }
  }
}
void show_illum(int a,int b){

  int reading1 = analogRead(55); 
  int reading2 = analogRead(56); 
 
  if (abs(reading1-reading2)<=b){
    textLCD(1,b,1);
  }else{
    textLCD(2,b,1);
  }
}
void air(int a,int b){

  int value_y = analogRead(57);
  int value_n = analogRead(58);

  if (abs(value_y-value_n)<=b){
    textLCD(1,b,3);
  }else{
    textLCD(2,b,3);
  }
}

void show_angle(int a){
  if (a==1){
    if (angle == 90) { 
      angle = 0;
    }
    else if (angle == 0) {
      angle = 90;
    }
    myServo.write(angle);
  }
if (a==2){
    if (angle1 == 90) {
      angle1 = 0;
    }
    else if (angle1 == 0) {
      angle1 = 90;
    }
    myServo2.write(angle1);
  }
}

void reillum(){
  //for (int i = 0; i <= 255; i++) {
    analogWrite(RGB_LED[0], LOW);
    analogWrite(RGB_LED[1], LOW);
    analogWrite(RGB_LED[2], LOW);
   // delay(10);
  //}
}
void loop() {

          if (irrecv.decode(&results)) //IR리모컨 라이브러리 호출
            {
              //Serial.print(results.value);
            //Serial.print(1);
            lcd.clear();
            irrecv.resume();
            if(results.value==16724175){
              digitalWrite(pins_LED[0],HIGH);
              int i = 0;
              int cnt = 0;
            //int angle=0;
              while(i<10){
                int howmuch = map(analogRead(A0),0,1023,0,99); 
                show_ultrasonic(1,howmuch);
                //time_previous = millis();
                delay(1000);
                show_angle(1);
                i=i+1;
                
              }
              //if(angle==90){
                //angle=0;
                //myServo.write(angle);
             // }
            }; // 버튼 상태 출력
            if(results.value==16718055){
              digitalWrite(pins_LED[1],HIGH);
              int i=0;
              int angle1=0;
              while(i<10){
                int howmuch = map(analogRead(A0),0,1023,0,99); 
                show_linetracing(1,howmuch);
                //Serial.print(howmuch);
                delay(1000);
                show_angle(2);
                i=i+1;
              }
            }; // 버튼 상태 출력
            if(results.value==16743045){
              digitalWrite(pins_LED[2],HIGH);
              int i=0;
              while(i<10){
                analogWrite(RGB_LED[0], 0);
                analogWrite(RGB_LED[1], 0);
                analogWrite(RGB_LED[2], 0);
                //Serial.print(analogRead(RGB_LED[0]));
                //Serial.print( analogRead(RGB_LED[1]));
                //Serial.println( analogRead(RGB_LED[2]));             
                int howmuch = map(analogRead(A0),0,1023,0,199); 
                show_illum(1,howmuch);
                delay(1000);
                i=i+1;
              }
                analogWrite(RGB_LED[0], 255);
                analogWrite(RGB_LED[1], 255);
                analogWrite(RGB_LED[2], 255);
            }; // 버튼 상태 출력
            if(results.value==16716015){
              digitalWrite(pins_LED[3],HIGH);
              int i=0;
              while(i<10){
                int howmuch = map(analogRead(A0),0,1023,0,99); 
                air(1,howmuch);
                delay(1000);
                i=i+1;
              }
        };
    }
  //delay(1000);
}
