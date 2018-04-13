#include <MPU6050_tockn.h>
#include <Arduino.h>
#include<Wire.h>

MPU6050 mpu6050(Wire);

int index = 0;

//pins:
const int pinLight1 = 0;
const int pinLight2 = 1;
const int pinLight3 = 2;

//const int pinTempSensor1 = 3;
//const int pinTempSensor2 = 4;


void setup() {
  Serial.begin(115200);

  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets();
}

void loop() {
  mpu6050.update();

  index ++;
  String json = CreateJson(index);
  Serial.println(json);
  
  delay(200);
}

String CreateJson(int messageIndex){
  String lightValue1 = String(analogRead(pinLight1));
  String lightValue2 = String(analogRead(pinLight2));
  String lightValue3 = String(analogRead(pinLight3));

  String tempValue1 = "0";//String(analogRead(pinTempSensor1));
  String tempValue2 = "0";//String(analogRead(pinTempSensor2));
  
  return "{" +
    CreateJsonLine("index", String(messageIndex)) + "," +
    CreateJsonLine("gyroscoop", "[" + String(mpu6050.getGyroAngleX()) + "," + String(mpu6050.getGyroAngleY()) + "," + String(mpu6050.getGyroAngleZ()) + "]") + "," +
    CreateJsonLine("Accelerometer", "[" + String(mpu6050.getAccX()) + "," + String(mpu6050.getAccY()) + "," + String(mpu6050.getAccZ()) + "]") + "," +
    CreateJsonLine("temperature", "[2" + tempValue1 + "," + tempValue2 + "]") + "," +
    CreateJsonLine("battery", "1024") + "," +
    CreateJsonLine("light", "[" + lightValue1 + "," + lightValue2 + "," + lightValue3 + "]") +
  "}";
}

String CreateJsonLine(String key, String value){
  return "\"" + key + "\":" + "\"" + value + "\"";
}

