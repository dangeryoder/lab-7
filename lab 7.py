# 25pt

odd = 1
while (odd <= 300):
    if odd % 2 == 0:
        print odd - 1
    odd = odd + 1
    
# 25pt

List = ["ya", "ye", "yo", "yeah", "yea", "no", "na", "nah", "nope", "yep"]
import random
rand = random.randstr(0, len(List) - 1)
Loop = True
while (Loop):
    user = raw_input()
    Loop = Loop + 1
print List(rand)
