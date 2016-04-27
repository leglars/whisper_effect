
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

#define NUMPIXELS 16

#define BRIGHTNESS 50

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 500;

void setup() {
  // put your setup code here, to run once:
  #if defined (__AVR_ATtiny85__)
    if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
  #endif

  strip.setBrightness(BRIGHTNESS);
  pixels.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<NUMPIXELS; i++){
  	
  }
}
