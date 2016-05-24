#include <Arduino.h>

#include "FastLED.h"
#define NUM_LEDS 16
#define PIN 6

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(9600);
  FastLED.addLeds<NEOPIXEL, PIN>(leds, 16);
}
void loop() {
  for (int i = 0; i < 5; i++) {
    processingPattern();
  }
  // changeColor();
  processing2done();
  delay(1000);
  //  linearPattern();
  //  checkColor();
  //  delay(1000);
  //  breathPattern();
}

void checkColor() {
  for (int i = 0; i < 16; i++) {
    leds[i].setHSV(100, 188, 188);
  }
  FastLED.show();
}

void linearPattern() {
  for (int dot = 0; dot < 511; dot++) {
    if ( dot < 255) {
      for (int i = 0; i < 16; i++) {
        leds[i].setHSV(235, 162, dot);
      }
      FastLED.show();
    } else {
      for (int i = 0; i < 16; i++) {
        leds[i].setHSV(235, 162, 511 - dot);
      }
      FastLED.show();
    }
  }
}

void breathPattern() {
  for (int dot = 0; dot < (256 * 5) - 1; dot++) {
    for (int i = 0; i < 16; i++) {
      leds[i].setHSV(235, 162, quadwave8(dot / 5));
    }
    FastLED.show();
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
}

void processing2done() {
  int one = 1;
  uint8_t hue, sat, bri;
    Serial.println("yes");
    for (int i = 0; i < NUM_LEDS; i++) {
      leds[i].setHSV(235, 162, 63 * 4);
      delay(42);
    FastLED.show();
    one--;
  }
  sat = 162;
  bri = 63 * 4;
  for (hue = 235; hue > 100; hue--) {
    if (sat <= 188) {
      sat++;
    }
    if (bri > 188) {
      bri--;
    }
    for(int i=0; i<NUM_LEDS; i++) {

      CRGB color = CHSV(hue, sat, bri);
      
      leds[i] = color;

      }
    delay(1);
    FastLED.show();
  }

  delay(1000);
}

void changeColor() {
  for (uint8_t hue = 235; hue > 100; hue--) {
    CRGB color = CHSV(hue, 188, 188);
    fill_solid(leds, NUM_LEDS, color);
  }
  FastLED.show();
  delay(500);
  
}
