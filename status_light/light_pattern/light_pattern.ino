#include <Arduino.h>

#include "FastLED.h"
#define NUM_LEDS 16
#define PIN 6
#define LED_TYPE NEOPIXEL

CRGB leds[NUM_LEDS];

static uint32_t x;
static uint32_t y;
static uint32_t z;

uint16_t speed = 1900;
uint16_t scale = 3957; 

uint8_t noise[16];

void setup() {
  Serial.begin(9600);
  FastLED.addLeds<LED_TYPE, PIN>(leds, 16);
  x = random16();
  y = random16();
  z = random16();

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

void linearPattern() {
  for (int dot = 0; dot < 511; dot++) {
    if ( dot < 255) {
      showAll(CHSV(235, 162, dot));
    } else {
      showAll(CHSV(235, 162, 511-dot));
    }
  }
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
}


void processing2done() {
  int one = 1;
  uint8_t hue, sat, bri;
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i].setHSV(235, 162, 63 * 4);
    delay(42);
    FastLED.show();
    one--;
  }


  // sat = 162;
  // bri = 63 * 4;
  // for (hue = 235; hue > 100; hue--) {
  //   if (sat <= 188) {
  //     sat++;
  //   }
  //   if (bri > 188) {
  //     bri--;
  //   }
  //   for(int i=0; i<NUM_LEDS; i++) {

  //     CRGB color = CHSV(hue, sat, bri);
      
  //     leds[i] = color;

  //     }
  //   delay(1);
  //   FastLED.show();
  // }

  // delay(1000);
}


void fillnoise16() {

  for (int i = 0; i < NUM_LEDS; i++) {

    uint8_t data = inoise16(x , y + (i * scale), z + (2*i * speed -1)) >> 8;
    noise[i] = data;
    
    Serial.println(noise[i]);
  }
  

}

void hueWheel() {

  for (uint8_t hue = 255; hue > 0; hue--) {
    showAll(hsv2rgb(hue, 200, 200));
    delay(20);
  }
}

void changeColor() {
  fillnoise16();
  for (uint8_t hue = 255; hue > 0; hue--) {
    for (int i =0; i < NUM_LEDS; i++) {
        // uint8_t h = hue >> 8;
        uint8_t sat = noise[i];
        // uint8_t bri = noise[i+1];

        CRGB color = CHSV(hue, sat, 200);

        leds[i] = color;
    }
    LEDS.show();
    delay(20);
  }
}


void loop() {
  // for (int i = 0; i < 5; i++) {
  //   processingPattern();
  // }
  // // changeColor();
  // processing2done();
  // delay(1000);
  // // linearPattern();
  // //  checkColor();
  // //  delay(1000);
  //  // breathPattern();
  //  changeColor();

  fillnoise16();
  delay(100000);
}