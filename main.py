#-----------------------------------------------------------
# Created by: Deepash Sunwar
# Created date: 09/03/23
# version = "1.0"
#-----------------------------------------------------------

# All the actions possible by the user
actions = ["heal", "attack", "defend", "quit"]

# Runs infinitely til its broken out of
while True:
  print("\n")  # line break for easier read for user
  # goes through all action within actions
  for action in actions:
    # prints them out
    print(f"- {action.capitalize()}")
  # Takes in user input and makes it lowercase ( easier for validation )
  print("\n")
  choice = input("Pick an action: ").lower()
  print("\n")
  # check if the user input is within the actions list
  if choice in actions:
    # if the user choice is quit, it will break out of loop
    if choice == "quit":
      print("goodbye!")
      break
    else:
      # else it will print the user input
      print(f"{choice.capitalize()}!")
  else:
    # if user input not in list, asks for valid input
    print("Please choose a valid action")
