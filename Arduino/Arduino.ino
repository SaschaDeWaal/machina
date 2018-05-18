#include <OneWire.h> 
#include <DallasTemperature.h>
#include <Adafruit_NeoPixel.h>
#include <MPU6050_tockn.h>
#include <Arduino.h>
#include<Wire.h>

//pins:
const int pinLight1 = 0;
const int pinLight2 = 1;
const int pinLight3 = 2;
const int pinTempSensor1 = 3;
const int pinTempSensor2 = 4;
const int pinNeoPixels = 6;

const int updateTempEvery = 20;
const int numberOfNeoPixels = 31;
const float lightSensitive = 0.05f;

int index = 0;
int sensorUpdate = 0;
String msgContent = "";

int lightVoltage1[] = {0,0};
int lightVoltage2[] = {0,0};
int lightVoltage3[] = {0,0};


MPU6050 mpu6050(Wire);

OneWire tempSensorWire1(pinTempSensor1);
OneWire tempSensorWire2(pinTempSensor2);

DallasTemperature tempSensor1(&tempSensorWire1);
DallasTemperature tempSensor2(&tempSensorWire2);

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(numberOfNeoPixels, pinNeoPixels, NEO_GRB + NEO_KHZ800);

void setup() {
  
  pixels.begin();
  CalibrateWarningAnimation();
  
  Serial.begin(9600);
  
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets();
  tempSensor1.begin();
  tempSensor2.begin();

  CalibrateLight();

  delay(200);
  SetAllLights(0, 255, 0);
}

void loop() {
  mpu6050.update();

  sensorUpdate ++;

  if(sensorUpdate == updateTempEvery / 2){
    tempSensor1.requestTemperatures();
  }

  if(sensorUpdate > updateTempEvery){
    tempSensor2.requestTemperatures();
    sensorUpdate = 0;
  }

  index ++;
  String json = CreateJson(index);
  //Serial.println(json);
  
  //ReadSerial();

  delay(10);
}

String CreateJson(int messageIndex){
  int light1 = analogRead(pinLight1);
  int light2 = analogRead(pinLight2);
  int light3 = analogRead(pinLight3);
  
  String lightValue1 = (light1 < lightVoltage1[0] || light1 > lightVoltage1[1]) ? "false" : "true";//String(analogRead(pinLight1));
  String lightValue2 = (light2 < lightVoltage2[0] || light2 > lightVoltage2[1]) ? "false" : "true";//String(analogRead(pinLight2));
  String lightValue3 = (light3 < lightVoltage3[0] || light3 > lightVoltage3[1]) ? "false" : "true";//String(analogRead(pinLight3));

  String tempValue1 = String(tempSensor1.getTempCByIndex(0));
  String tempValue2 = String(tempSensor2.getTempCByIndex(0));
  String tempValue3 = String(mpu6050.getTemp());


  Serial.println(analogRead(pinLight1));
  if(lightValue1 == "true"){
    SetAllLights(255, 255, 0);
  }else{
    SetAllLights(255, 0, 0);
  }
  
  return "{" +
    CreateJsonLine("index", String(messageIndex)) + "," +
    CreateJosnArrayLine("gyroscoop", String(mpu6050.getGyroAngleX()) + "," + String(mpu6050.getGyroAngleY()) + "," + String(mpu6050.getGyroAngleZ())) + "," +
    CreateJosnArrayLine("accelerator", String(mpu6050.getAccX()) + "," + String(mpu6050.getAccY()) + "," + String(mpu6050.getAccZ())) + "," +
    CreateJosnArrayLine("temperature", tempValue1 + "," + tempValue2 + "," + tempValue3) + "," +
    CreateJsonLine("battery", "1024") + "," +
    CreateJosnArrayLine("light", lightValue1 + "," + lightValue2 + "," + lightValue3) +
  "}";
}

String CreateJsonLine(String key, String value){
  return "\"" + key + "\":" + value;
}

String CreateJosnArrayLine(String key, String arr){
   return "\"" + key + "\":" + "[" + arr + "]";
}

void CalibrateLight() {
  delay(100);

  int precision = 10;

  lightVoltage1[0] = analogRead(pinLight1);
  lightVoltage2[0] = analogRead(pinLight2);
  lightVoltage3[0] = analogRead(pinLight3);  

  for(int i = 1; i < precision; i++){
    lightVoltage1[0] += analogRead(pinLight1);
    lightVoltage2[0] += analogRead(pinLight2);
    lightVoltage3[0] += analogRead(pinLight3);
    delay(100);
  }

  lightVoltage1[1] = (lightVoltage1[0] / precision) * ( 1 + lightSensitive);
  lightVoltage2[1] = (lightVoltage2[0] / precision) * ( 1 + lightSensitive);
  lightVoltage3[1] = (lightVoltage3[0] / precision) * ( 1 + lightSensitive);

  lightVoltage1[0] = (lightVoltage1[0] / precision) * ( 1 - lightSensitive);
  lightVoltage2[0] = (lightVoltage2[0] / precision) * ( 1 - lightSensitive);
  lightVoltage3[0] = (lightVoltage3[0] / precision) * ( 1 - lightSensitive);
}

void ReadSerial(){
  while (Serial.available() > 0) {
    
    byte character = Serial.read();

    if(character == ';'){
      OnMessage(msgContent);
      msgContent = "";
    }else{
      msgContent += String(character);
    }
  }
}

void OnMessage(String message) {  
  if (message == ToByteString("team1")){
    SetAllLights(255, 255, 0);
  }

  if (message == ToByteString("team2")){
    SetAllLights(255, 0, 255);
  }

  if (message == ToByteString("team3")){
    SetAllLights(0, 255, 255);
  }
}

void SetAllLights(int r, int g, int b) {
  for(int i=0;i<numberOfNeoPixels;i++){
    pixels.setPixelColor(i, pixels.Color(r, g, b));
  }
  pixels.show();
}

const String ToByteString(const String str) {
  String byteString = "";
  for(int i = 0; i < str.length(); i++) {
    byteString += String((int)str[i]);
  }

  return byteString;
}

//light animations
void CalibrateWarningAnimation(){
  for(int amount = 0; amount < 3; amount++){
    for(int i = 0; i < 255; i++){
      SetAllLights(i, i, i);
      delay(5);
    }
  
    for(int i = 255; i > 0; i--){
      SetAllLights(i, i, i);
      delay(5);
    }
  }
  for(int i = 0; i < 255; i++){
     SetAllLights(i, i, i);
     delay(5);
  }
}


