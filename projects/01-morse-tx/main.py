import sys
from time import sleep_ms

from modulino import ModulinoBuzzer

buzzer = ModulinoBuzzer()


duration = 200 # duration in millisecond

dit = duration
dah = 3 * duration

pause = duration
letterPause = 2 * duration
wordPause = 6 * duration  # in total 7 duration


while True:
    print("Insert the message:")
    data = sys.stdin.readline()
    for l in data:
      print(l)
      if l == " ":
        sleep_ms(wordPause)
      else:
        if l == "s":
          buzzer.tone(440, dit, True)
          sleep_ms(pause)
          buzzer.tone(440, dit, True)
          sleep_ms(pause)
          buzzer.tone(440, dit, True)
          sleep_ms(pause)
        elif l == "o":
          buzzer.tone(440, dah, True)
          sleep_ms(pause)
          buzzer.tone(440, dah, True)
          sleep_ms(pause)
          buzzer.tone(440, dah, True)
          sleep_ms(pause)
        sleep_ms(letterPause)
