#Call datetime and math method
print("Write the program that Gets input to the user, perform aritmetic,displaty result from the user to see.")
import math
import datetime

#Call to user to enter the width, ratio and diameter
width = float(input("Enter the with: "))
ratio = float(input("Enter the ratio: "))
diameter = float(input("Enter the dimeter: "))

#calculat the volume
volume = math.pi*width **2 * ratio * (width * ratio + 2450 * diameter) / 10000000000

#print the tire volume
print(f"The  approximate volume is: {volume:.2f}liters")

#print date
current_datetime = datetime.date.today()

#open fille for appendind

with open("volume.txt", "a") as file:
    file.write ('{},{},{},{},{}\n'.format(
        current_datetime,
        width,
        ratio,
        diameter,
        round(volume, 2)
    ))
