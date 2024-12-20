
from modulino import ModulinoButtons


buttons = ModulinoButtons()


buttons.on_button_a_press = lambda : print("Button A pressed")
buttons.on_button_b_press = lambda : print("Button B pressed")
buttons.on_button_c_press = lambda : print("Button C pressed")

while True:
    buttons_state_changed = buttons.update()
    print("is pressed", buttons_state_changed)
    if(buttons_state_changed):
      led_a_status = buttons.is_pressed(0) # Turn LED A on if button A is pressed
      led_b_status = buttons.is_pressed(1) # Turn LED B on if button B is pressed
      led_c_status = buttons.is_pressed(2) # Turn LED C on if button C is pressed
      print("is pressed", led_a_status, led_b_status, led_c_status)
    #   buttons.set_led_status(led_a_status, led_b_status, led_c_status)
