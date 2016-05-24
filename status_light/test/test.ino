#include<FastLED.h>

#define LED_PIN     6
#define BRIGHTNESS  255
#define LED_TYPE    NEOPIXEL
#define COLOR_ORDER GRB

#define NUM_LEDS 16

CRGB leds[NUM_LEDS];

static uint32_t x;
static uint32_t y;
static uint32_t z;

uint16_t speed = 1300;
uint16_t scale = 1500; 

uint8_t noise[135];

void setup() {
  
  LEDS.addLeds<LED_TYPE, LED_PIN>(leds, NUM_LEDS);
  LEDS.setBrightness(BRIGHTNESS);

  x = random16();
  y = random16();
  z = random16();
}

void fillnoise16() {

  for (int i = 0; i < NUM_LEDS; i++) {

    uint8_t data = inoise16(x , y + (i * scale), z) >> 8;
    noise[i] = data;
  }
  
  x += speed;
}

void mapNoiseToLEDs(){

  for (int i = 0; i < NUM_LEDS; i++) {

    uint8_t index = noise[i] >> 2;
    uint8_t bri =   noise[i];

    CRGB color = CHSV( index, 255, bri);

    leds[i] = color;
  }
}

void changeColor() {
  for (uint8_t hue = 255; hue > 0; hue--) {
    for (int i =0; i < NUM_LEDS; i++) {
        // uint8_t h = hue >> 8;
        uint8_t sut = noise[i] + 40;
        // uint8_t bri = noise[i+1];

        CRGB color = CHSV(hue, sut, 200);

        leds[i] = color;
    }
    LEDS.show();
    delay(20);
  }
}


void loop() {

  fillnoise16();

  // mapNoiseToLEDs();

  // LEDS.show();

  changeColor();
  delay(10);
}