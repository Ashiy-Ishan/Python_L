import pygame.mixer
import sys
sound = pygame.mixer
sound.init()
def wait_finish(channel):
    while  channel.get_busy():
        pass

correct_count = 0
wrong_count   = 0
user_number   = 0

#user input get and sound play
def corrct_sound():
    c_sound = sound.Sound("./sound/correct.wav")
    wait_finish(c_sound.play())

def wrong_sound():
    c_sound = sound.Sound("./sound/wrong.wav")
    wait_finish(c_sound.play())
print("1 : correct\n2 : wrong\n0 : exit")
while True :
    print("\n")
    print("1. In Python, a variable can be assigned a value of one data type (e.g., an integer) and then later be reassigned a value of a different data type (e.g., a string).")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Python is a dynamically-typed language, which means the type of a variable is determined at runtime and \ncan change as the program executes.")
    else:
        wrong_sound()
        wrong_count = wrong_count + 1
    print("\n")
    print("2. The operators `is` and `==` can be used interchangeably in all situations to check for equality.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("The `is` operator checks for object identity (if two variables refer to the exact same object in memory), \nwhile `==` checks for value equality (if the objects have the same content).")
    print("\n")
    print("3. Python uses curly braces `{}` to define code blocks, such as the body of a loop or a function.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Python's syntax uniquely uses indentation (whitespace) to define the scope and structure of code blocks, \nmaking it a fundamental part of the language's design.")
    print("\n")
    print("4. A Python tuple, once created, can have its elements modified, added, or removed.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Tuples are an immutable data type, meaning they cannot be changed after they are created. \nThis immutability makes them reliable as keys in dictionaries.")
    print("\n")
    print("5. The `else` block can only be used with an `if` statement in Python.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Python allows an `else` block to be used with `for` and `while` loops. The `else` block executes when \nthe loop completes its full iteration without being terminated by a `break` statement.")
    print("\n")
    print("6. The expression `7 // 2` will result in `3.5`.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("The `//` operator performs floor division, which divides and then rounds the result \ndown to the nearest whole number, resulting in `3`.")
    print("\n")
    print("7. In Python, a dictionary key must be an immutable type.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Dictionary keys must be hashable, meaning their value cannot change. Immutable types like strings, numbers, and tuples can be keys, \nbut mutable types like lists cannot.")
    else:
        corrct_sound()
        wrong_count = wrong_count + 1
    print("\n")
    print("8. The variable name `my-variable` is a valid variable name in Python.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Python variable names can only contain letters, numbers, and underscores (`_`), and they cannot start with a number. \nThe hyphen `-` is not an allowed character.")
    print("\n")
    print("9. Strings in Python are mutable, meaning you can change a character at a specific index.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        wrong_count = wrong_count + 1
    else:
        corrct_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("Like tuples, strings are immutable. You cannot change a character within a string; instead, \nyou must create a new string with the desired modification.")
    print("\n")
    print("10. A function's default arguments are evaluated only once, when the function is defined.")
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number == 1:
        wrong_sound()
        correct_count = correct_count + 1
        print("Why Correct : ")
        print("This behavior can lead to unexpected results when a mutable object, like a list, is used as a default argument, \nas it will be the same list object for all subsequent calls.")
    else:
        corrct_sound()
        wrong_count = wrong_count + 1

print("\n")
print(f"Correct count : {correct_count}\nWrong count : {wrong_count}")