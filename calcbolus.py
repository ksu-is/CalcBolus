#initialize variables
lowfact = 0
highfact = 0

#introduce the program
print("\nWelcome to CalcBolus! Please consult with your doctor before using this program.\n")

#get user input for blood glucose correction factor and ask if default physical correction factors need to be changed. 
print("Please input your blood glucose correction factor number as determined by your doctor. For example, if you divide your current number minus your target number by 35, please enter 35.")
corfact = int(input("BG Correction Factor: "))

print("\nThe current default correction factor for hypoglycemia-causing events (like exercise) is .8 . Would you like to change this number?")
while lowfact == 0:
  changelow = input("Enter 'y' to change, or enter 'n' to keep: ")
  if changelow.lower() == 'y':
    lowfact = float(input("Enter your new correction factor for hypoglycemia-causing events as a decimal such as .5 or .92: "))
  elif changelow.lower() == 'n':
    lowfact = 0.8
  else:
    print("That is not a valid input. Please enter 'y' to change, or enter 'n' to keep.")

print("\nThe current default correction factor for hyperglycemia-causing events like illness is 1.25 . Would you like to change this number?")
while highfact == 0:
  changehigh = input("Enter 'y to change, or enter 'n' to keep: ")
  if changehigh.lower() == 'y':
    highfact = float(input("Enter your new correction factor for hyperglycemia-causing events as a decimal such as 1.35 or 1.1: "))
  elif changehigh.lower() == 'n':
    highfact = 1.25
  else: 
    print("That is not a valid input. Please enter 'y' to change, or enter 'n' to keep.")


#get user input on current blood glucose, carb intake, and phyiscal factors
bg = int(input("\nPlease enter your latest blood glucose reading: "))
carbs = int(input("Please enter your carbohydrate count for your meal: "))
print("\nFor the following questions, please enter 'y' for yes, or 'n' for no.")
exercise = input("Will you be doing, or have you done, any strenuous or prolonged phyiscal exercise today?: ")
alcintake = input("Will you have, or have you had, more than two low-carb alcoholic bevarages today?: ")
illness = input("Are you currently sick with a cold, the flu, or another phyiscla illness that cause hyperglycemic trends?: ")
meds = input("Are you currently taking any medications, like corticosteroids or blood pressure medication, that cause hyperglycemic trends?: ")


#Read Inputs
while (forward == "no"):
  product = str(input("Name of product: "))

  while (product.isalpha() == False):
    print ("Not a valid string. Please enter a string.\n")
    product = str(input("Name of product: "))

  price = int(input("Price: "))
  
  quantity = int(input("Quantity: "))

  calculate = price * quantity



  forward = input("Enter 'yes' if you're done or 'no' to add another: ")

  print("\n\n")
    
#Calculate

while 
x = 0

while 

print ("\n")
print("--------------------------------")
print ("Total:                        "   + str(total))