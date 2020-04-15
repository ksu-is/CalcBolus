
#introduce the program
print("\nWelcome to CalcBolus! Please consult with your doctor before using this program.\n")

#get user input for blood glucose correction factor and ask if default physical correction factors need to be changed. 
print("Please input your blood glucose correction factor number as determined by your doctor. For example, if you divide your current number minus your target number by 35, please enter 35.")
corfact = input("BG Correction Factor: ")

print("\nThe current default correction factor for hypoglycemia-causing events (like exercise) is 4/5, or .8 . Would you like to change this number?")
changelow = input("Enter 'y' to change, or enter 'n' to keep: ")
#((add if statement for lowfact and initialize lowfact))

print("\nThe current default correction factor for hyperglycemia-causing events like illness is 5/4, or 1.25 . Would you like to change this number?")
changehigh = input("Enter 'y to change, or enter 'n' to keep: ")
#((add if statement for highfact and initialize highfact))

#get user input on current blood glucose, carb intake, and phyiscal factors
bg = input("\nPlease enter your latest blood glucose reading: ")
carbs = input("Please enter your carbohydrate count for your meal: ")
print("\nFor the following questions, please enter 'y' for yes, or 'n' for no.")
exercise = input("Will you be doing, or have you done, any strenuous or prolonged phyiscal exercise today?: ")
alcintake = input("Will you have, or have you had, more than two low-carb alcoholic bevarages today?: ")
illness = input("Are you currently sick with a cold, the flu, or another phyiscla illness that cause hyperglycemic trends?: ")
meds = input("Are you currently taking any medications, like corticosteroids or blood pressure medication, that cause hyperglycemic trends?: ")



product_list = []
price_list = []
quantity_list =[]
calculate_list = []


#Read Inputs
while (forward == "no"):
  product = str(input("Name of product: "))

  while (product.isalpha() == False):
    print ("Not a valid string. Please enter a string.\n")
    product = str(input("Name of product: "))

  price = int(input("Price: "))
  
  quantity = int(input("Quantity: "))

  calculate = price * quantity

  product_list.append(product)
  price_list.append(price)
  quantity_list.append(quantity)
  calculate_list.append(calculate)

  forward = input("Enter 'yes' if you're done or 'no' to add another: ")

  print("\n\n")
    
#Calculate

while (x < len(product_list)):
  print(str(product_list[x]) + "                          " + str(calculate_list[x]))
  x+=1

x = 0

while (x < len(product_list)):
  total += calculate_list[x]
  x+=1

print ("\n")
print("--------------------------------")
print ("Total:                        "   + str(total))