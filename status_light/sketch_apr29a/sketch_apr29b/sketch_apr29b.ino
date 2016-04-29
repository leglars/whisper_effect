   #include "FastLED.h"
  #define NUM_LEDS 16
  #define PIN 6
  
        CRGB leds[NUM_LEDS];
        void setup() { FastLED.addLeds<NEOPIXEL,PIN>(leds, 16); }
        void loop() { 
//                for(int dot = 0; dot < 255*6; dot++) { 
//                  if( (dot/255)%2 == 0) {
//                    leds[1].setHSV(235, 162, dot);
//                    FastLED.show();
//                    }
//                    else {
//                      leds[1].setHSV(235, 162, 255-(dot%255));
//                      FastLED.show();
//                      }
//            
//            // clear this led for the next time around the loop
//        }
        leds[1].setHSV(235,231,200);
        FastLED.show();
        delay(1000);
        leds[1].fadeToBlackBy(64);
        FastLED.show();
        delay(2000);
        }
