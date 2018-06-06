#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN            6
#define NUMPIXELS      22

float r = 1;
float g = 1;
float b = 0;

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 500; // delay for half a second

void setup() {
  // This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
#if defined (__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  // End of trinket special code

  pixels.begin(); 
}

void loop() {
  for(int i=0;i<12;i++){
    pixels.setPixelColor(i, pixels.Color(100 * r,100 * g,100 * b));
    pixels.setPixelColor(NUMPIXELS - i, pixels.Color(100 * r,100 * g,100 * b));
    pixels.show();
    delay(80);
    pixels.setPixelColor(i, pixels.Color(255 * r, 255 * g,255 * b));
    pixels.setPixelColor(NUMPIXELS - i, pixels.Color(255 * r, 255 * g,255 * b));
    pixels.show();
  }
}
