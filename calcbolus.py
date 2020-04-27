#import colorama module
from colorama import init

#initialize correction factor, target BG, and ICR variables
cfnum = 0
targetnum = 0
icrnum = 0

#introduce the CalcBolus program
from colorama import Fore, Back, Style
print(Fore.GREEN + "Welcome to CalcBolus! Please consult with your doctor before using this program.\n")
print(Style.RESET_ALL)

#get user input for blood glucose correction factor, target blood glucose, and insulin to carb ratio (ICR) 
print(Fore.YELLOW + "Please input your blood glucose correction factor number as determined by your doctor. For example, if you divide your current number minus your target number by 35, please enter 35.")
while cfnum == 0:
  corfact = input(Fore.LIGHTCYAN_EX + "BG Correction Factor: ")
  if corfact.isnumeric():
    cfnum = int(corfact)
  else:
    print(Fore.RED + "Invalid input. Please enter a numeric value.")

print(Fore.YELLOW + "\nPlease input your target blood glucose number. ")
while targetnum == 0:
  target = input(Fore.LIGHTCYAN_EX + "Target blood glucose: ")
  if target.isnumeric():
    targetnum = int(target)
  else:
    print(Fore.RED + "Invalid input. Please enter a numeric value.")

print(Fore.YELLOW + "\n Please enter your insulin to carb ratio. For example, if you take one unit for every 5 carbs, please enter 5.")
while icrnum == 0:
  icr = input(Fore.LIGHTCYAN_EX + "insulin to carb ratio: ")
  if icr.isnumeric():
    icrnum = int(icr)
  else:
    print(Fore.RED + "Inalid input. Please enter a numeric value.")


# Initialize PS factors and ask if default physical correction factors need to be changed
lowfact = 0
highfact = 0

print(Fore.YELLOW + "\nThe current default correction factor for hypoglycemia-causing events (like exercise) is .8 . Would you like to change this number?")
while lowfact == 0:
  changelow = input(Fore.MAGENTA + "Enter 'y' to change, or enter 'n' to keep: ")
  if changelow.lower() == 'y':
    lowfact = float(input(Fore.LIGHTCYAN_EX + "Enter your new correction factor for hypoglycemia-causing events as a decimal such as .5 or .92: "))
  elif changelow.lower() == 'n':
    lowfact = 0.8
  else:
    print(Fore.RED + "Invalid input. Please enter 'y' to change, or enter 'n' to keep.")

print(Fore.YELLOW + "\nThe current default correction factor for hyperglycemia-causing events like illness is 1.25 . Would you like to change this number?")
while highfact == 0:
  changehigh = input(Fore.MAGENTA + "Enter 'y to change, or enter 'n' to keep: ")
  if changehigh.lower() == 'y':
    highfact = float(input(Fore.LIGHTCYAN_EX + "Enter your new correction factor for hyperglycemia-causing events as a decimal such as 1.35 or 1.1: "))
  elif changehigh.lower() == 'n':
    highfact = 1.25
  else: 
    print(Fore.RED + "Invalid input. Please enter 'y' to change, or enter 'n' to keep.")

#initialize other variables for second round of user input
bgnum = 0
chonum = 0
exercise = 0 
alcintake = 0
illness = 0
meds = 0

#get user input on current blood glucose, carb intake, and phyiscal factors
while bgnum == 0:
  bg = input(Fore.LIGHTCYAN_EX + "\nPlease enter your latest blood glucose reading: ")
  if bg.isnumeric():
    bgnum = int(bg) 
  else:
     print(Fore.RED + "Invalid input. Please enter a numeric value.")

while chonum == 0:
  cho = input(Fore.LIGHTCYAN_EX + "\nPlease enter the carbohydrate count for your meal: ")
  if cho.isnumeric():
    chonum = int(cho)
  else:
     print(Fore.RED + "Invalid input. Please enter a numeric value.")

print(Fore.YELLOW + "\nFor the following questions, please enter 'y' for yes, or 'n' for no.")
while exercise == 0:
  exercise = input(Fore.LIGHTCYAN_EX + "\nWill you be doing, or have you done, any strenuous or prolonged phyiscal exercise today?: ")
  if exercise.lower() == 'y':
    exercise = 1
  elif exercise.lower() == 'n':
    exercise = 2
  else:
    print(Fore.RED + "Invalid input. Please enter either 'y' or 'n'.")

while alcintake == 0:
  alcintake = input(Fore.LIGHTCYAN_EX + "\nWill you have, or have you had, more than two low-carb alcoholic bevarages today?: ")
  if alcintake.lower() == 'y':
    alcintake = 1
  elif alcintake.lower() == 'n':
    alcintake = 2
  else:
    print(Fore.RED + "Invalid input. Please enter either 'y' or 'n'.")

while illness == 0: 
  illness = input(Fore.LIGHTCYAN_EX +  "\nAre you currently sick with a cold, the flu, or another phyiscla illness that cause hyperglycemic trends?: ")
  if illness.lower() == 'y':
    illness = 1
  elif illness.lower() == 'n':
    illness = 2
  else:
    print(Fore.RED + "Invalid input. Please enter either 'y' or 'n'.")

while meds == 0:
  meds = input(Fore.LIGHTCYAN_EX + "\nAre you currently taking any medications, like corticosteroids or blood pressure medication, that cause hyperglycemic trends?: ")
  if meds.lower() == 'y':
    meds = 1
  elif meds.lower() == 'n':
    meds = 2
  else:
    print(Fore.RED + "Invalid input. Please enter either 'y' or 'n'.")

#Calculate base insulin dosage, with and without physical factors
bolus = 0
while bolus == 0:
  if exercise and alcintake and illness and meds == 2:
    if targetnum >= bgnum:
      bolus = (chonum / icrnum)
      print(Fore.BLACK + Back.GREEN + "You should take", bolus, "units of insulin within the next 15 minutes.")
    else:
      bolus = (chonum / icrnum) + ((bgnum - targetnum)/ cfnum)
      print(Fore.BLACK + Back.GREEN + "You should take", bolus, "units of insulin within the next 15 minutes.")
  elif exercise or alcintake ==1:
    if targetnum >= bgnum:
      if illness or meds == 1:
        bolus = (chonum / icrnum) * (highfact * lowfact)
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
      else:
        bolus = (chonum / icrnum) * lowfact
        print(Fore.BLACK + Back.GREEN + "You should take", bolus, "units of insulin in the next 15 minutes.")
    else:
      if illness or meds == 1:
        bolus = ((chonum / icrnum) + ((bgnum - targetnum)/ cfnum))  * (highfact * lowfact)
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
      else:
        bolus = ((chonum / icrnum) + ((bgnum - targetnum)/ cfnum))  * lowfact
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
  elif illness or meds == 1:
    if targetnum >= bgnum:
      if exercise or alcintake == 1:
        bolus = (chonum / icrnum) * (highfact * lowfact)
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
      else:
        bolus = (chonum / icrnum) * highfact
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
    else:
      if exercise or alcintake == 1:
        bolus =  ((chonum / icrnum) + ((bgnum - targetnum)/ cfnum))  * (highfact * lowfact)
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
      else:
        bolus = ((chonum / icrnum) + ((bgnum - targetnum)/ cfnum))  * highfact
        print(Fore.BLACK + Back.GREEN + "You should take", bolus , "units of insulin within the next 15 minutes.")
  else:
    print(Fore.RED + "Sorry, the program cannot read your output. Please restart the program and try again.")
print(Style.RESET_ALL)



