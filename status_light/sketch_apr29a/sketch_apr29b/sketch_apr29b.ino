   #include "FastLED.h"
  #define NUM_LEDS 16
  #define PIN 6
  
        CRGB leds[NUM_LEDS];
        void setup() { FastLED.addLeds<NEOPIXEL,PIN>(leds, 16); }
        void loop() { 
                for(int dot = 0; dot < 511; dot++) { 
                  if( dot < 255) {
                    for(int i =0; i < 16; i++) {
                    leds[i].setHSV(235, 162, dot);
                    
                        }
                        FastLED.show();
                  }
                    else {
                      for(int i =0; i < 16; i++) {
                      leds[i].setHSV(235, 162, 511 - dot);

                      }
                    FastLED.show();
               
                      
                    }
            
            // clear this led for the next time around the loop
        }
//        leds[1].setHSV(235,231,200);
//        FastLED.show();
//        delay(1000);
//        leds[1].fadeToBlackBy(64);
//        FastLED.show();
//        delay(2000);
        }
