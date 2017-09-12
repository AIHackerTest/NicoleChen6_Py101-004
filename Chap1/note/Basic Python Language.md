## Basic Python Language ##

This is my notes after watching a Youtube channel conducted by Ameer Fazal. After listening his videos, I think I can understand my 7008 tutor's accent more...

### Assign value to variables ###

It is very simple to know: x = 1 means to assign the value 1 to x.

### Types of values ####

Note: Python variables don't have types, but the values do have. You can use the build-in function to check the type of a value such as: 

- type("Hello") -- **String**
- type(7) -- **Integers** (abbr:int)
- type(3.57) -- **Floating point**(abbr:float)
- type(3>5) -- **boolean**(bool)
- type(numbers = [1, 3, 5]) -- **list**
- type(numbers = 1, 3, 5) -- **tuple**
- type(fruits = {'a':'apples', 'b':'banana', 'o':'orange'}) -- **dictionary**(abbr:dict)
- type(a = {1, 3, 5}) -- **set**

In addition to check the type of values, for string which is a series of characters, you can use the len() to count the length of this string.


### Input and Output ###

You can use the build-in function print() to tell the computer what to dispaly.

You input your user name and password to access everywhere in life and this function is simply realized by another build-in function input().

    student_num = input ("Enter your number:")
    

This function means the computer receives messages from outer world. You can think it further, the data can also be stored and always ready to be retrived again. You can also write a program to plot a picture.

### Strings, Escape sequence and Comments ###

String is immutable, in other words, it is unable to be changed.

Sometimes, you don't want two strings in the same line, you can use \n between two strings.

    color = "red\ngreen"
    print (color)
    red
    green


A comment is a programmer-readable annotation in a computer program.

It starts with a # (hash symble).

    # Hi,I am a super hacker. I like comments which can help me to know 
    # what I mean by writing these codes because I had bad memory...
    # Sometimes, I just use comments to write dairies. 
    # The computer will ignore these comments anyway!


### Boolean values and Operators ###

The boolean data type is a data type with only two possible values: Ture and False.

Boolean operators: 


- and: True and False is False
- or: Ture or False is Ture
- not: not Ture is False

Actually there is a table for the combanations. Believe you can judge it by yourself or just test it by your computer.

### Rational Operators ###

A rational operator is an operator that tests or defines some kind of relation between two entities.

In fact, we all familiar with rational operators: <, >, <=, = etc. However, the problem is we do not familiar with EVERY English words..

In coding, to seperate the assingment use of =, we use bouble == to check equality. 1 != 3 means 1 is not equal to 3.

### The if statement (if elif else) ###

If statement is for decision making. For each decision, there will be an outcome.


    grades = int(input("Enter your grades in this exam:"))
    if grades >= 80:
        print ("HD")
    elif grades < 80 and grades >= 70:
        print ("D")
    elif grades < 70 and grades >= 50:
        print ("Passed")
    else:
        print ("Failed")


Then, running this little program in your Python3 or cmd, enter your grades, you can know your results.

### Lists ###

a = [1, 3, 5] is a list. Actually, we can put any types of values into one list:

    life = [1, "3", "Happy", False]

If you check the length of this list, it's 4. The order in programming is from 0. So, if you want to find the first value in this list, 

    life [0]

And you get the integer 1.

Lists are mutable. What you need to do is find the position of the value and reassign a new value.

### Tuples ###

a = (1, 3, 5) is a tuple. 

Tuples are just like lists, mixed value types are avaliable in tuples too. However, there are two difference: firstly they use different brakets: parenthese () for tuples and square brackets [] for lists. Secondly, lists are mutable while tuples are not.

### The for statement ###

For statement is for looping. You can get the data in a list or tuple one by one.

    a = ["apple", "banana", "orange"]
    for fruit in a:
        print (fruit)
    apple
    banana
    orange

### The while statement ###

It is a contorl and looping statement like the for statement.

    count = 2
    while count >= 0:
        print (count)
        count = count - 1

Guess what you would get? I think we've learned this in the math class in middle school.

### Functions ###

A function is a sequence of program instructions that perform a specific task, packaged as a unit.

We finally come to define functions! Bravo!

    def square(number):
        return number*number
    square(5)
    25

A function is also called a callable unit. You define a function, then you can call it anytime.

The functions are not confined in math functions. You can define everything you like. Just set what you want to get as a function.

### Recursion ###

A recursion is a function which **calls itself**. In Chinese, it's called "递归".

    def countdown(number):
        if number == 0:    # I am a comment, this is a Base Case
            print ("Completed")
        else:              # Recursive case
            print (number)
            countdown(number - 1)   # Recursive call
    countdown(3)
    3
    2
    1
    Completed
    


Recursion in computer science is a method where the solution to a problem depends on solutions to small instances of the same problem.

**Factorial function** is the product of all the positive integers from 1 to n. In Chinese, called "阶乘".

    def fact(number):
        if number == 0:
            return 1
        else:
            return number*fact(number-1)
    fact(3)
    6

### Dictionaries ###

A dictionary is an unordered collection of **key-value pairs**.

    fruits = {'a':'apples', 'b':'banana', 'o':'orange'}

Dictionaries are enclosed in curly braces {}.

Dictionaries are mutable.

    fruits ['a'] = 'abc'


    for key in fruits.keys():
        print (key)
    a
    b
    o
    for value in fruits.values():
        print (value)
    abc
    banana
    orange
    for item in fruits.items():
        print (tiem)
    ('a':'apples')
    (..)
    (..) # I know you know

### Sets ###

A set is an unordered collection of **unique elements**.

    a = {1, 3, 5}

Set is mutable.

    a.add(7)
    a
    {1, 3, 5, 7}
    a.remove(7)

### The break statement ###

To break out the smallest encolsing For or While loop.

    i = 0
    while i < 10:
         if i == 5:
         break
         print(i)
         i = i + 1


Fine, I just know them, but I don't know about them very much..



















 





