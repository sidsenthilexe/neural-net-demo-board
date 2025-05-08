from machine import Pin, ADC
import math, time
import neopixel

MAIN_LED_PIN = 11
CONF_LED_PIN = 3

main_leds = neopixel.NeoPixel(Pin(MAIN_LED_PIN), 4)
conf_leds = neopixel.NeoPixel(Pin(CONF_LED_PIN), 16)

switch_row = Pin(18, Pin.OUT)
switch_cols = [Pin(17, Pin.IN, Pin.PULL_DOWN), Pin(25, Pin.IN, Pin.PULL_DOWN), Pin(26, Pin.IN, Pin.PULL_DOWN), Pin(27, Pin.IN, Pin.PULL_DOWN)]
light = ADC(28)
temp = ADC(29)

light_raw = light.read_u16()
temp_raw = temp.read_u16()

def scan_matrix():
    switch_row.value(1)
    pressed_keys = []
    for col_index, col in enumerate(switch_cols):
        if col.value == 1:
            pressed_keys.append(col_index+1)
    switch_row.value(0)

    if pressed_keys:
        return pressed_keys

def normalize_value(value, min_value, max_value):
    return int((value - min_value) / (max_value - min_value))

def case_output(main_led_index, case, confidence):

    main_leds[main_led_index] = (255, 255, 255)
    main_leds.write()

    confidence_25, confidence_50, confidence_75, confidence_100 = case, case + 4, case + 8, case + 12
    if confidence >= 0 and confidence < 25:
        conf_leds[confidence_25] = (0, 255, 0)
    elif confidence >= 25 and confidence < 50:
        conf_leds[confidence_25] = (0, 255, 0)
        conf_leds[confidence_50] = (0, 255, 0)
    elif confidence >= 50 and confidence < 75:
        conf_leds[confidence_25] = (0, 255, 0)
        conf_leds[confidence_50] = (0, 255, 0)
        conf_leds[confidence_75] = (0, 255, 0)
    elif confidence >= 75 and confidence <= 100:
        conf_leds[confidence_25] = 0, 255, 0
        conf_leds[confidence_50] = (0, 255, 0)
        conf_leds[confidence_75] = (0, 255, 0)
        conf_leds[confidence_100] = (0, 255, 0)

while True:
    scan_matrix()
    time.sleep(0.01)