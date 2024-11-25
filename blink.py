from gpiozero import LED
from time import sleep

PinLED = LED(18)

while (True:):
  PinLED.on()
  sleep(1)
  PinLED.off()
  sleep(1)
