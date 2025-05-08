from machine import Pin, ADC
import math

switch_rows = [Pin(18, Pin.OUT)]
switch_cols = [Pin(17, Pin.IN, Pin.PULL_DOWN), Pin(25, Pin.IN, Pin.PULL_DOWN), Pin(26, Pin.IN, Pin.PULL_DOWN), Pin(27, Pin.IN, Pin.PULL_DOWN)]
light = ADC(28)
temp = ADC(29)