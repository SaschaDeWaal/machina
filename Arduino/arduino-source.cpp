#include <Arduino.h>

int index = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  String json = CreateJson(index);

  Serial.println(json);
  index ++;
  delay(200);
}

String CreateJson(int messageIndex){
  return "{" +
    CreateJsonLine("index", String(messageIndex)) + "," +
    CreateJsonLine("gyroscoop", "[0, 0, 0]") + "," +
	CreateJsonLine("Accelerometer", "[0, 0, 0]") + "," +
	CreateJsonLine("temperature", "[20, 20, 20]") + "," +
	CreateJsonLine("battery", "1024") + "," +
	CreateJsonLine("light", "[1024, 20, 500]") +
  "}";
}

String CreateJsonLine(String key, String value){
  return "\"" + key + "\":" + "\"" + value + "\"";
}
