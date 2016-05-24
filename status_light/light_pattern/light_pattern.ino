#include <Arduino.h>

#include "FastLED.h"
#define NUM_LEDS 16
#define PIN 6
  
CRGB leds[NUM_LEDS];
void setup() {Serial.begin(9600); FastLED.addLeds<NEOPIXEL,PIN>(leds, 16); }
void loop() { 
  processingPattern();
  // changeColor();
  }
    
void linearPattern() {
  for(int dot = 0; dot < 511; dot++) { 
    if( dot < 255) {
      for(int i =0; i < 16; i++) {
      leds[i].setHSV(235, 162, dot); 
      }
    FastLED.show();
    }else {
        for(int i =0; i < 16; i++) {
        leds[i].setHSV(235, 162, 511 - dot);
        }
    FastLED.show();
    }
  }
}

void breathPattern() {
  for(int dot = 0; dot < (256 * 4) - 1; dot++) {
    for(int i = 0; i < 16; i++) {
      leds[i].setHSV(235, 162, quadwave8(dot/4));
    }
    FastLED.show();
  }
}


void processingPattern() {
  for(int i = 0; i<16; i++) {
    leds[i].setHSV(235, 162, 255);
  }
  FastLED.show();
}

void changeColor() {
  for (int i=235; i>100; i--) {
    CRGB color = CHSV(i, 188, 188);
    fill_solid(leds, NUM_LEDS, color);
  }
  FastLED.show();
  delay(500);
  
}