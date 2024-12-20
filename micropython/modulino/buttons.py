
class ModulinoButtons():

  def __init__(self):
    self._current_buttons_status = [None, None, None]

    # Button callbacks
    self._on_button_a_press = None
    self._on_button_b_press = None
    self._on_button_c_press = None

  @property
  def on_button_a_press(self):
    """
    Returns the callback for the press event of button A.
    """
    return self._on_button_a_press

  @on_button_a_press.setter
  def on_button_a_press(self, value) -> None:
    """
    Sets the callback for the press event of button A.
    """
    self._on_button_a_press = value

  @property
  def on_button_b_press(self):
    """
    Returns the callback for the press event of button B.
    """
    return self._on_button_b_press

  @on_button_b_press.setter
  def on_button_b_press(self, value) -> None:
    """
    Sets the callback for the press event of button B.
    """
    self._on_button_b_press = value

  @property
  def on_button_c_press(self):
    """
    Returns the callback for the press event of button C.
    """
    return self._on_button_c_press

  @on_button_c_press.setter
  def on_button_c_press(self, value) -> None:
    """
    Sets the callback for the press event of button C.
    """
    self._on_button_c_press = value

  def printButtons(self):
    print("#########")
    print("#       #")
    print("# ", end="")
    print(self, end="")
    print(" #")
    print("#       #")
    print("#########")

  def update(self) -> bool:
    self.printButtons()
    pressed = input()
    if str.capitalize(pressed) == "A":
      self._current_buttons_status[0] = True
      self.printButtons()
      self._on_button_a_press()
      self._current_buttons_status[0] = False
    #   self.printButtons()
    elif str.capitalize(pressed) == "B":
      self._current_buttons_status[1] = True
      self.printButtons()
      self._on_button_b_press()
      self._current_buttons_status[1] = False
    elif str.capitalize(pressed) == "C":
      self._current_buttons_status[2] = True
      self.printButtons()
      self._on_button_c_press()
      self._current_buttons_status[2] = False
    else:
      raise ValueError("Invalid pressed button. Allowed keys are: 'A', 'B', 'C'")

    return True

  def __str__(self):
    a =  "a" if self._current_buttons_status[0] else "A"
    b =  "b" if self._current_buttons_status[1] else "B"
    c =  "c" if self._current_buttons_status[2] else "C"
    return f"{a} {b} {c}"

    return

  def is_pressed(self, index: int) -> bool:
    """
    Returns True if the button at the given index is currently pressed.

    Parameters:
        index (int): The index of the button. A = 0, B = 1, C = 2.
    """
    return self._current_buttons_status[index]

  @property
  def button_a_pressed(self) -> bool:
    """
    Returns True if button A is currently pressed.
    """
    return self.is_pressed(0)

  @property
  def button_b_pressed(self) -> bool:
    """
    Returns True if button B is currently pressed.
    """
    return self.is_pressed(1)

  @property
  def button_c_pressed(self) -> bool:
    """
    Returns True if button C is currently pressed.
    """
    return self.is_pressed(2)
