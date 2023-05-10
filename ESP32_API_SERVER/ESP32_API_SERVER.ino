#include <WiFi.h>
#include <WebServer.h>
#include <WiFiMulti.h>
#include <ArduinoJson.h>
#include "DHT11_ESP32.h"

DHT11_ESP32 dht(4);
float x , y ;


const char* ssid = "Abhishek";
const char* password = "NewPassword";

WiFiMulti wifiMulti;

WebServer server(80);

int data[2];

void handleRoot() {
  String webPage = "<script> setTimeout('location.reload(true);', 1000);</script>";
  String Json;

  // Allocate JsonBuffer
  StaticJsonBuffer<1024> jsonBuffer;

  JsonObject& root = jsonBuffer.createObject();
  root["battery_volt"] = data[0];
  root["pos_x"] = data[1];

  root.printTo(Json);  //Store JSON in String variable
  server.send(200, "text/html", Json + webPage);
}

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println();

  wifiMulti.addAP(ssid, password); // Connect to Wi-Fi network

  while (wifiMulti.run() != WL_CONNECTED) {
    delay(100);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);

  server.begin(); //Start web server
  Serial.println("HTTP server started");
}

void loop() {
  //Handle Client requests
  float temperature_c = dht.getTEMP();
  float humidity = dht.getHUM();
  Serial.println(temperature_c);
  Serial.println(humidity);
  data[1]= humidity ;
  data[0] = temperature_c ;
  delay(2000);


  //  if (Serial.available() > 0) {
  //
  //
  ////    data[0] = x;
  //
  //
  ////    data[1]= y;
  //
  //
  //
  //
  ////    for (int i = 0; i < 2; i++) {
  ////      data[i] = Serial.read();
  ////    }
  ////  }
  //
  //}
  server.handleClient();
}
