# coding: utf-8
import random  #调用随机模块
min = 0
max = 20
num = random.randint(0, 20) #从1-20随机生成一个数，并赋给num

#Welcome Screen
print ("Now, let's play an easy but fun game!\n")
print ("Guess a number in [0,20].")
print ("You have 10 chances.")

print ("\n")

guess = int (input ("Enter a number:") )#输入玩家的猜数

guesses = 0
if guess > num:
    print ("Too hign!")
elif guess < num:
    print ("Too low!")
else:
    print ("You're awesome, correct in the first time")

while guess != num and guesses < 9:
    time = 9 - guesses
    print ("You have %s times left." % time )
    guesses += 1
    guess = int(input("Enter a number:"))
    if guess > num:
        print ("Too hign!")
    elif guess < num:
        print ("Too low!")
    else:
        print ("You're correct in the %s time" % time)

if guess != num:
    print ("You lose the game!")
