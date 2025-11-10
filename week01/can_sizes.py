# Let write what the user can see
print("Let write a python program that computes and print the storege efficiency for each of 12 steel cans.")

#Let call the definition function
import math
def main():
#Start with 1# picnic
    name= "1# picnic"
    radius= 6.83
    height= 10.16
    volume= can_vol(radius, height)
    area= can_area(radius, height)
    eff= volume / area
    print(f"{name}, volume= {volume:.2f}, area= {area:.2f}, efficiency= {eff:.2f}")

    can_eff("#Tall", 7.78, 11.91)
    can_eff("#2", 7.78, 11.59)
    can_eff("#2.5", 10.32, 11.91)
    can_eff("#3Cylinder", 10.79, 17.78)
    can_eff("#5", 13.02, 14.29)
    can_eff("#6Z", 5.40, 8.89)
    can_eff("#8Z short", 6.83, 7.62)
    can_eff("#10", 15.72, 17.78)
    can_eff("#211", 6.83, 12.38)
    can_eff("#300", 7.62, 11.27)
    can_eff("#303", 8.10, 11.11)
    

#Compute the can volume
def can_vol(radius, height):
    volume= math.pi * radius**2 * height
    return volume

#Compute the can area
def can_area(radius, height):
    area= 2 * math.pi * radius * (radius + height)
    return area

#The can efficiency
def can_eff(name, radius, height):
    volume= can_vol(radius, height)
    area= can_area(radius, height)
    eff= volume / area
    print(f"{name}, volume= {volume:.2f}, area= {area:.2f}, efficiency= {eff:.2f}")

main()