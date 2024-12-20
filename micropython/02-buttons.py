
from modulino import ModulinoButtons


buttons = ModulinoButtons()


buttons.on_button_a_press = lambda : print("Button A pressed")
buttons.on_button_b_press = lambda : print("Button B pressed")
buttons.on_button_c_press = lambda : print("Button C pressed")

while True:
    buttons_state_changed = buttons.update()
