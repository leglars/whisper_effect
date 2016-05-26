#include <Arduino.h>

#include "FastLED.h"
#define NUM_LEDS 16
#define PIN 6
#define LED_TYPE NEOPIXEL

CRGB leds[NUM_LEDS];

int flag;         // a string to hold incoming data
boolean command = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  FastLED.addLeds<LED_TYPE, PIN>(leds, 16);
}

void loop() {
  // print the string when a newline arrives:
  if (command) {
  	if(flag == 'P') {
  		processingPattern();
  	}
  	if(flag == 'W') {
  		breathPattern();
    }
    if(flag == 'S'){
      command = false;
    }
  }else {
    changeColor();
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    flag = Serial.read();
    // add it to the inputString:
    
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    // if (inChar == '\n') {
    command = true;
    // }
  }
}

void showAll(CHSV color) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = color;
  }
  FastLED.show();
}

void showAll(CRGB color) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = color;
  }
  FastLED.show();
}

CRGB hsv2rgb(uint8_t hue, uint8_t sat, uint8_t bri) {
  CRGB color = CHSV(hue, sat, bri);
  return color;
}

void breathPattern() {
  for (int dot = 0; dot < (256 * 5) - 1; dot++) {
    showAll(CHSV(235, 162, quadwave8(dot / 5)));
  }
}

void processingPattern() {
  int a, b, c;
  for (int i = 0; i < 16; i++) {
    a = i + 1;
    b = i + 2;
    c = i + 3;
    if (a > 15) {
      a = a - 16;
    }
    if (b > 15) {
      b = b - 16;
    }
    if (c > 15) {
      c = c - 16;
    }
    leds[c].setHSV(235, 162, 63 * 4);
    leds[b].setHSV(235, 162, 63 * 3);
    leds[a].setHSV(235, 162, 63 * 2 + 30);
    leds[a].setHSV(235, 162, 63 * 1 + 40);
    if (i > 0) {
      leds[i - 1].setHSV(0, 0, 0);
    }
    else {
      leds[15].setHSV(0, 0, 0);
    }
    FastLED.show();
    delay(42);
  }
  Serial.println('D');
}

void changeColor() {
  for (uint8_t hue = 255; hue > 0; hue--) {
    for (int i =0; i < NUM_LEDS; i++) {
        // uint8_t h = hue >> 8
        // uint8_t bri = noise[i+1];

        CRGB color = CHSV(hue, 188, 188);

        leds[i] = color;
    }
    LEDS.show();
    delay(20);
  }
}