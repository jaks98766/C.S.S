#include <ezButton.h>

ezButton mySwitch(27);  // create ezButton object that attaches to ESP32 pin GPIO27
#define release_pin  32

void setup() {
  Serial.begin(9600);
  pinMode(release_pin, OUTPUT);
  digitalWrite(release_pin, LOW);
  mySwitch.setDebounceTime(50); // set debounce time to 50 milliseconds
}

void loop() {
  mySwitch.loop(); // MUST call the loop() function first
  if (mySwitch.isPressed()) {
    Serial.println("The switch: OFF -> ON");
  }
  if (mySwitch.isReleased()) {
    Serial.println("The switch: ON -> OFF");
  }

  int state = mySwitch.getState();
  if (state == HIGH) {
     digitalWrite(release_pin, LOW);
    Serial.println("The switch: OFF");
  } else {
    digitalWrite(release_pin, HIGH);
    Serial.println("The switch: ON");
  }
}
