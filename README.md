# CalcBolus
An insulin delivery calculator that accounts for carbohydrates, correction factors, and physiological states that affect insulin absorption.

This project builds of an already made budgeting program to initialize the math involved and edits/adds to the program to specialize it for use in calculating mealtime insulin delivery. The Quote Calculator program was chosen because it does not make use of more advanced math functions which are unnecessary for calculating bolus units. 

Basic insulin delivery is based on a formula that factors in a recent blood sugar reading, carbohydrate intake within 15 minutes of a bolus (i.e. the insulin injection), and a correction factor if blood sugar is above target range. However, there is another formula that factors in physiolocigal states and events that affect insulin absorption such as exercise, illness, certain medications, and alcohol intake. 

The program will ask the user questions that prompt input about blood sugar, carbs, target range, and their correction factor and then ask yes/no questions possibly using Boolean logic for decision trees. These decision trees will use the user input along with the formula to output units of insulin they should take. 

Because this program is for medical use, The program will first and foremost prompt the user to check with their doctor for approval before using the system. My doctor personally said that this was a good idea and she has had other patients do similar things to improve their blood sugar control. The program will also recommend that the user should re-test their blood sugars within one hour of bolusing to see if they need to make adjustments.
