# import the math model
import math

#display what the user will see
print("This programm computes and outputs the the surface arae of a rigth circul con.")

# Get the raduis and the height from the user
raduis = float(input("Enter the reduis of the con: "))
height = float(input("Enter the height of the con: "))

#Compute the surface area of the con.
radical = math.sqrt(raduis**2 + height**2)
surface_area = math.pi*raduis + (raduis + radical)

#Compute the surface area
print(f"The sutrface area is {surface_area}")