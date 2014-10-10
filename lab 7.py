# 25pt

odd = 1
while (odd <= 300):
    if odd % 2 == 0:
        print odd - 1
    odd = odd + 1
    
# 25pt

List = ["ya", "ye", "yo", "yeah", "yea", "no", "na", "nah", "nope", "yep"]
x = 0
while(x < len(List)):
    print List[x]
    x = x + 1

# 50pt
import random
rand = random.randint(0,50)
guess = 0
while(guess!= rand):
    print "Pick a number between 1 and 50"
    guess = int(raw_input())
    if guess > rand:
        print "too high!"
    elif guess < rand:
        print "too low!"
    elif guess == rand:
        print "nice!"
        
        