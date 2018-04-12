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
    CreateJsonLine("sensor1", "false") +
  "}";
}

String CreateJsonLine(String key, String value){
  return "\"" + key + "\":" + "\"" + value + "\"";
}
