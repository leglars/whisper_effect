#include <Arduino.h>

#include "FastLED.h"
#define NUM_LEDS 16
#define PIN 6
#define LED_TYPE NEOPIXEL

CRGB leds[NUM_LEDS];

int flag;         // a string to hold incoming data
boolean command = false;  // whether the string is complete

static uint32_t x;
static uint32_t y;
static uint32_t z;

uint16_t speed = 1900;
uint16_t scale = 3957;

uint8_t noise[16];


void setup() {
  // initialize serial:
  Serial.begin(19200);
  FastLED.addLeds<LED_TYPE, PIN>(leds, 16);
  x = random16();
  y = random16();
  z = random16();
}

void loop() {
  // print the string when a newline arrives:
  if (command) {
    // processing: I am recording?
  	if(flag == 'P') {
  		processingPattern();
    }
    if(flag == 'D') {
      processing2done();
      flag = 'd';
    }
    if(flag == 'd') {
      donePattern();
    }
  	// working
  	if(flag == 'W') {
  		breathPattern();
    }
    // recording
    if(flag == 'I'){
      recordPattern();
    }

    // Engaging people, waiting start to recording
    if(flag == 'E') {
      linearPattern();
    }
    // system standby
    if(flag == 'S') {
      standbyPattern();
    }
    // people leaving and reset the status
    if(flag == 'R'){
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


// The following is the different light pattern

// The basic function
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


// patterns start from here
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

void recordPattern() {
  for (int dot = 0; dot < (256 * 2) - 1; dot++) {
    showAll(CHSV(0, 255, quadwave8(dot / 2)));
  }
}

void standbyPattern() {
  for(int i = 0; i < 2; i++) {
    for (int dot = 0; dot < 255; dot++) {
      showAll(CHSV(26, 216, quadwave8(dot)));
    }
    delay(20);
  }

  for (int dot = 0; dot < (256 * 2) - 1; dot++) {
    showAll(CHSV(26, 216, quadwave8(dot / 2)));
  }
  delay(20);
  
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

void processing2done() {
  int one = 1;
  uint8_t hue, sat, bri;

  // continue processing circle -- last circle
  // fill in all
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i].setHSV(235, 162, 63 * 4);
    delay(42);
    FastLED.show();
    one--;
  }

  // fade out the red to half brightness
  sat = 162;

  for (bri = 63 * 4; bri > 63; bri--){
    sat--;
    showAll(CHSV(235, sat, bri));
    delay(1);
  }


  // change color into green

  for (bri = 63; bri < 188 + 1; bri++) {
    showAll(CHSV(100, 188, bri));
    delay(1);
  }
}

void donePattern() {
  for (int dot = -188; dot < 189; dot++) {
    if ( dot < 0 ) {
      showAll(CHSV(100, 188, 0 - dot));
    } else {
      showAll(CHSV(100, 188, dot));
    }
  }
}

void fillnoise16() {

  for (int i = 0; i < NUM_LEDS; i++) {

    uint8_t data = inoise16(x , y + (i * scale), z + (2*i * speed -1)) >> 8;
    noise[i] = data;
  }
  

}
  

void changeColor() {
  fillnoise16();
  for (uint8_t hue = 255; hue > 0; hue--) {
    for (int i =0; i < NUM_LEDS; i++) {
        uint8_t sat = noise[i];
        // uint8_t bri = noise[i+1];

        CRGB color = CHSV(hue, sat, 150);

        leds[i] = color;
    }
    LEDS.show();
    delay(14);
  }
}
