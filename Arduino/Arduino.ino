#include <OneWire.h> 
#include <DallasTemperature.h>
#include <MPU6050_tockn.h>
#include <Arduino.h>
#include<Wire.h>

//pins:
const int pinLight1 = 0;
const int pinLight2 = 1;
const int pinLight3 = 2;
const int pinTempSensor1 = 3;
const int pinTempSensor2 = 4;
const int updateTempEvery = 20;

int index = 0;
int sensorUpdate = 0;

int lightVoltage1 = 0;
int lightVoltage2 = 0;
int lightVoltage3 = 0;

MPU6050 mpu6050(Wire);

OneWire tempSensorWire1(pinTempSensor1);
OneWire tempSensorWire2(pinTempSensor2);

DallasTemperature tempSensor1(&tempSensorWire1);
DallasTemperature tempSensor2(&tempSensorWire2);

void setup() {
  Serial.begin(115200);

  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets();
  tempSensor1.begin();
  tempSensor2.begin();

  CalibrateLight();
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
  Serial.println(json);
  
  delay(0);
}

String CreateJson(int messageIndex){
  String lightValue1 = (analogRead(pinLight1) < lightVoltage1) ? "false" : "true";//String(analogRead(pinLight1));
  String lightValue2 = (analogRead(pinLight2) < lightVoltage2) ? "false" : "true";//String(analogRead(pinLight2));
  String lightValue3 = (analogRead(pinLight3) < lightVoltage3) ? "false" : "true";//String(analogRead(pinLight3));

  String tempValue1 = String(tempSensor1.getTempCByIndex(0));
  String tempValue2 = String(tempSensor2.getTempCByIndex(0));
  String tempValue3 = String(mpu6050.getTemp());
  
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

  lightVoltage1 = analogRead(pinLight1);
  lightVoltage2 = analogRead(pinLight2);
  lightVoltage3 = analogRead(pinLight3);

  for(int i = 1; i < precision; i++){
    lightVoltage1 += analogRead(pinLight1);
    lightVoltage2 += analogRead(pinLight2);
    lightVoltage3 += analogRead(pinLight3);
    delay(100);
  }

  lightVoltage1 = (lightVoltage1 / precision) * 0.8;
  lightVoltage2 = (lightVoltage2 / precision) * 0.8;
  lightVoltage3 = (lightVoltage3 / precision) * 0.8;
}


