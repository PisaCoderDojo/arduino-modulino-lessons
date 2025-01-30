import sys
from time import sleep_ms

from modulino import ModulinoBuzzer

buzzer = ModulinoBuzzer()

pause = 200  # pause in millisecond
dotDuration = 50
lineDuration = 200

while True:
    print("Insert the message:")
    data = sys.stdin.readline()
    for l in data:
      print(l)
      if l == " ":
        sleep_ms(7 * pause)
      else:
        if l == "s":
          buzzer.tone(440, dotDuration, True)
          sleep_ms(pause)
          buzzer.tone(440, dotDuration, True)
          sleep_ms(pause)
          buzzer.tone(440, dotDuration, True)
          sleep_ms(pause)
        elif l == "o":
          buzzer.tone(440, lineDuration, True)
          sleep_ms(pause)
          buzzer.tone(440, lineDuration, True)
          sleep_ms(pause)
          buzzer.tone(440, lineDuration, True)
        sleep_ms(2 * pause)
