x = 25

print("I am going to guess your age")

print("Are you " +\
      str(x) + \
      ", or are you older or younger? " )

guess = input()

while guess != "yes":

      if guess == "older":
            x = x + 1
            print(x)
            guess = input("Are you " +\
                              str(x) +\
                              ", or are you older or younger? " + "\n")
      elif guess == "younger":
            x = x - 1
            print(x)
            guess = input("Are you " +\
                              str(x) +\
                              ", or are you older or younger? " + str(x) + "\n")
print("I got it, you are ") + str(x)
