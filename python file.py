import random
ninety = []
sixty = []
thirty =[]
tasks = []
points = 0



def addTask():
  task = input("Add task: ")
  tasks.append(task)
  print(f"➢ Task '{task}' added to the list.")
    
def listTasks():
  if not tasks:
    print("There are no tasks! Woohoo!")
    print("Add new tasks by choosing '1'")
  else:
    print("\n")  
    print("    ≫To-do≪")
    for index, task in enumerate(tasks):
      print(f"{index}. {task}")


def addBasicReward():
  thirty = input("Add your 30pt reward: ")
  print(f"3. '{thirty}' - 30pts ")
    
def addCommonReward():
  sixty = input("Add your 60pt reward: ")
  print(f"2. '{sixty}' - 60pts ")

def addRareReward():
  ninety = input("Add your 90pt reward: ")
  print(f"1. '{ninety}' - 90pts ")


if __name__ == "__main__":

  print("≫To-do list≪")
  while True:
    print("\n")
    print(f"       MENU  {points} pts")
    print("╔══════⋆⋅☆⋅⋆══════╗")
    print("𝟷. Add task        ")
    print("𝟸. Complete task   ")
    print("𝟹. Show tasks      ")
    print("𝟺. Exchange points ")
    print("𝟻. Exit            ")
    print("╚══════⋆⋅☆⋅⋆══════╝")

    choice = input("Enter: ")
    print("\n")

    if (choice == "1"):
      addTask()

 
    elif (choice == "2"):
      listTasks()
      taskToComplete = int(input("Which task have you completed? Enter its number: "))
      if taskToComplete >= 0 and taskToComplete < len(tasks):
          tasks.pop(taskToComplete)
          print(f"you had {points} points,")
          points = points + random.randint(18, 42)
          print(f"but now you have {points} points! choose 4 to exchange them")
      else:
          print(f"➢ Task {taskToComplete} was not found ✗")
        
    elif (choice == "3"):
      listTasks()

  
    elif (choice == "4"):
      print("              POINT EXCHANGE")
      print("╔══════════════════⋆⋅★⋅⋆══════════════════╗")
      print(f"        Available points:{points}")
      print(f"𝟷. {ninety} - 90pts ")
      print(f"𝟸. {sixty} - 60 pts")
      print(f"𝟹. {thirty} - 30 pts")
      print("𝟺. Change rewards")
      print("𝟻. Menu")
      print("╚══════════════════⋆⋅★⋅⋆══════════════════╝")
      shopChoice = (input("Enter: "))


      if (shopChoice == '1'):
          if points < 90:
               print('you do not have enough points! complete tasks to obtain more')
          else:
               points = points - 90
               print(f"you used 90 points and now have {points} points left")
               print("have fun! you deserve it!!")
      elif (shopChoice == '2'):
          if points < 60:
              print('you do not have enough points! complete tasks to obtain more')
          else:
               points = points - 60
               print(f"you used 60 points and now have {points} points left")
               print("enjoy your break! you got this :)")
      elif (shopChoice == '3'):
          if points < 30:
              print('you do not have enough points! complete tasks to obtain more')
          else:
               points = points - 30
               print(f"you used 30 points and now have {points} points left")
               print("remember to stretch and stay hydrated!")
              

      elif (shopChoice == '4'):
          election = input("Which reward would you like to change (1-3)?: ")       
          if (election == '1'):
              ninety = input('Add your new 90pt reward:')
          elif (election == '2'):
              sixty = input('Add your new 60pt reward:')
          elif (election == '3'):
              thirty = input('Add your new 30pt reward:')
          else:
              print('You have to choose a number between 1 and 3! You are now back to the menu') 
      else:
          print('\n')


    elif (choice == "5"):
      break
        
    else:
      print("Input must be a number between 1 and 5! Please try again")

print("Bye!")  