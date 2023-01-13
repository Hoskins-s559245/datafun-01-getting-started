"""
Optional bonus. See course site for details.
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Assignment 1, Module 1, Task 6

"""

import random

# Change the name below to a name of your choice

name = "The Great Hunter Joshua"

# Fix the code below to print the name using an f-string

print()
print("Hello, I'm", name, "your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

user_choice = str(input("Enter wolf, eagle or snake :"))


# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!


if user_choice == buddy_choice:
    print("We tied!")

elif user_choice == "wolf" :
    if buddy_choice == "eagle" :
        print("The Wolf scares the Eagle.")
    else:
        print ("The Snake Bites the Wolf!")
elif user_choice == "eagle" :
    if buddy_choice == "wolf" :
        print ("The Wolf Scares the Eagle")
    else:
        print("The Eagle grabs the snake")
elif user_choice == "snake" :
    if buddy_choice == "wolf" :
        print("The Snake Bites the Wolf!")
    else: 
        print ("The Eagle Grabs the Snake")

# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""

PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-01-getting-started> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-01-getting-started/xtra_p1.py

Hello, I'm The Great Hunter Joshua your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.
Enter wolf, eagle or snake :wolf

You said wolf.
I said snake.

The Snake Bites the Wolf!
PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-01-getting-started> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-01-getting-started/xtra_p1.py

Hello, I'm The Great Hunter Joshua your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Enter wolf, eagle or snake :eagle

You said eagle.
I said eagle.

We tied!
PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-01-getting-started> & C:/Users/Hoski/miniconda3/python.exe c:/Users/Hoski/Desktop/NWMS/GIT/datafun-01-getting-started/xtra_p1.py

Hello, I'm The Great Hunter Joshua your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Enter wolf, eagle or snake :snake

You said snake.
I said wolf.

The Snake Bites the Wolf!
PS C:\Users\Hoski\Desktop\NWMS\GIT\datafun-01-getting-started>


"""
